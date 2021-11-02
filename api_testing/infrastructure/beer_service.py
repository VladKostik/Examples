from requests import Response, get

from api_testing.app import config


class BeerService:
    def __init__(self):
        self.__beer_url = f"{config['host']}/beers"

    def get_beer(self, id: int) -> Response:
        return get(f"{self.__beer_url}/{id}")
