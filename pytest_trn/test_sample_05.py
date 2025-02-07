import pytest
import requests

# Write a pytest for a given function
def add2Numbers(num1:int, num2:int) -> int:
    """Function that adds 2 numbers"""
    return num1 + num2

def test_add2Numbers():
    test_1 = [add2Numbers(1, 2), 3]
    test_2 = [add2Numbers(-4, 2), -2.0]
    assert test_1[0] == test_1[1], "Wrong answer"
    assert test_2[0] == test_2[1], "Wrong answer"

# Parametarized test
@pytest.mark.parametrize("num1, num2, output", [[1,2,3], [3,-10,-7]])
def test_add2Numbers_param(num1, num2, output):
    assert add2Numbers(num1,num2) == output, "Wrong response"

# Validate an API response
@pytest.fixture
def mockAPI() -> dict:
    return { "status": "success",
             "data": { "id": 123,
                       "name": "test user",
                       "e-mail": "test@example.com"
                }
            }

def test_mockAPI(mockAPI):
    assert mockAPI["status"] == "success", "Wrong response"
    assert type(mockAPI["data"]["id"]) == int, "Wrong response"
    assert isinstance(mockAPI["data"]["id"],int), "Wrong response"
    assert "@" in mockAPI["data"]["e-mail"], "Wrong response"

# Mock an API call
def fetch_data(url):
    response = requests.get(url)
    return response

def getfakeAPIResponse(url):
    response = requests.get(url)
    return response.json()

def test_fakeAPI():
    response = getfakeAPIResponse("https://jsonplaceholder.typicode.com/users")
    response = response[0]

    assert isinstance(response, dict)
    assert "name" in response, "No name key in response result"

# Python Scripting Challenge
# Open two files at a time:
file1 = "./dir1/file1.txt"
file2 = "./dir2/file1.txt"
result = "result.txt"
with open(file1, "r") as a, open(file2, "r") as b, open(result, "w") as c:
    a_line = a.readlines()
    b_line = b.readlines()
    for i in range(min(len(a_line), len(b_line))):
        if a_line[i] != b_line[i]: 
            c.write(f"Line {i+1}: Content in dir1: {a_line[i].strip()}, Content in dir2: {b_line[i].strip()}")
        else:
            continue
            