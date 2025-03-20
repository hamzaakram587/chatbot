import streamlit as st
import requests as req
import os
import load_dotenv

# load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHIAN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

st.title("Client side of langchain")
gpt_input = st.text_input("10 words on :")
ollama_input = st.text_input("15 words on :")

def get_gpt_responce(gptinput):
    res = req.post("http://localhost:8000/gpt/invoke", 
                   json={"input": {"topic" : gpt_input} })
    
    print(res.json)
    return res.json()['output']['content']



def get_ollama_responce(ollama_input):
    res = req.post("http://localhost:8000/ollama/invoke", 
                   json={"input": {"topic" : ollama_input} })
    
    return res.json()["output"]






if gpt_input:
    st.write(get_gpt_responce(gpt_input))


if ollama_input:
    st.write(get_ollama_responce(ollama_input))