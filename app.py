#create apis for all the chains
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()



os.environ["OPENAI_API_KEY"] =  os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="langchain serve api class",
    version="1.0",
    description="simple api class"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify allowed domains)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


# add_routes(
#     app,
#     ChatOpenAI(),
#     path = "/openai"
# )

gpt_llm = ChatOpenAI()
ollama_llm = Ollama(model="llama3.2")


prompt1 = ChatPromptTemplate.from_template("write 10 word on this {topic}")
promp2 = ChatPromptTemplate.from_template("write 15 words essay on this {topic}")

add_routes(
    app,
    prompt1|gpt_llm,
    path="/gpt"

)

add_routes(
    app,
    promp2|ollama_llm,
    path="/ollama"
)


if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)