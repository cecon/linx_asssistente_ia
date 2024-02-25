import os
import json
import asyncio
import aioconsole
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, ConversationalRetrievalChain
import uvicorn
from chat_service import chat
from llm import prepara_llm, prepara_llm_azure
from prompt import prepara_prompt
from vector_builder_confluence import cria_banco_confluence
from langchain.memory import ChatMessageHistory, ConversationBufferMemory


# rotina para testar o serviço
async def test():
  while True:
      print("\n")
      pergunta = input("O que você quer saber? ")
      if pergunta == ".":
        break
      resposta = await chat(pergunta)
      print("\nResposta:\n\n"+resposta)


async def main():
  criar_base = os.getenv("CRIAR_BASE_VETORIAL", "N")
  if criar_base == "S":
    confirma = input("Confirma criação da base vetorial? (S/N): ")
    if confirma == "S":
      await cria_banco_confluence()
    else:
      print("Criação da Base vetorial foi cancelada.")
  else:
    print("Inicializando o serviço de chat...")
    await test()


if __name__ == "__main__":
  asyncio.run(main())
