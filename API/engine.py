from .classes import *
from typing import Dict, List
from .http import *

class EngineAPI:
    def __init__(self, *args, **kwargs):
        self.http = httpStuff()
        self.page = kwargs.get("page", 1)
        self.limit = kwargs.get("limit", 100)
        self.sort = kwargs.get("sort", "id")
        self.direction = kwargs.get("direction", "asc")
        self.make = kwargs.get("make", "")
        self.model = kwargs.get("model", "")
        self.verbose = kwargs.get('verbose', 'yes')
        self.data = self._get_data()

    def _get_data(self) -> Dict:
        url = f"https://carapi.app/api/engines?page={self.page}&limit={self.limit}&sort={self.sort}&direction={self.direction}&year=2020&make={self.make}&model={self.model}"
        response_data = self.http.make_request(url)
        return response_data

    @property
    def engines(self) -> List[Engine]:
        engines = []
        for data in self.data['data']:
            engine = Engine(data=data)
            engines.append(engine)
        return engines


class EngineService:
    @staticmethod
    def search_engines(make: str, model: str, direction: str = 'asc') -> List[Engine]:
        api = EngineAPI(page=1, limit=100, sort="id", direction=direction, year=2020, make=make, model=model)
        return api.engines


# Example usage
# make = "audi"
# model = "r8"
# engines = EngineService.search_engines(make, model)
# custom_error = "no hp given bro"
# custom = 'no fuel given'
# for engine in engines:
#     engine.set_horsepower_hp = custom_error
#     print(engine.engine_type, engine.horsepower_hp, engine.transmission, engine.fuel_type)
