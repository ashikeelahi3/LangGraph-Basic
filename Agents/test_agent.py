from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
  model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY")
)
messages = [HumanMessage(content="Hello, explain LangChain briefly.")]
response = model.invoke(messages)
print(response.content)
