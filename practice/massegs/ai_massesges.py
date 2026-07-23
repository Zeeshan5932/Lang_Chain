from langchain_core.messages import SystemMessage,HumanMessage,AIMessage,ToolMessage

messages = [

    # 1. System Message
    SystemMessage(
        content="You are a helpful AI teacher. Explain everything in simple language."
    ),

    # 2. Human Message
    HumanMessage(
        content="What is LangChain?"
    ),

    # 3. AI Message
    AIMessage(
        content="LangChain is an open-source framework used to build AI applications."
    ),

    # 4. Tool Message
    ToolMessage(
        content="Temperature in Lahore is 35°C",
        tool_call_id="weather_tool_1"
    )
]

for message in messages:
    print(f"{type(message).__name__}:")
    print(message.content)
    print("-" * 50)