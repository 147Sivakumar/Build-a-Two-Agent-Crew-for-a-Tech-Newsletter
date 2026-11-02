
import os
from datetime import date
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Load API keys and model settings from .env
load_dotenv()
today = date.today().strftime("%B %d, %Y")
model = os.getenv("MODEL")
if not model:
    raise ValueError("MODEL is missing from your .env file.")

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing from your .env file.")

if not os.getenv("SERPER_API_KEY"):
    raise ValueError("SERPER_API_KEY is missing from your .env file.")

# Web search tool: assigned only to the Researcher
search_tool = SerperDevTool()

researcher = Agent(
    role="Technology News Researcher",
    goal="Find today's three most important technology news stories.",
    backstory=(
        "You are a careful technology journalist who researches current "
        "news and returns three distinct stories with reliable source URLs, "
        "dates, and concise factual summaries."
    ),
    tools=[search_tool],
    llm=model,
    verbose=True,
)

writer = Agent(
    role="Tech Newsletter Writer",
    goal="Turn the research into a clear newsletter with exactly five lines.",
    backstory=(
        "You are a concise technology newsletter editor. You use only "
        "the research provided to you and never invent facts."
    ),
    llm=model,
    verbose=True,
)

find = Task(
        description=(
        f"Today's date is {today}. Find three important technology news "
        f"stories relevant as of {today}. Search for recent stories using "
        "the current date, but never treat the search date as the article's "
        "publication date. Check the actual publication date shown on each "
        "source. Prefer stories published today or in the previous 7 days. "
        "If a story is older than 7 days, exclude it unless no suitable "
        "recent story is available. Never invent or guess a publication date. "
        "If the date cannot be verified, say 'publication date unverified'. "
        "Prefer credible sources such as Reuters, AP, BBC, or established "
        "technology publications. For each story, provide its headline, "
        "factual summary, actual publication date, and direct article URL."
    ),
    expected_output=(
        "Three distinct current technology news stories, each with a "
        "headline, brief summary, publication date when available, "
        "and source URL."
    ),
    agent=researcher,
)
write = Task(
    description=(
        "Using only the Researcher's findings, write a technology newsletter "
        "with exactly five content lines: three numbered story lines, one "
        "'Why it matters' line, and one 'Takeaway' line. Each line must be "
        "concise. Do not add a title, introduction, blank line, or extra "
        "bullet to the five-line newsletter."
    ),
    expected_output=(
        "Exactly five lines of newsletter content: lines 1-3 are three "
        "numbered technology stories, line 4 begins 'Why it matters:', "
        "and line 5 begins 'Takeaway:'. No title or extra lines."
    ),
    agent=writer,
    context=[find],
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[find, write],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("TECH DAILY | TWO-AGENT NEWSLETTER")
    print("=" * 50 + "\n")

    result = crew.kickoff()

    print("\n" + "=" * 50)
    print("FINAL NEWSLETTER")
    print("=" * 50)
    print(result.raw)
