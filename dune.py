
from json import loads
from requests import get, post
import pandas as pd
import asyncio
import time

DUNE_API_KEY = "0VrW09910Jv5mwdNR2Rm1jXcx9cCfXK5"
HEADER = {"x-dune-api-key" : DUNE_API_KEY}

BASE_URL = "https://api.dune.com/api/v1/"

def make_api_url(module, action, ID):
    """
    We shall use this function to generate a URL to call the API.
    """

    url = BASE_URL + module + "/" + ID + "/" + action

    return url

def execute_query(query_id):
    """
    Takes in the query ID.
    Calls the API to execute the query.
    Returns the execution ID of the instance which is executing the query.
    """

    url = make_api_url("query", "execute", query_id)
    response = post(url, headers=HEADER)
    execution_id = response.json()['execution_id']

    return execution_id

def get_query_status(execution_id):
    """
    Takes in an execution ID.
    Fetches the status of query execution using the API
    Returns the status response object
    """

    url = make_api_url("execution", "status", execution_id)
    response = get(url, headers=HEADER)

    return response

def get_query_results(execution_id):
    """
    Takes in an execution ID.
    Fetches the results returned from the query using the API
    Returns the results response object
    """

    #status = await get_query_status(execution_id)
    url = make_api_url("execution", "results", execution_id)
    response = get(url, headers=HEADER)

    return response

def produce_query_results(query_id):
    execution_id = execute_query(str(query_id))

    execution_state = ""
    while( not execution_state or execution_state != "QUERY_STATE_COMPLETED"):
        resp = get_query_status(execution_id)
        time.sleep(5)
        print(resp.json())
        execution_state = resp.json()['state']
    print(execution_id)

    response = get_query_results(execution_id)


    #if(response.json()['state']=='QUERY_STATE_COMPLETED'):
    data = pd.DataFrame(response.json()["result"]["rows"])

    return data

#produce_query_results(1531431)