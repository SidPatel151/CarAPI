from .classes import *
from .http import *
from typing import Dict, List, Union



class TrimAPI:
    def __init__(self, *args, **kwargs):
        self.http = httpStuff()
        self.page = kwargs.get("page", 1)
        self.limit = kwargs.get("limit", 100)
        self.sort = kwargs.get("sort", "id")
        self.direction = kwargs.get("direction", "asc")
        self.year = kwargs.get("year", 2020)
        self.make = kwargs.get("make", "")
        self.model = kwargs.get("model", "")
        self.verbose = kwargs.get('verbose', 'yes')
        self.data = self._get_data()

    def _get_data(self) -> Dict:
        url = f"https://carapi.app/api/trims?page={self.page}&limit={self.limit}&sort={self.sort}&direction={self.direction}&year={self.year}&make={self.make}&model={self.model}"
        response_data = self.http.make_request(url)
        return response_data

    @property
    def trims(self) -> List[Trim]:
        trims = []
        for data in self.data['data']:
            trim = Trim(data=data)
            trims.append(trim)
        return trims

class TrimService:
    @staticmethod
    def search_trims(year: int, make: str, model: str, direction: str = 'asc') -> List[Trim]:
        api = TrimAPI(page=1, limit=100, sort="id", direction=direction, year=year, make=make, model=model)
        return api.trims

    @staticmethod
    def get_max_msrp_trim(trims: List[Trim]) -> Trim:
        max_msrp_trim = max(trims, key=lambda trim: trim.msrp)
        return max_msrp_trim

# Example usage:
year = 2020
make = "Toyota"
model = "Camry"

trims = TrimService.search_trims(year, make, model)
max_msrp_trim = TrimService.get_max_msrp_trim(trims)
print(f"Name: {max_msrp_trim.name}, Description: {max_msrp_trim.description}, MSRP: {max_msrp_trim.msrp}")