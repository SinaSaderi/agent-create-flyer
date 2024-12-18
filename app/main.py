from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class NumberInput(BaseModel):
    number: int

@app.get("/factorial/{number}")
async def factorial(number: int):
    """
    Calculate the factorial of a given number.
    
    Args:
    - number (int): A non-negative integer whose factorial is to be calculated.
    
    Raises:
    - HTTPException: If the number is negative, raises a 400 status code error.
    
    Returns:
    - dict: A dictionary containing the original number and its factorial.
    """
    if number < 0:
        raise HTTPException(status_code=400, detail="Number must be non-negative.")
    return {"number": number, "factorial": calculate_factorial(number)}

def calculate_factorial(n: int) -> int:
    """
    Recursively calculates the factorial of a non-negative integer n.

    Args:
    - n (int): The non-negative integer to calculate the factorial of.

    Returns:
    - int: The factorial of n.
    """
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)
