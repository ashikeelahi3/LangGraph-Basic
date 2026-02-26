import os
from typing import List, TypedDict, Union
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class AgentState(TypedDict):
  messages: List[Union[HumanMessage, AIMessage]]

llm = ChatGoogleGenerativeAI(
  model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY")
)

def process(state: AgentState) -> AgentState:
  """This node will solve the request you input"""

  response = llm.invoke(state["messages"])
  # Append the AI's response to the messages list to maintain conversation history
  state["messages"].append(AIMessage(content=response.content))

  print(f"\nAI: {response.content}")
  # print("CURRENT STATE: ", state["messages"])
  return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process") 
graph.add_edge("process", END)
agent = graph.compile()

conversation_history = []

with open("conversation_history.txt", "r") as file:
  lines = file.readlines()
  for line in lines:
    if line.startswith("User:"):
      conversation_history.append(HumanMessage(content=line[5:].strip()))
    elif line.startswith("AI:"):
      conversation_history.append(AIMessage(content=line[3:].strip()))

user_input = input("Enter: ")
while user_input != "exit": 
  conversation_history.append(HumanMessage(content=user_input))  # Add user input to conversation history
  result = agent.invoke({"messages": conversation_history})
  conversation_history = result["messages"]  # Update conversation history with the latest messages (including AI response)
    
  user_input = input("Enter: ")

with open("conversation_history.txt", "w") as file:
  print("inside with open block")
  file.write("Your Conversation History:\n")  
  for message in conversation_history:
    if isinstance(message, HumanMessage):
      file.write(f"User: {message.content}\n")
    elif isinstance(message, AIMessage):
      file.write(f"AI: {message.content}\n")
  file.write("\nEnd of Conversation History.")  

print("Conversation history saved to conversation_history.txt")  