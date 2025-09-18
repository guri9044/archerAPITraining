import requests
import json

class ServiceNowAPI:
    def __init__(self, inst_url, username, password):
        self.api_url_base = f"https://{inst_url}/"
        self.username = username
        self.password = password
        self.headers = {
            "Content-Type": "application/json",
            "Auth": "application/json"
        }
    def getRecord(self, tableName, sysId):   
        response = requests.get(f"{self.api_url_base}api/now/table/{tableName}/{sysId}", auth=(self.username, self.password), headers=self.headers)
        data = json.loads(response.content)
        if response.status_code == 200:
            return data['result']
        else:
            print("Error: ", response.status_code, response.content)
    
    def createRecord(self, tableName, recordDetails):
        response = requests.post(f"{self.api_url_base}api/now/table/{tableName}", auth=(self.username, self.password), headers=self.headers, json=recordDetails)
        data = json.loads(response.content)
        if response.status_code == 201:
            print("Record created with Sys ID - ", data['result']['sys_id'])
            return data['result']['sys_id']
        else:
            print("Error: ", response.status_code, response.content)

    def updateRecord(self, tableName, sysId, updateDetails):
        response = requests.patch(f"{self.api_url_base}api/now/table/{tableName}/{sysId}", auth=(self.username, self.password), headers=self.headers, json=updateDetails)
        data = json.loads(response.content)
        if response.status_code == 200:
            print("Record updated with Sys ID - ", data['result']['sys_id'])
            return data['result']['sys_id']
        else:
            print("Error: ", response.status_code, response.content)