import pytest
import requests
import json


def test_get_home():
    response = requests.get("http://localkost:3000/register")
    assert response.headers["Content-Type"] == "application/json"