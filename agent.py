# from tools import multiply, add
# from schemas import Response
# import re


# # Now writing the function ( defining a unit of behaviour)
# def agent_logic(user_input: str) -> Response:

#   # adding a logic
#   if 'multiply' in user_input or '*' in user_input:
#     numbers = list(map(int, re.findall(r'\d+', user_input))) # find digits, map to int, 
#     # eg: ['25', '40'], map to int, i.e 25, 40
#     print("Hello, Multiplying with these numbers: ")
#     print(numbers)

#     if len(numbers) >= 2:
#       result = multiply(numbers[0], numbers[1])
#       return Response(ans = str(result), 
#                     steps = ['Detected multiplication request', 'Used Multiply tool' ])
    
#     else: 
#       return Response(
#         ans = 'Coulnot find enough numbers: ',
#         steps = ['Failed to extract numbers']
#       )
#   elif 'add' in user_input or '+' in user_input: 
#     numbers = list(map(int, re.findall(r'\d+', user_input)))
    
#     # print the ouput for validation: 
#     print(f"Here are the numbers for doing addition: {numbers}")
#     if len(numbers) >=2:
#       result = add(numbers[0], numbers[1])
#       return Response(
#         ans = str(result),
#         steps = ['Detection addition request', 'Used Add tool']
      
#       )
#     else:
#       return Response(ans = 'Couldnot find enough numbers:',
#                       steps = ['Failed to extract numbers'])
    
#     # global fallback
#   return Response(
#     ans = 'I dont understand',
#     steps = ['No valid operation detected']
#     )
    
'''
# Day 1: 
from tools import multiply , add 
from schemas import Response
import re

def extract_numbers(user_input: str):
  return list(map(int, re.findall(r'\d+', user_input)))

def agent_logic(user_input: str) -> Response: 
  numbers = extract_numbers(user_input)

  # Handle insufficinet numbers early:
  if len(numbers) <2:
    return Response(ans = 'Could not find enough numbers', steps = ['Failed to extract numbers'])
  
  # Multiplication: 
  if 'multiply' in user_input or '*' in user_input:
    result = multiply(numbers[0], numbers[1])
    return Response(
      ans = str(result),
      steps = ['Detected Multiplication request', 'Used multiply tool']
    )
  
  # Addition: 
  elif 'add' in user_input or '+' in user_input: 
    result = add(numbers[0], numbers[1])
    return Response(
      ans = str(result), 
      steps = ['Detected Addition request: ', 'Used add tool']
    )
  
  # Global fallback
  return Response(
    answer = 'I donot understand your input',
    steps = ['No valid operation detected']
  )



  # Day 2: 



from tools import multiply , add 
from schemas import Response 
from llm  import decide_action



def agent_logic(user_input: str) -> Response: 
  decision = decide_action(user_input)
  action = decision.get("action")
  a = decision.get("a")
  b = decision.get("b")

  # validation: 
  if action not in ['multiply', 'add']:
    return Response(
      ans= "I don't understand ", 
      steps = ["Invalid action from LLM"]
    )
  
  if a is None or b is None: 
    return Response(
      ans = "Missing numbers: ", 
      steps = ["LLM failed to extract numbers: "]

    )
  
  # execution 
  if action == "multiply":
    result = multiply(a, b)

  elif action == "add": 
    result = add(a, b)

  return Response(
    ans = str(result), steps = [f"LLM choose {action}", "Executed tool"] 
  )

  '''

