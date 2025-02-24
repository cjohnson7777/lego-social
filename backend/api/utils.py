import requests


def get_data_from_rebrick(id):
    url = f"https://rebrickable.com/api/v3/lego/sets/{id}"
    headers = {"Authorization": "key 012535ebae0227cee00bc3205c83f64c"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None
