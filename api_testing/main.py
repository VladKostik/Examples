from requests import get
from app import config


def get_beer(beer_id):
    return get(f"{config['host']}/beers/{beer_id}").json()


print(get_beer(3))
