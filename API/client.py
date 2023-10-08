import requests

from .bodies import BodyService
from .engine import EngineService
from .mileage import MileageService
from .trims import TrimService
from .makes import MakeService
from .models import ModelService

class CarAPIClient:
    def __init__(self):
        self.body_service = BodyService()
        self.engine_service = EngineService()
        self.mileage_service = MileageService()
        self.trim_service = TrimService()
        self.make_service = MakeService()
        self.model_service = ModelService()


    # def _make_request(self, url):
    #     response = requests.get(url)
    #     response.raise_for_status()
    #     return response.json()


    # Wrapper methods for individual services, Im too lazy to add more
    def search_bodies(self, query: str, direction: str = 'asc'):
        return self.body_service.search_bodies(query, direction)

    def search_engines(self, make: str, model: str, direction: str = 'asc'):
        return self.engine_service.search_engines(make, model, direction)

    def search_mileages(self, make: str, model: str, direction: str = 'asc'):
        return self.mileage_service.search_mileages(make, model, direction)

    def search_trims(self, year: int, make: str, model: str, direction: str = 'asc'):
        return self.trim_service.search_trims(year, make, model, direction)
