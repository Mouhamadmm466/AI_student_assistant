from pydantic import BaseModel
from typing import Union, List, Optional

class NoteInput(BaseModel):
    content: str
    detail: str = "concise"  # concise, detailed, bullet-points

class QueryInput(BaseModel):
    query: str
    context: Optional[str] = None

class QuestionTypes(BaseModel):
    mc: bool = True
    short: bool = False
    tf: bool = False

class QuestionsInput(BaseModel):
    content: str
    count: int = 5
    difficulty: str = "medium"
    types: QuestionTypes = QuestionTypes()

class Question(BaseModel):
    question: str
    answer: str
    type: str  # multiple-choice, true/false, open-ended

class APIResponse(BaseModel):
    status: str
    data: Union[str, List[Question]]
