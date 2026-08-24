vm = {
    "name": "prod-web-01",
    "location": "centralindia",
    "status": "Running",
    "public_ip": True,
    "port": 22
}
print(f"VM Name: {vm['name']}")
print(f"VM Location: {vm['location']}")
print(f"VM Status: {vm['status']}")
print(f"VM Public IP: {vm['public_ip']}")
print(f"VM Port: {vm['port']}")

if vm["public_ip"] == True:
    print("Security Alert !! VM is accessible from the internet.")