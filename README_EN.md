# Crypto Investment Advisor Bot
[English](README_EN.md) | [한국어](README.md)

This project implements a chatbot application that analyzes cryptocurrency market trends and provides investment insights using CrewAI and chatGPT.
![image](https://github.com/user-attachments/assets/f8a7ede8-9dbb-4793-b8b3-003812f5c1b2)
[Service Link](https://huggingface.co/spaces/HANTAEK/cryptocurrency_analyst_chatbot)

## Core Features

This application provides comprehensive cryptocurrency market analysis capabilities through advanced AI tools. The system conducts real-time market trend analysis, delivers AI-powered investment insights, and offers a user-friendly interface through Gradio for seamless interaction.

## Installation Guide

We provide **two installation methods** to accommodate different user needs: a streamlined Docker installation and a local development setup using Poetry.

### Prerequisites (Common)

You'll need the following API keys to run the project.

1. OpenAI API Key
   - Sign up at the [OpenAI website](https://platform.openai.com/signup)
   - Generate your API key from the [API Keys](https://platform.openai.com/account/api-keys) page

2. Tavily API Key
   - Visit the [Tavily website](https://tavily.com/) and create an account
   - After registration, you can obtain your API key from the dashboard

**Create a `.env` file** in the project root directory and configure it with your API keys as follows.
Environmental variables in Docker do not use upper("") and lower quotation marks(''). Please set it carefully.

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### **Method 1**: Quick Installation with Docker

This method offers a straightforward way to run the application without configuring a Python environment.

1. Install Docker
   - Windows/Mac: Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
   - Linux: Install Docker through your package manager

2. Clone the Project
```bash
git clone [repository-url]
cd [repository-name]
```

3. Build Docker Image
```bash
docker build -t crypto-advisor .
```

4. Run Docker Container
```bash
docker run -p 7860:7860 --env-file .env crypto-advisor
```

### **Method 2**: Local Development Setup with Poetry

This method provides a complete development environment for customization and enhancement.

1. Install Python 3.11
   - Download and install from [Python's official website](https://www.python.org/downloads/)

2. Install Poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Clone Project and Install Dependencies
```bash
git clone [repository-url]
cd [repository-name]
poetry install
```

4. Run Application
```bash
poetry run python app.py
```

## Usage Instructions

Once you have installed the application using either method, access it by following these steps.
1. Access the application at `http://localhost:7860`
2. Verify the "Crypto Investment Advisor Bot" interface
3. Enter your cryptocurrency-related questions or analysis topics
4. Review the AI-generated analysis and investment insights


## Troubleshooting Guide

Common issues and their solutions.

1. Port Conflicts with Docker
   - Use an alternative port: `docker run -p 7861:7860 --env-file .env crypto-advisor`

2. Poetry Installation Issues
   - Recreate virtual environment: Run `poetry env remove python` followed by `poetry install`

## Contributing

Welcome contributions to improve the project. To contribute

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request
