
from json import loads
from requests import get, post
import pandas as pd
import time

class DuneAPI():
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.dune.com/api/v1/"
        self.header = {"x-dune-api-key" : api_key}


    def make_api_url(self, module, action, ID):
        """
        We shall use this function to generate a URL to call the API.
        """

        url = self.base_url + module + "/" + ID + "/" + action

        return url

    def execute_query(self, query_id):
        """
        Takes in the query ID.
        Calls the API to execute the query.
        Returns the execution ID of the instance which is executing the query.
        """

        url = self.make_api_url("query", "execute", query_id)
        response = post(url, headers=self.header)
        execution_id = response.json()['execution_id']

        return execution_id

    def get_query_status(self, execution_id):
        """
        Takes in an execution ID.
        Fetches the status of query execution using the API
        Returns the status response object
        """

        url = self.make_api_url("execution", "status", execution_id)
        response = get(url, headers=self.header)

        return response

    def get_query_results(self, execution_id):
        """
        Takes in an execution ID.
        Fetches the results returned from the query using the API
        Returns the results response object
        """

        #status = await get_query_status(execution_id)
        url = self.make_api_url("execution", "results", execution_id)
        response = get(url, headers=self.header)

        return response

    def produce_query_results(self, query_id):
        execution_id = self.execute_query(str(query_id))

        execution_state = ""

        while( not execution_state or execution_state != "QUERY_STATE_COMPLETED"):
            resp = self.get_query_status(execution_id)
            time.sleep(5)
            print(resp.json())
            execution_state = resp.json()['state']

        response = self.get_query_results(execution_id)


        data = pd.DataFrame(response.json()["result"]["rows"])

        return data

if(__name__=='__main__'):
    DUNE_API_KEY = "0VrW09910Jv5mwdNR2Rm1jXcx9cCfXK5"
    dune = DuneAPI(DUNE_API_KEY)
    dune.produce_query_results(1258228)