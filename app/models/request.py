from pydantic import BaseModel, Field
from fastapi import UploadFile, File, Form


class ChatRequest(BaseModel):
    user_input: str = Field(
        ..., min_length=1, example="Brief me about california wildfire."
    )


class ChatWithCsvRequest(BaseModel):
    user_input: str = Form(...)
    csv_file: UploadFile = File(...)
