from .classes import *
from typing import Dict, List
from .http import * 


class MileageAPI:
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
        url = f"https://carapi.app/api/mileages?page={self.page}&limit={self.limit}&sort={self.sort}&direction={self.direction}&year=2020&make={self.make}&model={self.model}"
        response_data = self.http.make_request(url)
        return response_data

    @property
    def mileages(self) -> List[Mileage]:
        mileages = []
        for data in self.data['data']:
            mileage = Mileage(data=data)
            mileages.append(mileage)
        return mileages


class MileageService:
    @staticmethod
    def search_mileages(make: str, model: str, direction: str = 'asc') -> List[Mileage]:
        api = MileageAPI(page=1, limit=100, sort="id", direction=direction, year=2020, make=make, model=model)
        return api.mileages

# Example usage:
# mileages = MileageService.search_mileages(make="Tesla", model="Model X")
# for mileage in mileages:
#     print(f"fuel tank: {mileage.fuel_tank_capacity}, Combined: {mileage.combined_mpg}, Battery pack: {mileage.battery_capacity_electric}, Combined_epa: {mileage.epa_combined_mpg_electric}")

# Or, get a single mileage
# mileage = MileageService.search_mileages(make="Toyota", model="Camry", direction="desc")[0]
# print(mileage) # -> You can print like mileage.epa_combined_mpg_electric and stuff