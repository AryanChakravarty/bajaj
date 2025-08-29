#!/usr/bin/env python3
"""
Test script for the BFHL API
Tests the example case from the requirements
"""

import requests
import json
import time

def test_api():
    """Test the BFHL API with the example data"""
    
    # API endpoint
    url = "http://localhost:8000/bfhl"
    
    # Test data from requirements
    test_data = {
        "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
    }
    
    # Expected response based on requirements
    expected_response = {
        "is_success": True,
        "user_id": "aryan_chakravarty_17091999",  # Will vary based on current date
        "email": "aryan@xyz.com",
        "roll_number": "ABCD123",
        "odd_numbers": ["5"],
        "even_numbers": ["2", "4", "92"],
        "alphabets": ["A", "Y", "B"],
        "special_characters": ["&", "-", "*"],
        "sum": "103",
        "concat_string": "ByA"
    }
    
    print("🧪 Testing BFHL API...")
    print(f"📡 Endpoint: {url}")
    print(f"📤 Request data: {json.dumps(test_data, indent=2)}")
    print()
    
    try:
        # Send POST request
        response = requests.post(url, json=test_data)
        
        print(f"📥 Response Status: {response.status_code}")
        print(f"📥 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"📥 Response Body: {json.dumps(result, indent=2)}")
            print()
            
            # Validate response
            print("🔍 Validating response...")
            
            # Check required fields
            required_fields = [
                "is_success", "user_id", "email", "roll_number",
                "odd_numbers", "even_numbers", "alphabets", 
                "special_characters", "sum", "concat_string"
            ]
            
            for field in required_fields:
                if field in result:
                    print(f"✅ {field}: {result[field]}")
                else:
                    print(f"❌ Missing field: {field}")
            
            print()
            
            # Check specific values
            if result["is_success"] == True:
                print("✅ is_success: true")
            else:
                print("❌ is_success should be true")
            
            if result["email"] == "aryan@xyz.com":
                print("✅ email: john@xyz.com")
            else:
                print(f"❌ email should be 'aryan@xyz.com', got '{result['email']}'")
            
            if result["roll_number"] == "ABCD123":
                print("✅ roll_number: ABCD123")
            else:
                print(f"❌ roll_number should be 'ABCD123', got '{result['roll_number']}'")
            
            if result["odd_numbers"] == ["5"]:
                print("✅ odd_numbers: ['5']")
            else:
                print(f"❌ odd_numbers should be ['5'], got {result['odd_numbers']}")
            
            if result["even_numbers"] == ["2", "4", "92"]:
                print("✅ even_numbers: ['2', '4', '92']")
            else:
                print(f"❌ even_numbers should be ['2', '4', '92'], got {result['even_numbers']}")
            
            if result["alphabets"] == ["A", "Y", "B"]:
                print("✅ alphabets: ['A', 'Y', 'B']")
            else:
                print(f"❌ alphabets should be ['A', 'Y', 'B'], got {result['alphabets']}")
            
            if result["special_characters"] == ["&", "-", "*"]:
                print("✅ special_characters: ['&', '-', '*']")
            else:
                print(f"❌ special_characters should be ['&', '-', '*'], got {result['special_characters']}")
            
            if result["sum"] == "103":
                print("✅ sum: '103'")
            else:
                print(f"❌ sum should be '103', got '{result['sum']}'")
            
            if result["concat_string"] == "ByA":
                print("✅ concat_string: 'ByA'")
            else:
                print(f"❌ concat_string should be 'ByA', got '{result['concat_string']}'")
            
            # Check user_id format
            if "aryan_chakravarty_" in result["user_id"]:
                print("✅ user_id format: aryan_chakravarty_ddmmyyyy")
            else:
                print(f"❌ user_id should contain 'aryan_chakravarty_', got '{result['user_id']}'")
            
            print()
            print("🎉 API test completed!")
            
        else:
            print(f"❌ API request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure the API is running on http://localhost:8000")
        print("💡 Start the API with: python main.py")
    except Exception as e:
        print(f"❌ Test failed with error: {e}")

def test_health_endpoint():
    """Test the health endpoint"""
    print("\n🏥 Testing health endpoint...")
    
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("✅ Health endpoint working")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Health endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health test failed: {e}")

def test_root_endpoint():
    """Test the root endpoint"""
    print("\n🏠 Testing root endpoint...")
    
    try:
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            print("✅ Root endpoint working")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Root test failed: {e}")

if __name__ == "__main__":
    print("🚀 BFHL API Test Suite")
    print("=" * 50)
    
    # Wait a moment for API to be ready
    print("⏳ Waiting for API to be ready...")
    time.sleep(2)
    
    # Test main endpoint
    test_api()
    
    # Test other endpoints
    test_health_endpoint()
    test_root_endpoint()
    
    print("\n" + "=" * 50)
    print("🏁 Test suite completed!")
