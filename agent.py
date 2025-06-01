from datetime import datetime
from uuid import uuid4

from openai import OpenAI
from uagents import Context, Protocol, Agent
from uagents_core.contrib.protocols.chat import (
    ChatAcknowledgement,
    ChatMessage,
    EndSessionContent,
    TextContent,
    chat_protocol_spec,
)

# Create the agent
agent = Agent(
    name="climate_guard",
    port=8000,
    seed="climate_guard_secret_phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)

# Initialize OpenAI client with ASI-1
client = OpenAI(
    base_url='https://api.asi1.ai/v1',
    api_key='sk_67703b522cef404ba12cdb5c9b9e152e9aa86fa175d44ac79944a03e588ea3c3',
)

# Create protocol compatible with chat protocol spec
protocol = Protocol(spec=chat_protocol_spec)

@protocol.on_message(ChatMessage)
async def handle_message(ctx: Context, sender: str, msg: ChatMessage):
    # Send acknowledgement for receiving the message
    await ctx.send(
        sender,
        ChatAcknowledgement(timestamp=datetime.now(), acknowledged_msg_id=msg.msg_id),
    )

    # Collect all text chunks
    text = ''
    for item in msg.content:
        if isinstance(item, TextContent):
            text += item.text

    # Query the model based on the user question
    response = 'I am afraid something went wrong and I am unable to answer your question at the moment'
    try:
        r = client.chat.completions.create(
            model="asi1-mini",
            messages=[
                {"role": "system", "content": """
                You are ClimateGuard, an expert AI assistant focused on climate change, environmental protection, 
                and sustainable practices. Your expertise includes:
                - Climate change science and impacts
                - Carbon footprint calculation and reduction
                - Renewable energy and sustainable technologies
                - Environmental conservation and biodiversity
                - Sustainable living practices
                - Climate policy and international agreements
                
                When responding:
                1. Provide accurate, science-based information
                2. Include practical solutions and actionable steps
                3. Be encouraging and positive about climate action
                4. If asked about non-climate topics, politely redirect to climate-related aspects
                5. Use clear, accessible language while maintaining scientific accuracy
                """},
                {"role": "user", "content": text},
            ],
            max_tokens=2048,
        )
        response = str(r.choices[0].message.content)
    except Exception as e:
        ctx.logger.exception('Error querying model')
        response = f"I apologize, but I encountered an error while processing your request: {str(e)}"

    # Send the response back to the user
    await ctx.send(sender, ChatMessage(
        timestamp=datetime.utcnow(),
        msg_id=uuid4(),
        content=[
            TextContent(type="text", text=response),
        ],
    ))

@protocol.on_message(ChatAcknowledgement)
async def handle_ack(ctx: Context, sender: str, msg: ChatAcknowledgement):
    # We're not using acknowledgements for this implementation
    pass

# Attach the protocol to the agent
agent.include(protocol, publish_manifest=True)

if __name__ == "__main__":
    agent.run()
