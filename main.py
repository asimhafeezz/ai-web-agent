from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    config = BrowserConfig(
        headless=False,
        browser_instance_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",  # 👈 Your installed Chrome
    )

    browser = Browser(config=config)

    agent = Agent(
        task="Go to YouTube and search for 'how to make a cake', then list the ingredients.",
        llm=ChatOpenAI(model="gpt-4o"),
        browser=browser,
    )

    await agent.run()

asyncio.run(main())