from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
import re
from datetime import datetime

app = FastAPI(title="BFHL API", description="REST API for processing data arrays")

class DataRequest(BaseModel):
    data: List[str] = Field(..., example=["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"])

class DataResponse(BaseModel):
    is_success: bool = Field(..., example=True)
    user_id: str = Field(..., example="aryan_chakravarty_14092004")
    email: str = Field(..., example="aryan.chakravarty2022@vitstudent.ac.in")
    roll_number: str = Field(..., example="22BCE0590")
    odd_numbers: List[str] = Field(..., example=["5"])
    even_numbers: List[str] = Field(..., example=["2", "4", "92"])
    alphabets: List[str] = Field(..., example=["A", "Y", "B"])
    special_characters: List[str] = Field(..., example=["&", "-", "*"])
    sum: str = Field(..., example="103")
    concat_string: str = Field(..., example="ByA")

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
    if not alphabets:
        return ""
    
    # Concatenate all alphabets in order of appearance
    concat_str = "".join(alphabets)
    
    # Reverse the string
    reversed_str = concat_str[::-1]
    
    # Apply alternating case (first letter uppercase, second lowercase, etc.)
    result = ""
    for i, char in enumerate(reversed_str):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    
    return result

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "BFHL API is running! Use POST /bfhl to process data."}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/bfhl", response_model=DataResponse)
async def process_data(request: DataRequest):
    """
    Process the input data array and return categorized results.
    
    - **data**: Array of strings to process
    - **Returns**: Categorized data with various metrics
    """
    try:
        data = request.data
        
        # Initialize result variables
        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        numeric_sum = 0
        
        # Process each item in the data array
        for item in data:
            if is_number(item):
                num = float(item)
                if num.is_integer():
                    num = int(num)
                    if num % 2 == 0:
                        even_numbers.append(str(num))
                    else:
                        odd_numbers.append(str(num))
                    numeric_sum += num
            elif is_alphabetic(item):
                alphabets.append(item.upper())
            else:
                special_characters.append(item)
        
        # Fixed identity details as requested
        user_id = "aryan_chakravarty_14092004"
        fixed_email = "aryan.chakravarty2022@vitstudent.ac.in"
        fixed_roll = "22BCE0590"
        
        # Create alternating case string
        concat_string = create_alternating_case_string(alphabets)
        
        # Return the response
        return DataResponse(
            is_success=True,
            user_id=user_id,
            email=fixed_email,
            roll_number=fixed_roll,
            odd_numbers=odd_numbers,
            even_numbers=even_numbers,
            alphabets=alphabets,
            special_characters=special_characters,
            sum=str(int(numeric_sum)),
            concat_string=concat_string
        )
        
    except Exception as e:
        # Return error response
        return DataResponse(
            is_success=False,
            user_id="",
            email="",
            roll_number="",
            odd_numbers=[],
            even_numbers=[],
            alphabets=[],
            special_characters=[],
            sum="0",
            concat_string=""
        )

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting BFHL API server...")
    print("📡 Server will be available at: http://localhost:8000")
    print("📚 API documentation: http://localhost:8000/docs")
    print("🏥 Health check: http://localhost:8000/health")
    uvicorn.run(app, host="0.0.0.0", port=8000)
