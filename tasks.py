
"""
tasks.py

Defines tasks for each agent in the Autonomous Supply Chain system.

Tasks:
    - optimize_route_task: For logistics_agent to propose efficient shipping routes.
    - forecast_demand_task: For demand_agent to forecast product demand.
    - manage_inventory_task: For inventory_agent to adjust inventory levels.
"""

from crewai import Task
from agents import logistics_agent, demand_agent, inventory_agent

# Task for Logistics Agent
optimize_route_task = Task(
    description='Analyze current shipping manifests and vendor relationships to propose new, efficient routes.',
    agent=logistics_agent
)

# Task for Demand Agent
forecast_demand_task = Task(
    description='Forecast product demand using historical sales and market data.',
    agent=demand_agent
)

# Task for Inventory Agent
manage_inventory_task = Task(
    description='Adjust inventory levels based on demand forecasts and supply constraints.',
    agent=inventory_agent
)
