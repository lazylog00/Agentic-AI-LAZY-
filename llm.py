from ollama import chat
import json
import ast

def decide_action(user_input: str):
    prompt = """
You are a strict JSON generator. The user may write in any language.
Always parse the math intent regardless of language.

Return a JSON list of actions (steps to execute in order).

Each step must have:
- action: multiply or add or subtract
- a: number
- b: number

If a second step depends on the first result, use the previous result as the value.

Example:
Input: multiply 5 and 4 then add 10
Output:
[
  {{"action": "multiply", "a": 5, "b": 4}},
  {{"action": "add", "a": 20, "b": 10}}
]

Return ONLY the JSON list. No explanation. No markdown.

Input: {user_input}
"""
    response = chat(
        model="llama3.2",
        messages=[{
            "role": "user",
            "content": prompt.format(user_input=user_input)
        }]
    )

    content = response["message"]["content"].strip()
    print("Raw LLM output:", content)

    # Strip markdown if LLM wraps in backticks
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()

    try:
        return json.loads(content)
    except:
        try:
            return ast.literal_eval(content)
        except:
            return []  # return empty list, not dict — consistent type