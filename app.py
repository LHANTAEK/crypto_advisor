# 환경 변수에서 API 키 가져오기
from dotenv import load_dotenv

# CrewAI 라이브러리에서 필요한 클래스 가져오기
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import gradio as gr

load_dotenv()

# LLM
llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.3)

# Search Tool
from langchain_community.tools.tavily_search import TavilySearchResults

search_tool = TavilySearchResults()

def run_crypto_crew(topic):

    # Agent
    researcher = Agent(
    role='Market Researcher',
    goal=f'Uncover emerging trends and investment opportunities in the cryptocurrency market in 2025. Focus on the topic: {topic}.',
    backstory='Identify groundbreaking trends and actionable insights.',
    verbose=True,
    tools=[search_tool],
    allow_delegation=False,
    llm=llm,
    max_iter=3,
    max_rpm=10,
    )


    analyst = Agent(
    role='Investment Analyst',
    goal=f'Analyze cryptocurrency market data to extract actionable insights and investment leads. Focus on the topic: {topic}.',
    backstory='Draw meaningful conclusions from cryptocurrency market data.',
    verbose=True,
    allow_delegation=False,
    llm=llm,
    )


    # Tasks
    research_task = Task(
    description=f'Explore the internet to pinpoint emerging trends and potential investment opportunities. Focus on the topic: {topic}.',
    agent=researcher,
    expected_output='A detailed summary of the reserch results in string format'
    )


    analyst_task = Task(
    description=f'Analyze the provided cryptocurrency market data to extract key insights and compile a concise report. Focus on the topic: {topic}.',
    agent=analyst,
    expected_output='A refined finalized version of the report in string format'
    )


    #`Crew` is a group of agents working together to accomplish a task
    crypto_crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analyst_task],
    process=Process.sequential  
    )

    #`kickoff` method starts the crew's process
    result = crypto_crew.kickoff()

    return result.raw    # raw text 속성을 출력 


def process_query(message, history):
    return run_crypto_crew(message)


if __name__ == '__main__':
    app = gr.ChatInterface(
        fn=process_query,
        type="messages",     
        title="Crypto Investment Advisor Bot",
        description="Get insights into cryptocurrency trends to guide your investments. AI-generated results are for reference only. Invest responsibly."
    )

    app.launch(server_name="0.0.0.0", server_port=7860)
