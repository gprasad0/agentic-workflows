# from openai import AsyncOpenAI

# from config import settings


# class LLMClient:
#     def __init__(self):
#         self.client = AsyncOpenAI(
#             api_key=settings.GOOGLE_GEMINI_API_KEY,
#             base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#         )

#         self.model = settings.MODEL_NAME

#     async def generate(self, prompt: str) -> str:
#         # response = await self.client.responses.create(
#         #     model="gemini-2.5-flash",
#         #     input="tell me a joke in one senctence",
#         # )
#         # print(response.output_text)

#         # return response.output_text
#         return "hi"


# client = LLMClient()
