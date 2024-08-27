import sys
import os
from fastapi.testclient import TestClient

# Adiciona o diretório 'app' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from main import app

client = TestClient(app)

def test_query_yields_10_results():
    response = client.get("/query?query=same bed but it feels just a little bit bigger now")
    json_response = response.json()
    
    assert response.status_code == 200
    assert len(json_response["results"]) == 10
    assert json_response["message"] == "OK"

def test_query_yields_few_results():
    response = client.get("/query?query=hello")
    json_response = response.json()
    
    assert response.status_code == 200
    assert 1 < len(json_response["results"]) < 10
    assert json_response["message"] == "OK"

# this test is not obvious because of the huge relevance value
def test_query_yields_non_obvious_results():
    response = client.get("/query?query=die with a smile")
    json_response = response.json()
    
    assert response.status_code == 200
    assert len(json_response["results"]) > 0
    assert json_response["message"] == "OK"
    assert json_response["results"][0]["relevance"] > 0.9
