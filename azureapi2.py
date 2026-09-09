from azure.identity import AzureCliCredential
from azure.mgmt.resource.subscriptions import SubscriptionClient

credential = AzureCliCredential()

client = SubscriptionClient(credential)

for subscription in client.subscriptions.list():
    print("Subscription ID:", subscription.subscription_id)
    print("Subscription Name:", subscription.display_name)