import requests


class httpStuff:
  def __init__(self):
    pass
  def make_request(self, url: str) -> dict:
      try:
          response = requests.get(url)
          response.raise_for_status()
          return response.json()
      except requests.exceptions.RequestException as e:
          raise Exception(f"Error making request: {e}")