import asyncio
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

# Get API key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# External OpenAI client (Gemini endpoint)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Configure the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# RunConfig (optional, but useful for tracing/debugging)
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the agent
agent = Agent(
    name="assistant",
    instructions="You are a abid ali personal agent.tell hello from abid e is piaic student.roll no is 256874.",
    model=model
)

# Main async runner
async def main():
    result = await Runner.run(
        agent,
        "tellme short  about abid ali?",
         run_config=RunConfig(model_provider=model),
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
