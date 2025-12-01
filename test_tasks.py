"""
Unit tests for task assignment in tasks.py
"""
import pytest
from tasks import optimize_route_task, forecast_demand_task, manage_inventory_task, risk_assessment_task
from agents import logistics_agent, demand_agent, inventory_agent, risk_agent

def test_optimize_route_task_agent():
    assert optimize_route_task.agent is logistics_agent

def test_forecast_demand_task_agent():
    assert forecast_demand_task.agent is demand_agent

def test_manage_inventory_task_agent():
    assert manage_inventory_task.agent is inventory_agent

def test_risk_assessment_task_agent():
    assert risk_assessment_task.agent is risk_agent
