
import requests
from azure.identity import AzureCliCredential

credential = AzureCliCredential()

token = credential.get_token(
    "https://management.azure.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}"
}

subscription_id = "76f62c75-865d-4b5e-99e9-f512832303ba"

url = (
    f"https://management.azure.com/"
    f"subscriptions/{subscription_id}/resources"
    f"?api-version=2021-04-01"
)

response = requests.get(url, headers=headers)

print(response.status_code)

data = response.json()
for resource in data["value"]:
    print(resource["name"])