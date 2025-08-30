import json
import requests

class ArcherInstance:
    #default initialization method to set up instance variables and creating self object
    def __init__(self, inst_url, instance_name, username, password):
        self.api_url_base = f"https://{inst_url}/platformapi/"
        self.username = username
        self.password = password
        self.instance_name = instance_name
        self.session_token = ""
        self.login()
        self.headers = {
            "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q =0.9,*/*;q=0.8",
            "Content-type": "application/json",
            "Authorization": 'Archer session-id='+self.session_token
        }
    
    #login method to authenticate and get session token
    def login(self):
        api_url = f"{self.api_url_base}core/security/login"
        header = {"Accept": "application/json,text/html,application/xhtml+xml,application/xml;q =0.9,*/*;q=0.8",
				  "Content-type": "application/json"}
        response = requests.post(api_url, headers=header, json={"InstanceName": self.instance_name,
                                                                "Username": self.username, "UserDomain": "",
                                                                "Password": self.password}, verify=False)
        data = json.loads(response.content.decode("utf-8"))
        if response.status_code == 200:
            archerReqSuccess = data["IsSuccessful"]
        if archerReqSuccess:
            self.session_token = data["RequestedObject"]["SessionToken"]
            return self.session_token
        else:
            print("Login Failed")
    
    #create a user in Archer
    def createUser(self, userDetails):
        response = requests.post(f"{self.api_url_base}core/system/user", headers=self.headers, json=userDetails, verify=False)
        data = json.loads(response.content)
        
        if response.status_code == 200:
            archerReqSuccess = data["IsSuccessful"]
        if archerReqSuccess:
            userId = data["RequestedObject"]["Id"]
            print("User ceated with Id - ",userId)
            return userId
    
    #assign role to user in Archer
    def assignRoleToUser(self, userRoleDetails):
        response = requests.put(self.api_url_base+"core/system/userrole", headers=self.headers, json=userRoleDetails, verify=False)
        data = json.loads(response.content)
        if response.status_code == 200:
            archerReqSuccess = data["IsSuccessful"]
        if archerReqSuccess:
            roleId = data["RequestedObject"]["Id"]
            print("Role with Id - ",roleId)