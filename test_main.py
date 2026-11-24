import pytest
from fastapi.testclient import TestClient
from main import app, tasks

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_tasks():
    original_tasks = [task.copy() for task in tasks]

    tasks.clear()
    tasks.extend([
        {"id": 1, "title": "Learn Python", "done": False},
        {"id": 2, "title": "Build an API", "done": False},
        {"id": 3, "title": "Test my API", "done": True}
    ])

    yield

    tasks.clear()
    tasks.extend(original_tasks)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["name"] == "Task API"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_task():
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Learn Python"


def test_get_missing_task():
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Complete internship"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Complete internship"
    assert response.json()["done"] is False


def test_update_task():
    response = client.put(
        "/tasks/1",
        json={"title": "Learn FastAPI", "done": True}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Learn FastAPI"
    assert response.json()["done"] is True


def test_delete_task():
    response = client.delete("/tasks/2")
    assert response.status_code == 204


def test_delete_missing_task():
    response = client.delete("/tasks/999")
    assert response.status_code == 404