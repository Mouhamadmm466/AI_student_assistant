# Summarization Prompts
SUMMARIZE_SYSTEM_PROMPT = """You are an expert academic assistant. Your goal is to summarize study notes effectively based on the user's requested detail level.
Ensure the summary is clear, accurate, and captures the key points."""

SUMMARIZE_USER_PROMPT = """Please summarize the following notes.
Detail Level: {detail}

Notes:
{content}
"""

# Question Generation Prompts
QUESTION_GEN_SYSTEM_PROMPT = """You are an expert teacher. Create practice questions based on the provided text.
Output the result strictly as a JSON array of objects, where each object has 'question', 'answer', and 'type' keys.
Do not include any markdown formatting or extra text outside the JSON."""

QUESTION_GEN_USER_PROMPT = """Generate {num_questions} practice questions based on the following content.
Difficulty: {difficulty}
Allowed question types: {types}
Only use the allowed types. Keep answers concise.

Content:
{content}
"""

# Conceptual Explanation Prompts
EXPLAIN_SYSTEM_PROMPT = """You are a knowledgeable tutor. Explain the concept clearly and concisely.
If context is provided, use it to tailor your explanation. Use analogies where helpful."""

EXPLAIN_USER_PROMPT = """Explain the following concept: "{query}"

Context (if any):
{context}
"""
