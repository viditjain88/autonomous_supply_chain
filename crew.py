
"""
crew.py

Defines the crew that coordinates all agents and tasks for the Autonomous Supply Chain system.

The Crew class from CrewAI is used to group tasks and manage their execution order.
"""

from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task, risk_assessment_task


# Simple sequential runner for Gemini-based tasks
class SupplyChainCrew:
    def __init__(self):
        pass

    def run(self, context=None):
        # Example context, replace with real data as needed
        context = context or {
            'cold_chain_logistics': 'Cold storage available in 3 regions',
            'distribution_partnerships': 'Partnerships with 2 major distributors',
            'population_data': 'Population: 1M, Age distribution: 20% elderly',
            'infection_rates': 'Current infection rate: 2%',
            'vaccine_availability': '50,000 doses in stock'
        }
        results = {}
        results['demand_forecast'] = forecast_demand_task(context['population_data'], context['infection_rates'])
        results['inventory_management'] = manage_inventory_task(context['vaccine_availability'])
        results['route_optimization'] = optimize_route_task(context['cold_chain_logistics'], context['distribution_partnerships'])
        results['risk_assessment'] = risk_assessment_task(context['infection_rates'], context['cold_chain_logistics'])
        return results

supply_chain_crew = SupplyChainCrew()
