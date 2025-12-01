
"""
crew.py

Defines the crew that coordinates all agents and tasks for the Autonomous Supply Chain system.

The Crew class from CrewAI is used to group tasks and manage their execution order.
"""

from crewai import Crew, Process
from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task, risk_assessment_task

# Crew coordinates all tasks in a sequential process
supply_chain_crew = Crew(
    tasks=[forecast_demand_task, manage_inventory_task, optimize_route_task, risk_assessment_task],
    process=Process.sequential,
    verbose=True
)
