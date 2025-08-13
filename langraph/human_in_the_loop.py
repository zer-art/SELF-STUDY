from typing import  Annotated
from typing_extensions import TypedDict
from langgraph .prebuilt import ToolNode , tools_condition
from langgraph.graph import StateGraph, START , END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import  tool
from langchain.chat_models import init_chat_model
from langgraph.types import interrupt , Command
from dotenv import load_dotenv
import os
load_dotenv()

memory = MemorySaver()

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

@tool
def get_price(symbol: str) -> float:
    '''Return the current price of a stock given the stock symbol
    :param symbol: stock symbol
    :return: current price of the stock
    '''
    return {
        "MSFT": 200.3,
        "AAPL": 100.4,
        "AMZN": 150.0,
        "RIL": 87.6
    }.get(symbol, 0.0)

@tool
def buy_shares(symbol: str, quantity: int , total_price :float) -> str:
    '''Buy shares of a stock
    :param symbol: stock symbol
    :param quantity: number of shares to buy
    :return: confirmation message
    '''
    decision = interrupt(f"Do you want to buy {quantity} shares of {symbol}?")
    if decision == command("yes"):
        total_price = get_price(symbol) * quantity
        return f"Bought {quantity} shares of {symbol} at a total price of {total_price}."
    elif decision == command("no"):
        return f"Did not buy {quantity} shares of {symbol}."
    else:
        total_price = get_price(symbol) * quantity
    return f"Bought {quantity} shares of {symbol} and price is {total_price}."

tools = [get_price , buy_shares]

llm = init_chat_model(
    model="gemini-1.5-flash",
    model_provider="google_genai",
    api_key=os.getenv("GEMINI_API"),
    temperature=0.2
)

llm_with_tools = llm.bind_tools(tools)


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

builder = StateGraph(State)

builder.add_node(chatbot)
builder.add_node("tools", ToolNode(tools))

builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")

graph = builder.compile(checkpointer=memory)

from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))

config = { 'configurable' : {'thread_id':'1'}}

msg = "what is the total pice of 10 MSFT and AMZN share ."

initial_state = {"messages": [
    {
        "role": "user",
        "content": msg
    }
]}

State = graph.invoke(initial_state , config=config)

print(State["messages"][-1].content)

msg1 = "buy 20 AAPL and get the total price from the previous message."

St = {"messages" : [
    {
        "role": "user",
        "content": msg1
    }
]}

State = graph.invoke(St , config=config)
print(State["messages"][-1].content)

decision = input("Do you want to buy 20 AAPL shares? (yes/no): ").strip().lower()
state = graph.invoke({"resume": decision}, config=config)
print(state["messages"][-1].content)