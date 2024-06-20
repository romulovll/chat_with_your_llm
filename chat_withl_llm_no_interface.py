import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv

# Carrega variáveis de ambiente
_ = load_dotenv(find_dotenv())

st.title("Chat com Modelo de Linguagem - LangChain")

# Configuração do prompt e do modelo
system = "You are a helpful assistant."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
chat = ChatGroq(temperature=0, model_name="llama3-8b-8192")
chain = prompt | chat

response_stream = chain.invoke({"text": "Olá, tudo bem?"})

print("Resposta do modelo: ", response_stream.content)