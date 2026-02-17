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


class Course(BaseModel):
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


class Metadata(BaseModel):
    model_config = ConfigDict(extra="ignore")

    limit: Optional[int] = 0
    page: Optional[int] = 0
    total_count: Optional[int] = 0
    next_page: Optional[int] = None


class ApiResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    courses: List[Course] = []
    metadata: Optional[Metadata] = None
