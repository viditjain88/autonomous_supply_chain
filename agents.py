
"""
agents.py

Defines specialized AI agents for the Autonomous Supply Chain system.

Agents:
    - logistics_agent: Optimizes shipping routes and vendor relationships.
    - demand_agent: Forecasts future product demand.
    - inventory_agent: Manages inventory levels and reduces costs.

Each agent is created using CrewAI's Agent class and is assigned a specific role, goal, and backstory.
"""



import ollama

# Helper function to call Ollama local model (gemma3:4b)
def ollama_ask(prompt, system_instruction=None):
    if system_instruction:
        prompt = f"{system_instruction}\n{prompt}"
    response = ollama.generate(
        model="gemma3:4b",
        prompt=prompt
    )
    return response['response']

# Agent classes using Gemini
class Agent:
    def __init__(self, role, goal, backstory):
        self.role = role
        self.goal = goal
        self.backstory = backstory

    def run(self, prompt):
        system_instruction = f"Role: {self.role}\nGoal: {self.goal}\nBackstory: {self.backstory}"
        return ollama_ask(prompt, system_instruction=system_instruction)

# Logistics Optimizer Agent
logistics_agent = Agent(
    role='Logistics Optimizer',
    goal='Identify and secure the most cost-effective and fastest shipping routes.',
    backstory='An expert in global logistics, dedicated to minimizing transit times and costs.'
)

# Demand Forecaster Agent
demand_agent = Agent(
    role='Demand Forecaster',
    goal='Predict future product demand accurately.',
    backstory='A data-driven analyst skilled in market trends and forecasting.'
)

# Inventory Manager Agent
inventory_agent = Agent(
    role='Inventory Manager',
    goal='Maintain optimal stock levels and reduce holding costs.',
    backstory='Experienced in inventory control and supply chain efficiency.'
)

# Risk Management Agent
risk_agent = Agent(
    role='Risk Management Specialist',
    goal='Identify potential supply chain disruptions and propose mitigation strategies.',
    backstory='A seasoned risk analyst with a focus on global supply chain vulnerabilities and crisis management.'
)
