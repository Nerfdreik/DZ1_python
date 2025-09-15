import requests
from config import BASE_URL, HEADERS


class YougileAPI:
    """Класс для работы с API Yougile"""
    
    def __init__(self, base_url=BASE_URL, headers=HEADERS):
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
