from api_testing.entities.beer import Beer


def test_check_beer_name_by_id(beer_service):
    response = beer_service.get_beer(1)
    assert response.json()[0]['name'] == 'Buzz'

def test_check_beer_data(beer_service, first_beer):
    response = beer_service.get_beer(1)

    actual_beer = Beer(
        response.json()[0]['id'],
        response.json()[0]['name'],
        response.json()[0]['tagline'],
        response.json()[0]['first_brewed'],
        response.json()[0]['abv'],
        response.json()[0]['ibu'],
        response.json()[0]['target_fg'],
        response.json()[0]['target_og'],
        response.json()[0]['ebc'],
        response.json()[0]['srm'],
        response.json()[0]['ph']
    )

    assert actual_beer == first_beer
