import requests


cookie_session_id = ""
# GET http://localhost:8080/auth/realms/realm_001/protocol/openid-connect/auth?client_id=myclient&redirect_uri=https%3A%2F%2Fwww.keycloak.org%2Fapp%2F%23url%3Dhttp%3A%2F%2Flocalhost%3A8080%26realm%3Drealm_001%26client%3Dmyclient&state=bafe18a2-12cf-4849-bed8-333fa55fac4b&response_mode=fragment&response_type=code&scope=openid&nonce=327517ea-1237-4117-8136-d3b1321c3794
def step_1():

    r = requests.get(
        url="http://keycloak:8080/auth/realms/realm_001/protocol/openid-connect/auth",
        params={
            "client_id": "mylocalclient",
            "redirect_uri": "http://auth-example-advanced:8000/api/auth",
            "realm": "realm_001",
            "response_type": "code",
            "scope": "openid"
        }
    )
    print(r.text)
    print(r.status_code)
    print(r.headers)
    return r.headers['Set-Cookie']


def step_2():
    ...


if __name__ == "__main__":
    cookie = step_1()