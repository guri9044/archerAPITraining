import json
import requests

class ArcherInstance:
    def __init__(self, inst_url, instance_name, username, password):
        self.api_url_base = f"https://{inst_url}/platformapi/"
        self.username = username
        self.password = password
        self.instance_name = instance_name
        self.session_token = ""	
        self.login()
    
    def login(self):
        api_url = f"{self.api_url_base}core/security/login"
        header = {"Accept": "application/json,text/html,application/xhtml+xml,application/xml;q =0.9,*/*;q=0.8",
				  "Content-type": "application/json"}
        response = requests.post(api_url, headers=header, json={"InstanceName": self.instance_name,
                                                                "Username": self.username, "UserDomain": "",
                                                                "Password": self.password}, verify=False)
        data = json.loads(response.content.decode("utf-8"))
        print(data)
        self.session_token = data["RequestedObject"]["SessionToken"]