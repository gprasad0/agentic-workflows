from openai import AsyncOpenAI

from config import settings


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
        # return "hi"


client = LLMClient()
