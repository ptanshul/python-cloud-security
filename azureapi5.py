import requests
from azure.identity import AzureCliCredential
from azure.mgmt.resource.subscriptions import SubscriptionClient

credential = AzureCliCredential()

client = SubscriptionClient(credential)

subscription_id = None

for subscription in client.subscriptions.list():
    if subscription.display_name == "Developer":
        subscription_id = subscription.subscription_id
        break

token = credential.get_token(
    "https://management.azure.com/.default"
)

headers = {
    "Authorization": f"Bearer {token.token}"
}

url = (
    f"https://management.azure.com/"
    f"subscriptions/{subscription_id}/resources"
    f"?api-version=2021-04-01"
)

response = requests.get(
    url,
    headers=headers
)

# print("Status:", response.status_code)

data = response.json()

# print(type(data))
for resource in data["value"]:
    print(resource["name"])
if data["kbs-agentpool"] == "kbs-agentpool":
    print("Found kbs-agentpool resource")
