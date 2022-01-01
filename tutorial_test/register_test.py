import pytest
import requests
import json
@pytest.mark.parametrize("id", "name","phone","password","email",[(1,"George","077125555","husyd"),(2,"Janet")])
def test_list_valid_user(url,id,name):
	url = "http://localhost:3000/register"
	resp = requests.get(url)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['data']['id'] == id, resp.text
	assert j['data']['first_name'] == name, resp.text

def test_list_invaliduser(url):
	url = "http://localhost:3000/register"
	resp = requests.get(url)
	assert resp.status_code == 404, resp.text