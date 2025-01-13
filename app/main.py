from fastapi import FastAPI, HTTPException,UploadFile, File, Form
from services.llm_providers import GeminiLLMProvider
from models.request import ChatRequest, ChatWithCsvRequest
from models.response import ChatResponse
from services.agent_executors import CsvAgentExecutor
import tempfile

app = FastAPI()
gemini_provider = GeminiLLMProvider()

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
def health_check():
    return {"status": "ok", "message": "API is running"}

# Chat route
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        llm = gemini_provider.get_llm()
        messages = [
            ("system", "You are a helpful assistant"),
            ("human", request.user_input),
        ]

        ai_msg = llm.invoke(messages)
        return ChatResponse(response=ai_msg.content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat-with-csv", response_model=ChatResponse)
#async def chat_with_csv(request: ChatWithCsvRequest):
async def chat_with_csv(
        user_input : str = Form(...),
        csv_file: UploadFile = File(...)
):
    try:
        llm = gemini_provider.get_llm()

        temp_csv_path = await handle_temp_csv(csv_file)
        csv_executor = CsvAgentExecutor(llm=llm, csv_path=temp_csv_path)

        response = csv_executor.invoke_agent_executor(user_input)
        return ChatResponse(response=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

### working code ###