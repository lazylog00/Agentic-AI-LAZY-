from agent import agent_logic

queries = [
    "multiply 9 and 3",
    "producto de 9 y 3",           # Spanish
    "multiply 5 and 4 then add 10", # multi-step
    "add 100 and 200 then multiply by 3",
]

for query in queries:
    print(f"\n{'='*50}")
    print(f"Query: {query}")
    response = agent_logic(query)
    print(f"Answer: {response.ans}")
    print(f"Steps:  {response.steps}")