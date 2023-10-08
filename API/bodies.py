from .classes import *
# from .client import CarAPIClient
from typing import List
from .http import *

class BodyAPI:
    def __init__(self, *args, **kwargs):
        # self.client = CarAPIClient()
        self.http =  httpStuff()
        self.page = kwargs.get("page", 1)
        self.limit = kwargs.get("limit", 100)
        self.sort = kwargs.get("sort", "id")
        self.direction = kwargs.get("direction", "asc")
        self.verbose = kwargs.get('verbose', 'yes')
        self.data = self._get_data()

    def _get_data(self) -> Dict:
        url = f"https://carapi.app/api/bodies?page={self.page}&limit={self.limit}&sort={self.sort}&direction={self.direction}&verbose={self.verbose}&year=2020"
        response_data = self.http.make_request(url)
        return response_data

    @property
    def bodies(self) -> List[Body]:
        bodies = []
        for data in self.data['data']:
            body = Body(data=data)
            bodies.append(body)
        return bodies

class BodyService:
    @staticmethod
    def search_bodies(query: str, direction: str = 'asc') -> List[Body]:
        api = BodyAPI(page=1, limit=100, sort="id", direction=direction, year=2020)
        bodies = api.bodies
        filtered = [body for body in bodies if query.lower() in body.name.lower()]
        if not filtered:
          return None
        return filtered

# Example usage
# query = "Volkswagen"
# bodies = BodyService.search_bodies(query, 'desc')
# for body in bodies:
#     print(f"ID: {body.id}, name:{body.name}, type:{body.type}, doors:{body.doors}, cargo:{body.cargo_capacity}")
