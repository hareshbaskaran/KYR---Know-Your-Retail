from fastapi import FastAPI, HTTPException, Form, File, UploadFile
from pydantic import BaseModel
from services.llm_providers import GeminiLLMProvider
from models.request import ChatRequest
from models.response import ChatResponse
from services.agent_executors import CsvAgentExecutor
import os
import tempfile
from typing import Union

app = FastAPI()
gemini_provider = GeminiLLMProvider()

# Pydantic model for chat with CSV request
class ChatWithCsvRequest(BaseModel):
    user_input: str
    csv_file: UploadFile

# Helper function to handle the lifecycle of the temporary CSV file
async def handle_temp_csv(csv_file: UploadFile) -> str:
    try:
        # Save the uploaded CSV to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_csv:
            temp_csv.write(await csv_file.read())
            temp_csv_path = temp_csv.name
        return temp_csv_path
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving CSV: {str(e)}")


# Health check route
@app.get("/")
async def health_check():
    return {"status": "ok", "message": "API is running"}

# Chat route
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Get the LLM from the provider
        llm = gemini_provider.get_llm()

        # Construct messages for the model
        messages = [
            ("system", "You are a helpful assistant"),
            ("human", request.user_input),
        ]

        # Invoke the LLM
        ai_msg = llm.invoke(messages)

        # Return the response
        return ChatResponse(response=ai_msg.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Chat with CSV route
@app.post("/chat-with-csv", response_model=ChatResponse)
async def chat_with_csv(request: ChatWithCsvRequest):
    try:
        # Handle the temporary CSV file
        temp_csv_path = await handle_temp_csv(request.csv_file)

        # Initialize the LLM and executor
        llm = gemini_provider.get_llm()
        csv_executor = CsvAgentExecutor(llm=llm, csv_path=temp_csv_path)

        response = csv_executor.invoke_agent_executor(request.user_input)

        # Clean up the temporary file
        os.remove(temp_csv_path)

        # Return the response
        return ChatResponse(response=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
