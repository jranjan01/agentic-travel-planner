from google.adk.agents import SequentialAgent

from travel_agent.agents.validated_trip_planner import validated_trip_planner
from travel_agent.agents.travel_plan_generator import travel_plan_generator

travel_workflow = SequentialAgent(
    name="travel_workflow",
    description="Coordinates the end-to-end travel planning workflow.",
    sub_agents=[
        validated_trip_planner,
        travel_plan_generator,
    ],
)
