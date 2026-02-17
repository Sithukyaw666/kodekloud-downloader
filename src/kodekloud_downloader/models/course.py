from typing import List, Optional

from pydantic import BaseModel, ConfigDict, HttpUrl


class Category(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    name: str


class Tutor(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    name: str
    bio: Optional[str] = None
    description: Optional[str] = None
    avatar_url: Optional[HttpUrl] = None


class Lesson(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    title: str
    type: str  # e.g., "video", "lab", "quiz"
    position: int
    duration: Optional[int] = 0  # Duration is optional and may not be present


class Module(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    title: str
    position: int
    lessons_count: Optional[int] = 0
    lessons: List[Lesson] = []


class IncludesSection(BaseModel):
    model_config = ConfigDict(extra="ignore")

    modules_count: Optional[int] = 0
    lessons_count: Optional[int] = 0
    lab_lessons: Optional[bool] = False
    lab_lesson_count: Optional[int] = 0
    quiz_lessons: Optional[bool] = False
    quiz_lesson_count: Optional[int] = 0
    mock_exams: Optional[bool] = False
    community_support: Optional[bool] = None
    hours_of_video: Optional[int] = 0
    course_duration: Optional[int] = 0


class CourseDetail(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    slug: str
    title: str
    thumbnail_url: Optional[HttpUrl] = None
    tutors: List[Tutor] = []
    popularity: Optional[int] = 0
    difficulty_level: Optional[str] = None
    categories: List[Category] = []
    plan: Optional[str] = None
    excerpt: Optional[str] = None
    description: Optional[str] = ""
    lessons_count: Optional[int] = 0
    userback_id: Optional[str] = None
    hidden: Optional[bool] = False
    modules: List[Module] = []
    includes_section: Optional[IncludesSection] = None
