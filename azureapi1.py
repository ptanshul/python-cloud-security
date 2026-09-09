
import requests
import subprocess
from azure.identity import AzureCliCredential


credential = AzureCliCredential()


token = credential.get_token(
    "https://management.azure.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}"
}

subscription_id = subprocess.check_output(
    ["az", "account", "show", "--query", "id", "-o", "tsv"],
    text=True
).strip()

print(subscription_id)

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