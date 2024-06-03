import os
from typing import Any, List
from openai import AsyncAzureOpenAI
from openai.types.chat import ChatCompletionMessageParam

class LargeLanguageModelRepository:
    def __init__(self):
        self.async_client = AsyncAzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_MODEL"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),   
        )

    async def achat_completion(self, messages: List[ChatCompletionMessageParam] ) -> str:
        response = self.async_client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_MODEL"),
            temperature=0,
            messages=messages
        )
        return response.choices[0].message.content