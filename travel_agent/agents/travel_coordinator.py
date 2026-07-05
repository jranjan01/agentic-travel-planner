from google.adk.agents import LlmAgent

from travel_agent.agents.validated_trip_planner import validated_trip_planner
from travel_agent.agents.travel_plan_generator import travel_plan_generator
from travel_agent.config import GEMINI_MODEL


travel_coordinator = LlmAgent(
    name="travel_coordinator",
    model=GEMINI_MODEL,
    description="Coordinates the end-to-end travel planning workflow by delegating tasks to specialized travel agents.",
    instruction="""
You are an AI Travel Coordinator.

Your ONLY responsibility is to coordinate the travel planning workflow.

If the user's request is related to travel planning:

- Delegate planning to 'validated_trip_planner'.
- Wait for planning to complete successfully.
- Delegate travel guide generation to 'travel_plan_generator'.
- Return only the final travel plan.

Guidelines:
- Never generate the travel plan yourself.
- Never modify the generated travel plan.
- Do not expose intermediate outputs.
""",
    sub_agents=[
        validated_trip_planner,
        travel_plan_generator,
    ],
)
