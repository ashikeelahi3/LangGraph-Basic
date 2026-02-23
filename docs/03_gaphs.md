# Graphs

## Hello World Graph 01

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

## Multiple Input Graphs 02

### Objectives (Multiple Input Graphs)

- Define a more complex `AgentState`
- Create a processing node that performs operations on **list data**
- Setup a `LangGraph` that processes and outputs computed result.
- Invoke the graph with structured inputs and retrieve outputs.

**Main Goal**: Learn how to handle multiple inputs

### Simple example for Graph 2

![Graph 2](../images/simple-graphs/02_simple_graph.png)

### Define AgentState with Multiple Fields

```python
class AgentState(TypedDict):
    values: List[int]
    name: str
    result: str
```

### Create Processing Node

```python
def process_values(state: AgentState) -> AgentState:
    """This function handles multiple different inputs from the state, 
    processes them, and updates the state with a result."""
    total = sum(state['values'])
    state['result'] = f"Hi there {state['name']}! The sum of your values is {total}."
    return state
```

### Build and Compile the Graph for 2

```python
graph = StateGraph(AgentState)
graph.add_node("processor", process_values)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()
```

### Exercise for Graph 2

**Your task**: Create a **Graph** where you pass in a single list of integers along with a name and an operation. If the operation is a "+", you **add** the elements and if it is a "*", you multiply the elements, **All within the same node.**

**Input**: {"name": "Ashik", "values": [1, 2, 3, 5], "operation": "*+*"}

**Output**: "HI Ashik, your answer is: 30"

*Hint*: You need an if-statement in your node.

You can check the solution here: [Multiple Inputs](../simple_graphs/02_Multiple_Inputs.ipynb)

## Sequential Graph 03

### Objectives (Sequential Graph)

- Create **multiple** `Nodes` that sequentially process and update different parts of the state.
- Connect `Nodes` together in a graph.
- Invoke the `Graph` and see how the **state is transformed** step-by-step.

**Main Goal**: Create and handle multiple `Nodes`

### Simple example for Graph 3

![Graph 3](../images/simple-graphs/03_simple_graph.png)

### Exercise for Graph 3

**Your task**:

1. Accept a user's name, age, and a list of their skills.
2. Pass the state through **three nodes** that
   - First node: Personalizes the name field with a greeting.
   - Second node: Describes the user's age.
   - Third node: Lists the user's skills in a formatted string.
3. The final output in the result field should be **combined message** in this formate:

**Output**: "Ashik, welcome to the system! You are 31 years old! You have skills in: Python, Machine Learning, and LangGraph"

*Hint*: You will need the add_edge method twice.

You can check the solution here: [Sequential Graphs](../simple_graphs/03_Sequential_Graphs.ipynb)
