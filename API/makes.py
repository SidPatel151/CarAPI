from .classes import *
from typing import Union, List
from .client import *
class Pagination:
    def __init__(self, limit: int, page: int):
        self.limit = limit
        self.page = page

    def validate(self):
        if self.limit <= 0:
            raise ValueError("Limit must be a positive integer.")
        if self.page <= 0:
            raise ValueError("Page must be a positive integer.")

class MakeAPI:
    def __init__(self):
        self.client = CarAPIClient()

    def get_makes(self, page: int, limit: int, sort: str, direction: str, year: Union[int, str]) -> List[Make]:
        pagination = Pagination(limit, page)
        pagination.validate()

        url = f"https://carapi.app/api/makes?page={page}&limit={limit}&sort={sort}&direction={direction}&year={year}"
        response_data = self.client._make_request(url)
     

        makes = []
        for make_data in response_data['data']:
            make = Make(id=make_data["id"], name=make_data["name"])
            makes.append(make)

        return makes


class MakeService:
    @staticmethod
    def get_makes(page: int, limit: int, sort: str, direction: str, year: Union[int, str]) -> List[Make]:
        api = MakeAPI()
        pagination = Pagination(limit=limit, page=page)
        pagination.validate()
        makes = api.get_makes(page=pagination.page, limit=pagination.limit, sort=sort, direction=direction, year=year)
        return makes

    @staticmethod
    def get_all_makes() -> List[Make]:
      direction = ['asc', 'desc']
      for i in direction:
        makes = MakeService.get_makes(page=1, limit=100, sort='id', direction=i, year=2020)
        
      return makes

  
    @staticmethod
    def search_make(query:str, direction: str='asc') -> List[Make]:
      all_makes = MakeService.get_makes(page=1, limit=100, sort="id", direction=direction, year=2020)
      filtered_makes = [make for make in all_makes if query.lower() in make.name.lower()]
      return filtered_makes

    @staticmethod
    def search_make_id(id: int, direction='asc') -> List[Make]:
        all_makes = MakeService.get_makes(page=1, limit=100, sort="id", direction=direction, year=2020)
        filtered = [make for make in all_makes if id == make.id]
        if filtered == []:
          return None
        return filtered

#Example usage 
# makes = MakeService.get_makes(page=1, limit=100, sort="id", direction="desc", year=2022)
# for make in makes:
#     print(make.id, make.name)

# query = 'Subaru'

# id = 300
# makes = MakeService.search_make(query)
# for make in makes:
#   print(make.id, make.name)

# makess = MakeService.search_make_id(id, direction='desc')
# for make in makess:
#   print(make.name, make.id)