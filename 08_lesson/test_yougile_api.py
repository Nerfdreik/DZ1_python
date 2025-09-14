import pytest
import requests

BASE_URL = "https://yougile.com/api-v2"

API_TOKEN = "123"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}


class YougileAPI:
    """Класс для работы с API Yougile (подобие Page Object для API)"""

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def create_project(self, data):
        """Создание проекта [POST] /api-v2/projects"""
        response = requests.post(
            f"{self.base_url}/projects",
            json=data,
            headers=self.headers
        )
        return response

    def update_project(self, project_id, data):
        """Обновление проекта [PUT] /api-v2/projects/{id}"""
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            json=data,
            headers=self.headers
        )
        return response

    def get_project(self, project_id):
        """Получение проекта [GET] /api-v2/projects/{id}"""
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response


@pytest.fixture
def api_client():
    return YougileAPI(BASE_URL, HEADERS)


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

    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["title"] == project_data["title"]
    assert response.json()["description"] == project_data["description"]


def test_get_project_positive(api_client, temp_project):
    """Позитивный тест получения проекта"""
    response = api_client.get_project(temp_project)

    assert response.status_code == 200
    assert response.json()["id"] == temp_project
    assert "title" in response.json()
    assert "description" in response.json()


def test_update_project_positive(api_client, temp_project):
    """Позитивный тест обновления проекта"""
    update_data = {
        "title": "Updated Test Project",
        "description": "Updated test project description"
    }

    response = api_client.update_project(temp_project, update_data)

    assert response.status_code == 200
    assert response.json()["title"] == update_data["title"]
    assert response.json()["description"] == update_data["description"]


def test_create_project_negative(api_client):
    """Негативный тест создания проекта (без обязательного поля title)"""
    project_data = {
        "description": "Test project without title"
    }

    response = api_client.create_project(project_data)

    assert response.status_code != 201


def test_get_project_negative(api_client):
    """Негативный тест получения проекта (несуществующий ID)"""
    non_existent_id = "non-existent-id-12345"

    response = api_client.get_project(non_existent_id)

    assert response.status_code != 200


def test_update_project_negative(api_client):
    """Негативный тест обновления проекта (несуществующий ID)"""
    non_existent_id = "non-existent-id-12345"
    update_data = {
        "title": "Updated Test Project",
        "description": "Updated test project description"
    }

    response = api_client.update_project(non_existent_id, update_data)

    assert response.status_code != 200


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
