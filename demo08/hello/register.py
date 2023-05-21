import consul

def register_service():
    service_name = 'hello'
    service_port = 5000
    request_host = 'hello:5000'  # you'll need to determine the correct host and port
    client = consul.Consul(host='consul', port=8500)
    array = [
        {"Key": "traefik/http/routers/router01/entryPoints/0", "Value": "web"},
        {"Key": "traefik/http/routers/router01/service", "Value": service_name},
        {"Key": "traefik/http/routers/router01/rule", "Value": f"Path(`/{service_name}`)"},
        {"Key": f"traefik/http/services/{service_name}/loadBalancer/servers/0/url", "Value": f"http://{request_host}/"},
    ]

    for item in array:
        key = item["Key"]
        value = item["Value"]
        client.kv.put(key, value)

if __name__ == "__main__":
    register_service()
