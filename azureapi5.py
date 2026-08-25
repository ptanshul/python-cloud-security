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

print("Subscription:", subscription_id)
