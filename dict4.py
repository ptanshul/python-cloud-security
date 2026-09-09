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


vm1 = {
    "name": "prod-web-01",
    "network": {
        "publicAccess": {
            "enabled": True,
            "ip": "20.10.10.10"
        }
    }
}
print(identity["properties"]["type"])
print(vm["properties"]["hardwareProfile"]["vmSize"])

print(vm1["network"]["publicAccess"]["enabled"])