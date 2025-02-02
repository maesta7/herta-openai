from typing import Union
from herta.llms import BaseLLM
from herta.inputs import *
from openai import OpenAI, AsyncOpenAI
import os

class ChatOpenAI(BaseLLM):
    def __init__(
        self,
        api_key=None,
    ):
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.async_client = AsyncOpenAI(api_key=api_key)

    def __get_openai_msg(self, msgs: list[AI_msg, Human_msg, Tool_msg, System_msg]) -> list[dict]:
        openai_msgs = []
        for msg in msgs:
            openai_msgs.append(msg.model_dump(exclude_unset=True))
        return openai_msgs

    def __parameters_preprocess(self, kwargs: dict) -> dict:
        if "models" not in kwargs:
            raise ValueError("You must provide a model name")
        if "messages" not in kwargs:
            raise ValueError("You must provide at least one message")
        kwargs["messages"] = self.__get_openai_msg(kwargs["messages"])
        return kwargs
    
    async def chat(
        self,
        kwargs: dict
    ):
        kwargs = self.__parameters_preprocess(kwargs)
        return await self.client.beta.chat.completions.parse(**kwargs)
