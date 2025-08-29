from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import re
from datetime import datetime

app = FastAPI(title="BFHL API", description="REST API for processing data arrays")

class DataRequest(BaseModel):
    data: List[str]

    class Config:
        schema_extra = {
            "example": {
                "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
            }
        }

class DataResponse(BaseModel):
    is_success: bool
    user_id: str
    email: str
    roll_number: str
    odd_numbers: List[str]
    even_numbers: List[str]
    alphabets: List[str]
    special_characters: List[str]
    sum: str
    concat_string: str

    class Config:
        schema_extra = {
            "example": {
                "is_success": True,
                "user_id": "aryan_chakravarty_17091999",
                "email": "aryan@xyz.com",
                "roll_number": "ABCD123",
                "odd_numbers": ["5"],
                "even_numbers": ["2", "4", "92"],
                "alphabets": ["A", "Y", "B"],
                "special_characters": ["&", "-", "*"],
                "sum": "103",
                "concat_string": "ByA"
            }
        }

def is_number(s: str) -> bool:
    """Check if a string represents a valid number"""
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_alphabetic(s: str) -> bool:
    """Check if a string contains only alphabetic characters"""
    return s.isalpha()

def is_special_character(s: str) -> bool:
    """Check if a string is neither purely numeric nor purely alphabetic"""
    return not is_number(s) and not is_alphabetic(s)

def create_alternating_case_string(alphabets: List[str]) -> str:
    """Create alternating case string from alphabetic characters"""
    # Concatenate all alphabetic values in order of appearance
    concat = ''.join(alphabets)
    # Reverse the string
    reversed_str = concat[::-1]
    # Make it alternating caps, starting with uppercase
    result = ""
    for i, char in enumerate(reversed_str):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

@app.post("/bfhl", response_model=DataResponse)
async def process_data(request: DataRequest):
    try:
        data = request.data
        
        # Separate numbers, alphabets, and special characters
        numbers = []
        alphabets = []
        special_chars = []
        
        for item in data:
            if is_number(item):
                numbers.append(item)
            elif is_alphabetic(item):
                alphabets.append(item.upper())
            else:
                special_chars.append(item)
        
        # Separate even and odd numbers
        even_numbers = []
        odd_numbers = []
        total_sum = 0
        
        for num_str in numbers:
            try:
                num = int(float(num_str))
                if num % 2 == 0:
                    even_numbers.append(num_str)
                else:
                    odd_numbers.append(num_str)
                total_sum += num
            except ValueError:
                # Handle cases where conversion to int fails
                continue
        
        # Create user_id with current date
        current_date = datetime.now().strftime("%d%m%Y")
        user_id = f"aryan_chakravarty_{current_date}"
        
        # Create alternating case string
        concat_string = create_alternating_case_string(alphabets)
        
        response = DataResponse(
            is_success=True,
            user_id=user_id,
            email="aryan@xyz.com",
            roll_number="ABCD123",
            odd_numbers=odd_numbers,
            even_numbers=even_numbers,
            alphabets=alphabets,
            special_characters=special_chars,
            sum=str(total_sum),
            concat_string=concat_string
        )
        
        return response
        
    except Exception as e:
        # Return error response if parsing fails
        return DataResponse(
            is_success=False,
            user_id="",
            email="",
            roll_number="",
            odd_numbers=[],
            even_numbers=[],
            alphabets=[],
            special_characters=[],
            sum="",
            concat_string=""
        )

@app.get("/")
async def root():
    return {"message": "BFHL API is running. Use POST /bfhl to process data."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
