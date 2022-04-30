from flask import Blueprint, request
from flask_pydantic import validate
import requests


# from app.exceptions.item import ItemDoesNotExist, ItemNameIsAlreadyThere


bp = Blueprint("oidc", __name__, url_prefix="/api/auth")


# GET http://localhost:8080/auth/realms/realm_001/protocol/openid-connect/auth?client_id=myclient&redirect_uri=https%3A%2F%2Fwww.keycloak.org%2Fapp%2F%23url%3Dhttp%3A%2F%2Flocalhost%3A8080%26realm%3Drealm_001%26client%3Dmyclient&state=bafe18a2-12cf-4849-bed8-333fa55fac4b&response_mode=fragment&response_type=code&scope=openid&nonce=327517ea-1237-4117-8136-d3b1321c3794


@bp.route("", methods=["GET"])
def receiving_callback_step1():
    print(request.url)
    print(request.args)
    print(request.headers)
    return "nothing"