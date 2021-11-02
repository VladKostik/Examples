import pytest

from api_testing import Beer, BeerService


@pytest.fixture(scope="session")
def beer_service():
    yield BeerService()

@pytest.fixture
def first_beer():
    yield Beer(
        id=1,
        name='Buzz',
        tagline='A Real Bitter Experience.',
        first_brewed='09/2007',
        abv=4.5,
        ibu=60,
        target_fg=1010,
        target_og=1044,
        ebc=20,
        srm=10,
        ph=4.4
    )
