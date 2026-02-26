import os
from typing import Annotated, Sequence, TypedDict
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, ToolMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

load_dotenv()  

# Annotated - provides additional context without affecting the type itself.
# Sequence - To automatically handle the state updates for sequences such as by adding new messages to a chat history.
# BaseMessage - The foundation class for all message types in Langgraph.
# ToolMessage - Passes data back to LLM after it calls a tool such as the content and the tool name.
# SystemMessage - Message for providing instructions to the LLM


# Now what is the `add_messages` function?
# It is a reducer function
# Rule that controls how updates from nodes are combined with the existing state.
# Tells us how to merge new data into the current state.

# Without a reducer, updates would have replaced the existing value entirely!

# # Without a reducer
# state = {"messages": ["Hi!"]}
# update = {"messages": ["How are you?"]}
# new_state = {"messages": ["How are you?"]}

# # With a reducer
# state = {"messages": ["Hi!"]}
# update = {"messages": ["How are you?"]}
# new_state = {"messages": ["Hi!", "How are you?"]}


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


@tool
def add(a: int, b: int):
    """This is an addition function that adds 2 numbers together"""

    return a + b


@tool
def subtract(a: int, b: int):
    """Subtraction function"""
    return a - b


@tool
def multiply(a: int, b: int):
    """Multiplication function"""
    return a * b


tools = [add, subtract, multiply]

model = ChatGoogleGenerativeAI(
  model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY")
).bind_tools(tools) # Bind the tools to the LLM so it can call them when needed.


def model_call(state: AgentState) -> AgentState:
  system_prompt = SystemMessage(
    content="You are my AI assistant, please answer my query to the best of your ability. Make things into smaller parts if it needed."
  )
  response = model.invoke([system_prompt] + state["messages"]) # type: ignore
  return {"messages": [response]}


def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if not last_message.tool_calls:  # type: ignore
        return "end"
    else:
        return "continue"

graph = StateGraph(AgentState)
graph.add_node("our_agent", model_call)

tool_node = ToolNode(tools=tools)
graph.add_node("tools", tool_node)

graph.set_entry_point("our_agent")
graph.add_conditional_edges(
  "our_agent",
  should_continue,
  {
    "continue": "tools",
    "end": END
  }
)

graph.add_edge("tools", "our_agent")

app = graph.compile()

def print_stream(stream):
  for s in stream:
    message = s["messages"][-1]
    if isinstance(message, tuple):
      print(message)
    else:
      message.pretty_print()  

inputs = {"messages": [("user", "Add 4, 7 together and then subtract 10 from the result, then multiply the result by 2.")]}

print_stream(app.stream(inputs, stream_mode="values"))  # type: ignore
