
# 🚀 Customer Review Analysis AI Agent 📊

This project automates the process of collecting and analyzing customer reviews from platforms like Google Maps using AI agents from the CrewAI framework. It provides deep insights into customer satisfaction, identifies key themes from reviews, and suggests actionable recommendations for improving services.

## 📋 Project Overview

The project utilizes two agents:
1. **Data Collector Agent** 🤖: Gathers and structures customer reviews, summarizing key themes and sentiments.
2. **Change Advisor Agent** 💼: Analyzes the structured data and provides actionable insights to improve service quality.

## 💻 Key Components

- **Agents:** CrewAI agents were used for both data collection and recommendations.
- **Tools:** `SerperDevTool` was integrated to search and retrieve Google Maps reviews.
- **LLMs:** Utilized powerful language models `groq/llama-3.1-8b-instant` and `groq/gemma-7b-it` for intelligent processing.

## 🚀 Features

- **Automated Data Collection**: Automatically fetches reviews from Google Maps.
- **Sentiment Analysis**: Extracts key sentiments and themes from reviews.
- **Actionable Insights**: Provides detailed recommendations based on user feedback.

## 🧠 Agents Involved

### 1. Data Collector Agent

- **Goal**: Collect and analyze customer reviews for a specified location.
- **Backstory**: Focuses on gathering and interpreting reviews to help businesses improve.
- **Tool**: Integrates with Google Maps API using `SerperDevTool`.
- **Expected Output**: Structured dataset with key themes, ratings, and sentiments from user reviews.

### 2. Change Advisor Agent

- **Goal**: Offer strategic advice to enhance service quality based on review analysis.
- **Backstory**: Interprets feedback to provide businesses with actionable steps for improvement.
- **Expected Output**: A list of specific recommendations for improving customer satisfaction.

## 📊 Example Tasks

### Task 1: Collect Reviews
- **Description**: Search Google for customer reviews for a given location.
- **Output**: Structured data with key insights in bullet points.

### Task 2: Analyze & Recommend
- **Description**: Analyze collected reviews and provide improvement suggestions.
- **Output**: A list of actionable suggestions based on feedback.

## ⚙️ How to Run

1. Clone the repository.
   ```bash
   git clone https://github.com/Pratham1410/Review-AI-Agent.git
   cd Review-AI-Agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Add your `SERPER_API_KEY` and `GROQ_API_KEY` in `.env` file.
   
4. Run the script:
   ```bash
   python review_agent.py
   ```
5. Running the ui:
  ```bash
   python UI_Review_agent.py
   ```
   

## 🔑 API Keys

You need the following API keys to run this project:
- `SERPER_API_KEY`: For retrieving reviews from Google Maps.
- `GROQ_API_KEY`: For utilizing the LLM models.


