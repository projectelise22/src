# API Test Framework (Pytest)

This project is a simple but structured **API Test Automation Framework** built using **Python** and **Pytest**.  
It is designed to demonstrate **API testing fundamentals**, **pytest best practices**, and **clean test organization**.

---

## 📌 Tech Stack
- Python 3
- Pytest
- Requests
- JSONPlaceholder public API (https://jsonplaceholder.typicode.com)

---

## 📂 Project Structure
```bash
api_test_framework/
├── api
│ └── users_api.py # API client functions
├── config
│ └── config.py # Environment configuration
├── tests
│ ├── test_users_api.py # API test cases
│ └── conftest.py # Pytest fixtures
├── pytest.ini # Pytest configuration
├── requirements.txt # Project dependencies
└── README.md
```

---

## 🧪 What This Project Covers

### ✅ API Testing
- GET requests
- Status code validation
- Response header validation
- Response body validation
- Negative test cases (error handling)

### ✅ Pytest Features
- Fixtures for reusability
- Parametrized tests
- Markers (smoke, negative)
- Centralized configuration using `pytest.ini`

### ✅ QA Best Practices
- Separation of test logic and API calls
- Environment-based configuration
- Readable and maintainable test cases

---

## ⚙️ Setup Instructions

### 1️⃣ Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Running the Tests
Run all tests:
```bash
pytest
```

Run with verbose output:
```bash
pytest -v
```

Run specific markers(if added):
```bash
pytest -m smoke
pytest -m negative
```


## 🧩 Fixtures Used

Fixtures are defined in conftest.py and provide:
- Base URL configuration
- Reusable test setup
- Cleaner test functions

## 📌 Sample Test Case
```python
@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user_by_id(base_url, user_id):
    response = get_user_by_id(base_url, user_id)

    assert response.status_code == 200
    assert response.json()["id"] == user_id
```
