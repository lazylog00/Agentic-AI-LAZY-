
''' from ollama import chat
import json 
import ast 
def decide_action(user_input: str): 

  prompt = f""" You are an intelligent agent. 

  Extract: 
  - action(multiply or add)
  - a (first number)
  - b (second number)  
   
  Map meanings: 
  - multiply -> multi, times, multiplica, product, producto
  - add -> add, plus, combine, sum, suma, agregar, 


  Return ONLY valid JSON( no explanation ) like:
  {
    {"action": "multiply", 
     "a": 5, 
     "b": 4}
     }
   
  Input: {user_input}
  """

  response = chat(
  model = 'llama3.2:latest',
  messages = [{"role": "user", 
               "content": prompt}]

)
  content = response['message']['content']
  print("Raw llms ouput: ", content)

  try: 
    return json.loads(content)
  except: 
    try: 
      return ast.literal_eval(content)
    except:
      return { "action": "unknown"}

      '''


from ollama import chat
import json 
import ast

def decide_action(user_input: str):
 prompt = """ 

You are a strict JSON generator: 

Break the task into steps: 

Return a json list of actions: 

Each step must have: 
- action: mulitply or add
- a: number
- b: number

If second step depends on first result, 
use previous result

Example: 
Input: multiply 5 and 4 then add 10 

Ouput: 
[
{{"action": "multiply", "a": 5, "b": 4}}, 
{{"action": "add", "a": 20, "b": 10}}
]

Return only JSON 
No explanation: 

Input: {user_input}
"""

response = chat(
 model = 'llama3.2', 
 messages = [{
  "role": "user", 
  "content": "prompt"

 } ]
)

content = response["messages"]["content"]
print("Raw LLMs output: ", content)

try: 
 return json.loads(content)
except: 
 try: 
  return ast.literal_eval(content)
 except: 
  return ("action": "unknown")