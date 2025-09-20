"""
Unit tests for crew coordination in crew.py
"""
import pytest
from crew import supply_chain_crew
from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task

def test_crew_tasks_order():
    tasks = supply_chain_crew.tasks
    assert tasks[0] is forecast_demand_task
    assert tasks[1] is manage_inventory_task
    assert tasks[2] is optimize_route_task

def test_crew_process_sequential():
    assert supply_chain_crew.process.name == 'sequential'
