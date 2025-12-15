from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent

TEST_CASE = """
Launch Obsidian
Create note
Enter text
Verify persistence
"""

planner = PlannerAgent()
executor = ExecutorAgent()

plan = planner.create_plan(TEST_CASE)

print("Generated Plan:", plan)
executor.execute(plan)
