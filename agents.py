
"""
agents.py

Defines specialized AI agents for the Autonomous Supply Chain system.

Agents:
    - logistics_agent: Optimizes shipping routes and vendor relationships.
    - demand_agent: Forecasts future product demand.
    - inventory_agent: Manages inventory levels and reduces costs.

Each agent is created using CrewAI's Agent class and is assigned a specific role, goal, and backstory.
"""

from crewai import Agent

# Logistics Optimizer Agent
logistics_agent = Agent(
    role='Logistics Optimizer',
    goal='Identify and secure the most cost-effective and fastest shipping routes.',
    backstory='An expert in global logistics, dedicated to minimizing transit times and costs.',
    verbose=True
)

# Demand Forecaster Agent
demand_agent = Agent(
    role='Demand Forecaster',
    goal='Predict future product demand accurately.',
    backstory='A data-driven analyst skilled in market trends and forecasting.',
    verbose=True
)

# Inventory Manager Agent
inventory_agent = Agent(
    role='Inventory Manager',
    goal='Maintain optimal stock levels and reduce holding costs.',
    backstory='Experienced in inventory control and supply chain efficiency.',
    verbose=True
)
