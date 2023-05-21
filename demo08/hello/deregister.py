import consul

def deregister_service():
    service_name = 'hello'
    client = consul.Consul(host='consul', port=8500)
    keys = [
        "traefik/http/routers/router01/entryPoints/0",
        "traefik/http/routers/router01/service",
        "traefik/http/routers/router01/rule",
        f"traefik/http/services/{service_name}/loadBalancer/servers/0/url",
    ]

    for key in keys:
        client.kv.delete(key)

if __name__ == "__main__":
    deregister_service()
