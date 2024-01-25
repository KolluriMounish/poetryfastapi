# import pytest
# from models import Blog

# @pytest.fixture
# def blog_data():
from fastapi.testclient import TestClient
from .main import app
from models import Task

client = TestClient(app)


# def test_get_users():
#     response = client.get("/users")
#     assert response.status_code == 200
#     assert len(response.json()) > 0
# def test_get_users():
#     response = client.get("/user/")
#     assert response.status_code == 200
#     assert response.json() == [{"username": "Rick"}, {"paswword": "Morty"}]

async def test_create_user():
    response = client.post("/user/", json={"name": "Jessica", "email":"userxyz@gmail.com","password": "password"})
    assert response.status_code == 200
    assert response.json() == {"name": "Jessica","email":"userxyz@gmail.com","tasks":[]}

async def test_get_users_not_found():
    response = client.get("/user/999")  # assuming that 999 is not a valid user ID
    assert response.status_code == 404
# def test_create_task():
#     task_data = {"title": "Test Task", "description": "This is a test task.",
#                  "status": "pending", "due_date": "2024-01-25", "user_id": 1}
#     response = client.post("/task/", json=task_data)
#     assert response.status_code == 201
#     assert response.json() == {"title": "Test Task", "description": "This is a test task.",
#                                "status": "pending", "due_date": "2024-01-25", "user_id": 1, "id": 1}

#     task = Task.get(1)
#     assert task.title == "Test Task"
#     assert task.description == "This is a test task."
#     assert task.status == "pending"
#     assert task.due_date == "2024-01-25"
#     assert task.user_id == 1

# def test_get_task():
#     task = Task.get(1)
#     response = client.get(f"/task/{task.id}")
#     assert response.status_code == 200
#     assert response.json() == {"title": "Test Task", "description": "This is a test task.",
#                                "status": "pending", "due_date": "2024-01-25", "user_id": 1, "id": 1}

# def test_update_task():
#     task = Task.get(1)
#     updated_data = {"title": "Updated Test Task", "description": "This is an updated test task.",
#                     "status": "completed", "due_date": "2024-02-01", "user_id": 1}
#     response = client.put(f"/task/{task.id}", json=updated_data)
#     assert response.status_code == 200
#     assert response.json() == {"title": "Updated Test Task", "description": "This is an updated test task.",
#                                "status": "completed", "due_date": "2024-02-01", "user_id": 1, "id": 1}

#     task = Task.get(1)
#     assert task.title == "Updated Test Task"
#     assert task.description == "This is an updated test task."
#     assert task.status == "completed"
#     assert task.due_date == "2024-02-01"
#     assert task.user_id == 1

# def test_delete_task():
#     task = Task.get(1)
#     response = client.delete(f"/task/{task.id}")
#     assert response.status_code == 204

#     with pytest.raises(Task.DoesNotExist):
#         Task.get(1)