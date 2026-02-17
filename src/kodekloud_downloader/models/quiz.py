import concurrent.futures
from typing import Dict, List, Optional

import requests
from pydantic import BaseModel, ConfigDict, Field


class QuizQuestion(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: Dict[str, str] = Field(alias="_id")
    type: int
    correctAnswers: List[str]
    code: Dict[str, str]
    question: str
    answers: List[str]
    labels: Optional[List[str]] = None
    documentationLink: Optional[str] = None
    explanation: Optional[str] = None
    topic: Optional[str] = None


class Quiz(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    id: Dict[str, str] = Field(alias="_id")
    questions: Dict[str, str]
    name: Optional[str] = None
    topic: Optional[str] = None
    projectId: Optional[str] = None
    order: Optional[str] = None

    def fetch_questions(self) -> List[QuizQuestion]:
        quiz_questions = []

        def fetch_question(question_id):
            params = {
                "id": question_id,
            }
            url = "https://mcq-backend-main.kodekloud.com/api/questions/question"
            response = requests.get(url, params=params)
            response.raise_for_status()
            if question_json := response.json():
                quiz_questions.append(QuizQuestion(**question_json))

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(fetch_question, self.questions.values())

        return quiz_questions
