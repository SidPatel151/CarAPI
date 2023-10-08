from .http import *
from .classes import *
from typing import List, Tuple, Union

class ModelAPI:
    def __init__(self):
        self.http = httpStuff()

    def get_models(self, page: int, limit: int, sort: str = "id", verbose: str = 'yes', direction: str= 'asc', year: int=2020) -> List[Model]:
        url = f"https://carapi.app/api/models?page={page}&limit={limit}&sort={sort}&direction={direction}&verbose={verbose}&year={year}"
        response_data = self.http.make_request(url)

        models = []
        
        for data in response_data['data']:
            model = Model(id=data["id"], make_id=data["make_id"], name=data["name"])
            models.append(model)

        return models

class ModelService:
    @staticmethod
    def get_models(page: int, limit: int, sort: str = "id", verbose: str = 'yes', direction: str= 'asc', year: int=2020) -> List[Model]:
      api = ModelAPI()
      models = api.get_models(page=page, limit=limit, sort=sort, verbose=verbose, direction=direction, year=year)
      return models

    @staticmethod
    def search_models(query: str) -> List[Tuple[Model, str]]:
      api = MakeService()
      models = ModelService.get_models(page=1, limit=100, sort="id", direction="asc", verbose="yes")
      models1 = ModelService.get_models(page=1, limit=100, sort="id", direction="desc", verbose="yes")
      all_makes = api.get_all_makes()
      make_id = None
      car_name = ""
      
      for make in all_makes:
        if query.lower() == make.name.lower():
          make_id, car_name = make.id, make.name


      combined = models + models1
      matched_models = [(model, car_name) for model in combined if model.make_id == make_id]
      return matched_models
          
        
      

#Ex usage
# makes = ModelService.get_models(page=1, limit=200, sort="id", direction="desc", year=2020)
# for make in makes:
#     print(make.id, make.make_id, make.name)

# query = 'Audi'
# models = ModelService.search_models(query)



# if len(models) > 0:
#     print(f"Models matching the query '{query}':")
#     for model, car_name in models:
#         print(f"Car Name: {car_name}")
#         print(f"Model: {model.name}")
# else:
#     print(f"No models found matching the query '{query}'.")