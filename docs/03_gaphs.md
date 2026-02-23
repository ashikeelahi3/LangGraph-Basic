# Graphs

## Hello World Graph

### Objectives

- Understand and define the `AgentState` structure
- Create simple node functions to process and update state
- Set up a basic `LangGraph` structure
- Compile and invoke a LangGraph graph
- Understand how data flows through a single-node in `LangGraph`

### Simple example for Graph 1

![Graph 1](../images/simple-graphs/01_simple_graph.png)

### Installation

```bash
pip install langgraph IPython
```

### Import Required Libraries

```python
from typing import Dict, TypedDict
from langgraph.graph import StateGraph
```

`StateGraph` is a framework that helps you design and manage the flow of tasks in your application using a graph.

### Define AgentState and Node Function

```python
class AgentState(TypedDict):
    message: str

def greeting_node(state: AgentState) -> AgentState:
    """Simple node that adds a greeting message to the state"""
    state['message'] = "Hey " + state['message'] + ", how is your day going?"
    return state
```

`AgentState` is a shared data structure that keeps track of information as your application runs.

### Build and Compile the Graph

```python
graph = StateGraph(AgentState)

graph.add_node("greeter", greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()
```

### Exercise for Graph 1

#### Your task

Create a **Personalized Compliment Agent** using LangGraph!

**Input**: {"name": "Bob"}

**Output**: "Bob, you're doing an amazing job learning LangGraph!"

*Hint*: You have to concatenate the state, not replace it.

You can check the solution here: [Basic Graphs](../simple_graphs/01_Basic_Graphs.ipynb)

## Multiple Input Graphs

### Objectives (Multiple Input Graphs)

- Define a more complex `AgentState`
- Create a processing node that performs operations on **list data**
- Setup a `LangGraph` that processes and outputs computed result.
- Invoke the graph with structured inputs and retrieve outputs.

**Main Goal**: Learn how to handle multiple inputs
