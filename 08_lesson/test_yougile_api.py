import pytest
from yougile_api import YougileAPI


@pytest.fixture
def api_client():
    return YougileAPI()


@pytest.fixture
def temp_project(api_client):
    project_data = {
        "title": "Test Project for API Testing",
        "description": "This is a test project created for API testing"
    }
    response = api_client.create_project(project_data)
    assert response.status_code == 201
    project_id = response.json().get("id")

    yield project_id



def test_create_project_positive(api_client):
    """Позитивный тест создания проекта"""
    project_data = {
        "title": "New Test Project",
        "description": "Test project description"
    }

    response = api_client.create_project(project_data)

    assert response.status_code == 201, f"Ожидался статус 201, но получен {response.status_code}. Тело ответа: {response.text}"

    response_json = response.json()
    assert "id" in response_json, "В ответе отсутствует ID проекта"
    assert response_json["title"] == project_data["title"], f"Ожидалось title: {project_data['title']}, но получено: {response_json['title']}"
    assert response_json["description"] == project_data["description"], f"Ожидалось description: {project_data['description']}, но получено: {response_json['description']}"


def test_get_project_positive(api_client, temp_project):
    """Позитивный тест получения проекта"""
    response = api_client.get_project(temp_project)

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}. Тело ответа: {response.text}"

    response_json = response.json()
    assert response_json["id"] == temp_project, f"Ожидался ID проекта: {temp_project}, но получен: {response_json['id']}"
    assert "title" in response_json, "В ответе отсутствует поле title"
    assert "description" in response_json, "В ответе отсутствует поле description"


def test_update_project_positive(api_client, temp_project):
    """Позитивный тест обновления проекта"""
    update_data = {
        "title": "Updated Test Project",
        "description": "Updated test project description"
    }

    response = api_client.update_project(temp_project, update_data)

    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}. Тело ответа: {response.text}"

    response_json = response.json()
    assert response_json["title"] == update_data["title"], f"Ожидалось title: {update_data['title']}, но получено: {response_json['title']}"
    assert response_json["description"] == update_data["description"], f"Ожидалось description: {update_data['description']}, но получено: {response_json['description']}"


def test_create_project_negative(api_client):
    """Негативный тест создания проекта (без обязательного поля title)"""
    project_data = {
        "description": "Test project without title"
    }

    response = api_client.create_project(project_data)

    assert response.status_code != 201, f"Ожидалась ошибка, но получен статус 201. Тело ответа: {response.text}"

    if response.status_code != 201:
        response_json = response.json()
        assert "error" in response_json or "message" in response_json, "Ожидалось сообщение об ошибке в ответе"


def test_get_project_negative(api_client):
    """Негативный тест получения проекта (несуществующий ID)"""
    non_existent_id = "non-existent-id-12345"

    response = api_client.get_project(non_existent_id)

    assert response.status_code != 200, f"Ожидалась ошибка, но получен статус 200. Тело ответа: {response.text}"

    if response.status_code != 200:
        response_json = response.json()
        assert "error" in response_json or "message" in response_json, "Ожидалось сообщение об ошибке в ответе"


def test_update_project_negative(api_client):
    """Негативный тест обновления проекта (несуществующий ID)"""
    non_existent_id = "non-existent-id-12345"
    update_data = {
        "title": "Updated Test Project",
        "description": "Updated test project description"
    }

    response = api_client.update_project(non_existent_id, update_data)

    assert response.status_code != 200, f"Ожидалась ошибка, но получен статус 200. Тело ответа: {response.text}"

    if response.status_code != 200:
        response_json = response.json()
        assert "error" in response_json or "message" in response_json, "Ожидалось сообщение об ошибке в ответе"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
