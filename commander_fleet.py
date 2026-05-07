import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

load_dotenv()

gemini_llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("GEMINI_API_KEY")
)

sentry = Agent(
    role='Lead Systems Sentry',
    goal='Optimize Godot 4 code for battery life and GPS efficiency.',
    backstory='An expert in mobile performance who hates battery drain.',
    llm=gemini_llm,
    verbose=True
)

artisan = Agent(
    role='Master High-Fantasy Artisan',
    goal='Design lore-accurate 3D creature prompts and UI aesthetics.',
    backstory='A veteran 3D artist specializing in high-fantasy Blender workflows.',
    llm=gemini_llm,
    verbose=True
)

architect = Agent(
    role='Infrastructure Architect',
    goal='Manage Firebase, S2 Cells, and XULPLABS business logic.',
    backstory='A systems engineer focused on scalable, free-tier backends.',
    llm=gemini_llm,
    verbose=True
)

print("🚀 Fleet successfully initialized and standing by.")
