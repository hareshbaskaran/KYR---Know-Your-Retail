from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    user_input: str = Field(..., min_length = 1, example="Brief me about california wildfire.")
