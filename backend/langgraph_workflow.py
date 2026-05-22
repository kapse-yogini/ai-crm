from typing import TypedDict

from langgraph.graph import StateGraph, END


class CRMState(TypedDict):
    customer_name: str
    customer_email: str
    analysis: str


# TOOL 1
def create_customer_tool(state):
    print("Create Customer Tool Running")
    return state


# TOOL 2
def read_customer_tool(state):
    print("Read Customer Tool Running")
    return state


# TOOL 3
def update_customer_tool(state):
    print("Update Customer Tool Running")
    return state


# TOOL 4
def delete_customer_tool(state):
    print("Delete Customer Tool Running")
    return state


# TOOL 5 (AI TOOL)
def analyze_customer_tool(state):
    name = state["customer_name"]

    if len(name) > 5:
        analysis = "High Value Lead"
    else:
        analysis = "Normal Lead"

    state["analysis"] = analysis

    return state


graph = StateGraph(CRMState)

graph.add_node("create_customer", create_customer_tool)

graph.add_node("read_customer", read_customer_tool)

graph.add_node("update_customer", update_customer_tool)

graph.add_node("delete_customer", delete_customer_tool)

graph.add_node("analyze_customer", analyze_customer_tool)

graph.set_entry_point("create_customer")

graph.add_edge("create_customer", "read_customer")

graph.add_edge("read_customer", "update_customer")

graph.add_edge("update_customer", "delete_customer")

graph.add_edge("delete_customer", "analyze_customer")

graph.add_edge("analyze_customer", END)

workflow = graph.compile()