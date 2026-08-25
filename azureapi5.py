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
rfound = False
# print(type(data))
for resource in data["value"]:
    print(resource["name"])
    if resource["name"] == "vm-aks-nsg":
        rfound = True
        print("Resource found:", resource["name"])
        print("Resource ID:", resource["id"])
        print("Resource Type:", resource["type"])
        print("Resource Location:", resource["location"])
        break
for resource in data["value"]:
    if resource["type"] == "Microsoft.Network/networkSecurityGroups":
        
        print("NSG Resource found:", resource["name"])
        

