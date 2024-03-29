from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

if __name__ == "__main__":
    # Set the environment variable OPENAI_API_KEY
    os.environ['OPENAI_API_KEY'] = "your_actual_api_key"

    # Initialize the ChatOpenAI model
    model = ChatOpenAI()

    # Add routes for ChatOpenAI model
    add_routes(
        app,
        model,
        path="/openai"
    )

    # Define prompt templates for essay and poem
    prompt = ChatPromptTemplate.from_template("provide me an essay about {topic}")
    prompt1 = ChatPromptTemplate.from_template("provide me a poem about {topic}")

    # Add routes for essay and poem prompts
    add_routes(
        app,
        prompt | model,
        path="/essay"
    )

    add_routes(
        app,
        prompt1 | model,
        path="/poem"
    )

    # Run the FastAPI application using Uvicorn server
    uvicorn.run(app, host="localhost", port=8000)





# from fastapi import FastAPI
# from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
# from langserve import add_routes
# import uvicorn
# import os

# os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

# app=FastAPI(
#     title="Langchain Server",
#     version="1.0",
#     decsription="A simple API Server"

# )

# add_routes(
#     app,
#     ChatOpenAI(),
#     path="/openai"
# )

# model=ChatOpenAI()
# prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
# prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

# add_routes(
#     app,
#     prompt|model,
#     path="/essay"

# )

# add_routes(
#     app,
#     prompt1|model,
#     path="/poem"

# )

# if __name__=="__main__":
#     uvicorn.run(app,host="localhost",port=8000)