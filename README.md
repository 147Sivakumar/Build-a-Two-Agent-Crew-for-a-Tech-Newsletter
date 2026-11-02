# Tech Daily — Two-Agent Newsletter Crew

An AI-powered technology newsletter generator built with **CrewAI**, **OpenAI**, and **Serper API**. The project uses two AI agents working sequentially to research current technology news and produce a concise five-line newsletter.

## Project Overview

The goal of this project is to automate the process of researching technology news and converting it into a short, readable daily briefing.

### AI Agents

**1. Technology News Researcher**
- Searches for recent technology news using Serper.
- Prefers credible news sources.
- Collects headlines, summaries, publication dates, and article URLs.
- Avoids guessing publication dates.

**2. Tech Newsletter Writer**
- Receives the Researcher's findings as task context.
- Summarizes the research into a concise newsletter.
- Produces exactly five content lines.

## Features

- Two-agent AI workflow using CrewAI.
- Sequential task execution.
- Web search using Serper API.
- OpenAI-powered research and writing.
- Context sharing between agents.
- Publication-date verification instructions.
- Structured five-line newsletter output.
- Environment variables for API key management.

## Technology Stack

- Python
- CrewAI
- CrewAI Tools
- OpenAI API
- Serper API
- python-dotenv

## Project Structure

```text
weather-news-agent/
│
├── news_crew.py       # Main two-agent newsletter application
├── weather_news.py    # Previous weather-news assignment
├── .env               # Private API keys (not committed)
├── .env.example       # Environment variable template
├── .gitignore         # Excludes secrets and temporary files
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## Prerequisites

Before running the project, install:

- Python 3.10 or a compatible version supported by your installed CrewAI release.
- An OpenAI API key.
- A Serper API key.

## Installation and Setup

### 1. Clone the repository

```cmd
git clone https://github.com/147Sivakumar/weather-news-agent.git
cd weather-news-agent
```

### 2. Create a virtual environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```cmd
python -m pip install --upgrade pip
python -m pip install "crewai[tools]" python-dotenv
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
MODEL=your_supported_crewai_model
```

Replace the placeholders with your own values. Use a model identifier supported by your CrewAI and OpenAI configuration.

**Security:** Never upload your actual API keys to GitHub.

### 5. Run the application

```cmd
python news_crew.py
```

The Researcher searches for technology news first. The Writer then uses the research results to generate the newsletter.

## Workflow

```text
User runs news_crew.py
          |
          v
Technology News Researcher
          |
          v
Search recent technology news
          |
          v
Research results passed as context
          |
          v
Tech Newsletter Writer
          |
          v
Final five-line newsletter
```

The crew uses `Process.sequential`, so the research task runs before the writing task.

## Expected Output Format

The final newsletter contains exactly five content lines:

```text
1. First technology news story.
2. Second technology news story.
3. Third technology news story.
Why it matters: The impact of these developments.
Takeaway: The main lesson for readers.
```

The actual stories depend on the research results returned during each run.

## Configuration and Security

- Keep `.env` private and excluded through `.gitignore`.
- Commit `.env.example` with placeholders only.
- Do not share API keys, access tokens, or other secrets in screenshots.
- Treat generated news summaries as AI-produced content and verify important facts against the linked sources.

## Learning Outcomes

This project demonstrates:

- Creating AI agents with distinct roles.
- Assigning tools to specific agents.
- Defining tasks with clear expected outputs.
- Passing task results through context.
- Building sequential multi-agent workflows.
- Managing API credentials using environment variables.

## Future Improvements

- Add a web dashboard for viewing newsletters.
- Save generated newsletters to text, CSV, or Excel files.
- Maintain a history of previous runs.
- Add source validation and duplicate-story detection.
- Connect the dashboard to the live CrewAI workflow.

## Author

**Sivakumar**

GitHub: [147Sivakumar](https://github.com/147Sivakumar)

## Disclaimer

This project is an educational demonstration of AI-agent orchestration. News summaries are generated automatically and should be checked against the original sources.
