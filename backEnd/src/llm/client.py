from openai import AsyncOpenAI
from pydantic import BaseModel
from typing import TypeVar, Type

from config import settings

T = TypeVar("T", bound=BaseModel)


class LLMClient:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.GOOGLE_GEMINI_API_KEY,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )

        self.model = settings.MODEL_NAME

    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        print(response.model_dump_json(indent=2))

        return response.choices[0].message.content

    async def generate_structured(
        self, userPrompt: str, response_model: Type[T], systemPrompt: str = ""
    ) -> T:
        """Send a prompt and get back a validated Pydantic model instance."""
        messages = []
        if systemPrompt:
            messages.append({"role": "system", "content": systemPrompt})
        messages.append({"role": "user", "content": userPrompt})
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": response_model.__name__,
                    "schema": response_model.model_json_schema(),
                },
            },
        )
        raw = response.choices[0].message.content
        return response_model.model_validate_json(raw)


client = LLMClient()
