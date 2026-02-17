from pydantic import HttpUrl
from kodekloud_downloader.models.course import CourseDetail, IncludesSection

def test_includes_section_missing_fields():
    data = {
        "modules_count": 1,
        "lessons_count": 12,
        "lab_lessons": True,
        "lab_lesson_count": 4,
        "quiz_lessons": False,
        "quiz_lesson_count": 0,
        "mock_exams": False,
        "hours_of_video": 718,
        # community_support is missing
    }
    obj = IncludesSection(**data)
    assert obj.community_support is None
    assert obj.course_duration == 0

def test_course_detail_missing_fields():
    # Minimal data for CourseDetail
    data = {
        "id": "123",
        "slug": "test-course",
        "title": "Test Course",
        "thumbnail_url": "https://example.com/thumb.png",
        "tutors": [],
        "popularity": 100,
        "categories": [],
        "plan": "premium",
        "description": "A test course",
        "lessons_count": 10,
        "hidden": False,
        "modules": [],
        "includes_section": {
            "modules_count": 1,
            "lessons_count": 12,
            "lab_lessons": True,
            "lab_lesson_count": 4,
            "quiz_lessons": False,
            "quiz_lesson_count": 0,
            "mock_exams": False,
            "hours_of_video": 718,
        }
    }
    # difficulty_level, excerpt, userback_id are missing
    obj = CourseDetail(**data)
    assert obj.difficulty_level is None
    assert obj.excerpt is None
    assert obj.userback_id is None
    assert obj.includes_section.community_support is None
