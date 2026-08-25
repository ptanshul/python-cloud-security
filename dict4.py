identity = {
    "name": "terraform-pipeline",
    "properties": {
        "principalId": "abc-123",
        "type": "ServicePrincipal"
    }
}
print(identity["properties"]["type"])