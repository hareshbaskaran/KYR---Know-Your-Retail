from services.llm.gemini_llm import GeminiLLMProvider

llm = GeminiLLMProvider().get_llm()

######### test - chatGenerativeModel ##########
messages = [
    (
        "system",
        "You are a helpful assistant",
    ),
    ("human", "brief me about los angeles wild fire"),
]
ai_msg = llm.invoke(messages)

print(ai_msg.content)

