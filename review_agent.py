import os
from crewai import Crew, Task, Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm_model_name = "groq/llama-3.1-8b-instant"
function_calling_model_name = "groq/gemma-7b-it"

place_name = "Pallidium Ahmedabad"
 
data_collector = Agent(
    llm=llm_model_name, 
    function_calling_llm=function_calling_model_name,
    role="Data Collector",
    goal=f"Efficiently collect and analyze customer reviews for {place_name} from Google Maps and other relevant review platforms, providing insights into customer satisfaction and service quality.",
    backstory="As a dedicated data collector, I focus on gathering and interpreting reviews on Google Maps and other relevant platform to provide actionable insights for businesses, enabling them to enhance their services and customer relationships.",
    allow_delegation=False,
    tools=[SerperDevTool()],  
    verbose=1
)

task = Task(
    description=f"Search Google for customer reviews of {place_name}, summarizing the key themes and sentiments expressed by users.",
    expected_output="A structured dataset containing customer reviews, including ratings, sentiments, and key themes identified from the feedback. In Bullet Points",
    agent=data_collector  
)

Advisor = Agent(
    llm=llm_model_name,
    role="Change Advisor",
    goal=f"Provide actionable recommendations for improving customer satisfaction and service quality at {place_name} based on the analysis of collected reviews.",
    backstory="As a change advisor, my focus is on interpreting customer feedback and offering strategic suggestions to enhance service quality and overall customer experience at businesses.",
    allow_delegation=False,
    verbose=1    
)

task2 = Task(
    description=f"Analyze the structured dataset of customer reviews collected from {place_name} along with all original reviews, identifying specific areas for improvement and actionable suggestions based on user feedback.",
    expected_output="A list of actionable recommendations for improving customer satisfaction, highlighting key areas of concern and positive feedback from both structured data and original reviews.",
    agent=Advisor  
)

crew = Crew(agents=[data_collector, Advisor], tasks=[task, task2], verbose=1)

results = crew.kickoff()

data_collector_output = task.output  
advisor_output = task2.output    

print("Data Collector Output:")
print(data_collector_output)

print("\nAdvisor Output:")
print(advisor_output)

