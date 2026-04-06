from tools import TOOL_REGISTRY
from schemas import Response
from llm import decide_action


def agent_logic(user_input: str) -> Response:
    steps_log = []
    intermediate_results = []

    # Step 1: Ask LLM to plan the actions
    decisions = decide_action(user_input)

    if not decisions:
        return Response(
            ans="I couldn't understand that.",
            steps=["LLM returned no actions"]
        )

    last_result = None

    # Step 2: Execute each action in order
    for i, decision in enumerate(decisions):
        action = decision.get("action")
        a = decision.get("a")
        b = decision.get("b")

        # Validation
        if action not in TOOL_REGISTRY:
            return Response(
                ans=f"Unknown action: {action}",
                steps=steps_log + [f"Step {i+1}: invalid action '{action}'"]
            )

        if a is None or b is None:
            return Response(
                ans="Missing numbers.",
                steps=steps_log + [f"Step {i+1}: LLM failed to extract a or b"]
            )

        # Execute the tool
        tool = TOOL_REGISTRY[action]
        result = tool(a, b)
        last_result = result

        steps_log.append(f"Step {i+1}: {action}({a}, {b}) = {result}")
        intermediate_results.append(result)

    return Response(
        ans=str(last_result),
        steps=steps_log,
        intermediate_results=intermediate_results
    )