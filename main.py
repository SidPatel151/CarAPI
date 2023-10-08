from API.client import *
from typing import List, Union, Tuple, Dict
from API.classes import *

from API.makes import *



# client = CarAPIClient()
# makes_endpoint = '/trims?year=2020&verbose=yes'
# url = f'{client.base_url}{makes_endpoint}'
# response = client._make_request(url)
# print(response)


# Example usage:
car_api = CarAPIClient()

# Search for bodies
# bodies = car_api.search_bodies("Audi")
# for body in bodies:
#     print(body)

# Search for engines
# custom_error = "no hp given bro"
# engines = car_api.search_engines("Tesla", "Model X")
# for engine in engines:
#     # engine.set_horsepower_hp = custom_error
#     print(engine.engine_type, engine.horsepower_hp, engine.transmission, engine.fuel_type)


# Search for mileages
# mileages = car_api.search_mileages("Toyota", "Camry")
# for mileage in mileages:
#       print(f"fuel tank: {mileage.fuel_tank_capacity}, Combined: {mileage.combined_mpg}, Battery pack: {mileage.battery_capacity_electric}, Combined_epa: {mileage.epa_combined_mpg_electric}")

# Or, get a single mileage
# mileage = car_api.search_mileages(make="Toyota", model="Camry", direction="desc")[0]
# print(mileage) # -> You can print like mileage.epa_combined_mpg_electric and stuff


# # Search for trims
trims = car_api.search_trims(2020, "audi", "r8")
print(trims)
