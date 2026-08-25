identity = {
    "name": "terraform-pipeline",
    "properties": {
        "principalId": "abc-123",
        "type": "ServicePrincipal"
    }
}

vm = {
    "name": "prod-web-01",
    "properties": {
        "hardwareProfile": {
            "vmSize": "Standard_D2s_v5"
        }
    }
}
print(identity["properties"]["type"])
print(vm["properties"]["hardwareProfile"]["vmSize"])