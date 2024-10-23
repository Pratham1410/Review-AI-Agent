import taipy.gui as tp
import os
from crewai import Crew, Task, Agent
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

llm_model_name = "groq/llama-3.1-8b-instant"

def analyze_reviews(place_name):
    data_collector = Agent(
        llm=llm_model_name, 
        role="Data Collector",
        goal=f"Efficiently collect and analyze customer reviews for {place_name} from Google Maps and other relevant review platforms, providing insights into customer satisfaction and service quality.",
        backstory="As a dedicated data collector, I focus on gathering and interpreting reviews to provide actionable insights for businesses.",
        allow_delegation=False,
        tools=[SerperDevTool()],
        verbose=1
    )

    task = Task(
        description=f"Search Google for customer reviews of {place_name}, summarizing the key themes and sentiments expressed by users.",
        expected_output="A structured dataset containing customer reviews, including ratings, sentiments, and key themes identified from the feedback.",
        agent=data_collector
    )

    advisor = Agent(
        llm=llm_model_name,
        role="Change Advisor",
        goal=f"Provide actionable recommendations for improving customer satisfaction and service quality at {place_name} based on the analysis of collected reviews.",
        backstory="As a change advisor, I focus on interpreting customer feedback and offering strategic suggestions to enhance service quality and overall customer experience at businesses.",
        allow_delegation=False,
        verbose=1    
    )

    task2 = Task(
        description=f"Analyze the structured dataset of customer reviews collected from {place_name} along with original reviews, identifying specific areas for improvement and actionable suggestions.",
        expected_output="A list of actionable recommendations for improving customer satisfaction, highlighting key areas of concern and positive feedback.",
        agent=advisor  
    )

    crew = Crew(agents=[data_collector, advisor], tasks=[task, task2], verbose=1)

    # Kick off the tasks
    results = crew.kickoff()

    # Process the outputs
    data_collector_output = task.output  
    advisor_output = task2.output

    # Convert outputs to strings (if they are lists or other objects)
    data_collector_output_str = '\n'.join(data_collector_output) if isinstance(data_collector_output, list) else str(data_collector_output)
    advisor_output_str = '\n'.join(advisor_output) if isinstance(advisor_output, list) else str(advisor_output)

    return data_collector_output_str, advisor_output_str

place_name = ""
review_gist = ""
change_suggestions = ""

# Function to handle form submission and trigger review analysis
def on_submit(state):
    global place_name
    data_collector_output, advisor_output = analyze_reviews(state.place_name)
    state.review_gist = data_collector_output
    state.change_suggestions = advisor_output

# Define the page layout
page = """
# Review Analysis

Please enter the place name (e.g., Gordhan Thal Ahmedabad):

<|{place_name}|input|label=Place Name|>

<|Analyze|button|on_action=on_submit|>

### Reviews:
<|{review_gist}|text|>

### Suggested Changes:
<|{change_suggestions}|text|>
"""

# Run the GUI
gui = tp.Gui(page)
gui.run()
