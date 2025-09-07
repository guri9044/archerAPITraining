import json
import requests
from cryptography.fernet import Fernet

#key = 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode()
def decrypt(encrypted_password: bytes, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

class ArcherInstance:
    #default initialization method to set up instance variables and creating self object
    def __init__(self, inst_url, instance_name, username, password):
        self.api_url_base = f"https://{inst_url}/"
        self.username = decrypt(username.encode(), 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode())
        self.password = decrypt(password.encode(), 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode())
        self.instance_name = instance_name
        #self.session_token to store session token after login and be used in all other methods
        self.session_token = ""
        self.login()
        self.headers = {
            "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q =0.9,*/*;q=0.8",
            "Content-type": "application/json",
            "Authorization": 'Archer session-id='+self.session_token
        }
    
    #login method to authenticate and get session token
    def login(self):
        api_url = f"{self.api_url_base}platformapi/core/security/login"
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
        response = requests.post(f"{self.api_url_base}platformapi/core/system/user", headers=self.headers, json=userDetails, verify=False)
        data = json.loads(response.content)
        
        if response.status_code == 200:
            archerReqSuccess = data["IsSuccessful"]
        if archerReqSuccess:
            userId = data["RequestedObject"]["Id"]
            print("User ceated with Id - ",userId)
            return userId
    
    #assign role to user in Archer
    def assignRoleToUser(self, userRoleDetails):
        response = requests.put(self.api_url_base+"platformapi/core/system/userrole", headers=self.headers, json=userRoleDetails, verify=False)
        data = json.loads(response.content)
        if response.status_code == 200:
            archerReqSuccess = data["IsSuccessful"]
        if archerReqSuccess:
            roleId = data["RequestedObject"]["Id"]
            print("Role with Id - ",roleId)

    class Record:
        def __init__(self, archer_instance):
            self.archer_instance = archer_instance

        def getRecordById(self, recordId):
            response = requests.get(f"{self.archer_instance.api_url_base}platformapi/core/content/contentid?id={recordId}", headers=self.archer_instance.headers, verify=False)
            data = json.loads(response.content)
            #print(data)
            if response.status_code == 200:
                archerReqSuccess = data["IsSuccessful"]
            if archerReqSuccess:
                recordData = data["RequestedObject"]
                #print("Record Data: ", recordData)
                return recordData
    class Fields:
        def __init__(self, archer_instance):
            self.archer_instance = archer_instance

        def getFieldByAppId(self, appId):
            response = requests.get(f"{self.archer_instance.api_url_base}platformapi/core/system/fielddefinition/application/{appId}", headers=self.archer_instance.headers, verify=False)
            data = json.loads(response.content)
            #print(data)
            return data

    class Content:
        def __init__(self, archer_instance):
            self.archer_instance = archer_instance

        def getContentById(self, applicationName, contentId):
            response = requests.get(f"{self.archer_instance.api_url_base}contentapi/{applicationName}({contentId})", headers=self.archer_instance.headers, verify=False)
            data = json.loads(response.content)
            print(data)