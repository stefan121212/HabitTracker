import requests
from datetime import datetime

USERNAME = "stefan1212"
TOKEN = "asdalskdnalsdna"
pixela_endpoint = "https://pixe.la/v1/users"
MY_GRAPH = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_enpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "My coding graph",
    "unit": "Minutes",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.now()
formated_today = today.strftime("%Y%m%d")

pixel_data = {
    "date": formated_today,
    "quantity": input("How many minutes did you studied today?: ")
}

response = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/{MY_GRAPH}", json=pixel_data, headers=headers)
print(response.text)


# pixel_update_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{MY_GRAPH}/{formated_today}"
#
# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{MY_GRAPH}/{formated_today}"
#
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)