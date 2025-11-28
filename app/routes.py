from fastapi import APIRouter, HTTPException, Depends
from .schemas import NoteInput, QueryInput, APIResponse, Question, QuestionsInput
from .utils import PromptEngine
from typing import List, Union

router = APIRouter()

def get_engine():
    return PromptEngine()

@router.post("/api/summarize", response_model=APIResponse)
async def summarize_notes_route(note: NoteInput, engine: PromptEngine = Depends(get_engine)):
    try:
        summary = await engine.summarize_notes(note.content, note.detail)
        return APIResponse(status="success", data=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/questions", response_model=APIResponse)
async def generate_questions_route(payload: QuestionsInput, engine: PromptEngine = Depends(get_engine)):
    try:
        questions = await engine.generate_questions(
            content=payload.content,
            num_questions=payload.count,
            difficulty=payload.difficulty,
            types=payload.types.dict(),
        )
        return APIResponse(status="success", data=questions)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/api/explain", response_model=APIResponse)
async def explain_concept_route(query: QueryInput, engine: PromptEngine = Depends(get_engine)):
    try:
        explanation = await engine.explain_concept(query.query, query.context or "")
        return APIResponse(status="success", data=explanation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
