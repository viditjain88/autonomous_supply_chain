"""
tasks.py

Defines tasks for each agent in the Autonomous Supply Chain system.

Tasks:
    - optimize_route_task: For logistics_agent to propose efficient shipping routes.
    - forecast_demand_task: For demand_agent to forecast product demand.
    - manage_inventory_task: For inventory_agent to adjust inventory levels.
"""

from agents import logistics_agent, demand_agent, inventory_agent, risk_agent


# Task for Logistics Agent
def optimize_route_task(cold_chain_logistics, distribution_partnerships):
    prompt = f"Analyze current shipping manifests and vendor relationships to propose new, efficient routes. Context: {cold_chain_logistics}, {distribution_partnerships}"
    return logistics_agent.run(prompt)


# Task for Demand Agent
def forecast_demand_task(population_data, infection_rates):
    prompt = f"Forecast product demand using historical sales and market data. Context: {population_data}, {infection_rates}"
    return demand_agent.run(prompt)


# Task for Inventory Agent
def manage_inventory_task(vaccine_availability):
    prompt = f"Adjust inventory levels based on demand forecasts and supply constraints. Context: {vaccine_availability}"
    return inventory_agent.run(prompt)


# Task for Risk Agent
def risk_assessment_task(infection_rates, cold_chain_logistics):
    prompt = f"Analyze potential risks in the supply chain based on infection rates and logistics capabilities. Context: {infection_rates}, {cold_chain_logistics}"
    return risk_agent.run(prompt)
