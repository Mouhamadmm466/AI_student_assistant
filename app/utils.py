import os
import json
import httpx
from typing import List, Dict, Any
from dotenv import load_dotenv
from .prompts import (
    SUMMARIZE_SYSTEM_PROMPT, SUMMARIZE_USER_PROMPT,
    QUESTION_GEN_SYSTEM_PROMPT, QUESTION_GEN_USER_PROMPT,
    EXPLAIN_SYSTEM_PROMPT, EXPLAIN_USER_PROMPT
)
from .schemas import Question

load_dotenv()

class PromptEngine:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY is not set in environment variables.")

    async def _call_gemini(self, system_prompt: str, user_prompt: str, temperature: float = 0.5) -> str:
        prompt_text = f"{system_prompt.strip()}\n\n{user_prompt.strip()}"
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": prompt_text}]
                }
            ],
            "generationConfig": {
                "temperature": temperature
            }
        }

        url = f"{self.base_url}/models/{self.model}:generateContent?key={self.api_key}"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload, timeout=30.0)
                response.raise_for_status()
                data = response.json()
                return data["candidates"][0]["content"]["parts"][0]["text"].strip()
            except httpx.HTTPStatusError as e:
                raise Exception(f"Gemini API Error: {e.response.text}")
            except Exception as e:
                raise Exception(f"An error occurred: {str(e)}")

    async def summarize_notes(self, content: str, detail: str) -> str:
        user_prompt = SUMMARIZE_USER_PROMPT.format(detail=detail, content=content)
        return await self._call_gemini(SUMMARIZE_SYSTEM_PROMPT, user_prompt, temperature=0.3)

    async def generate_questions(
        self,
        content: str,
        num_questions: int = 5,
        difficulty: str = "medium",
        types: Dict[str, bool] | None = None
    ) -> List[Question]:
        type_labels = {
            "mc": "multiple-choice",
            "short": "short-answer",
            "tf": "true/false"
        }
        allowed_types = [label for key, label in type_labels.items() if types and types.get(key)]
        if not allowed_types:
            allowed_types = list(type_labels.values())

        user_prompt = QUESTION_GEN_USER_PROMPT.format(
            num_questions=num_questions,
            difficulty=difficulty,
            types=", ".join(allowed_types),
            content=content
        )
        response_text = await self._call_gemini(QUESTION_GEN_SYSTEM_PROMPT, user_prompt, temperature=0.7)
        
        try:
            # Attempt to parse JSON response
            # Clean up potential markdown code blocks if present
            cleaned_text = response_text.replace("```json", "").replace("```", "").strip()
            questions_data = json.loads(cleaned_text)
            
            questions = []
            for q in questions_data:
                questions.append(Question(**q))
            return questions
        except json.JSONDecodeError:
            raise Exception("Failed to parse questions from AI response.")
        except Exception as e:
            raise Exception(f"Error processing questions: {str(e)}")

    async def explain_concept(self, query: str, context: str = "") -> str:
        user_prompt = EXPLAIN_USER_PROMPT.format(query=query, context=context)
        return await self._call_gemini(EXPLAIN_SYSTEM_PROMPT, user_prompt, temperature=0.5)
