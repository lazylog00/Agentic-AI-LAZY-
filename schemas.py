'''
A schema in programming is a formal blueprint or structural definition that 
dictates how data is organized, stored, and related

It acts as a "contract" for data integrity, defining data types, table structures (in databases), 
or markup rules (in XML/JSON) to ensure applications can reliably create, read, and manipulate information.

'''






from pydantic import BaseModel
from typing import List 

class Response(BaseModel): 
  ans: str 
  steps: List[str]