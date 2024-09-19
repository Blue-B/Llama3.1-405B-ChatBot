"""Run this model in Python

> pip install azure-ai-inference
"""
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('token')


# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(token),
)

Ucontent = "당신은 AI비서입니다. 항상 반드시 영어가 아닌 한국어로만 응답을 하세요. 대답은 너무 길게 답변하지 마세요"
while(1):
  
    response = client.complete(
        messages=[
            SystemMessage(content="""안녕하세요! AI 비서입니다."""),
            UserMessage(content=Ucontent),
        ],
        model="Meta-Llama-3.1-405B-Instruct",
        temperature=0.8,
        max_tokens=4096,
        top_p=0.1
    )

    print(response.choices[0].message.content)
    Ucontent = input('User: ')