import requests
import json
import xmltodict
import os
import csv

#from ArcherAPI import ArcherInstance

#clear terminal screen
os.system('cls' if os.name == 'nt' else 'clear')

url = "https://archer-irm.com/Archer/platformapi/core/security/login"

payload = {
  "InstanceName": "training2025",
  "Username": "api.user",
  "UserDomain": "",
  "Password": "Archer@123"
}
headers = {
  'Content-Type': 'application/json'
}

'''response = requests.post(url, headers=headers, json=payload)
data = json.loads(response.content)
if response.status_code == 200:
    archerReqSuccess = data["IsSuccessful"]
    if archerReqSuccess:
        print("Login Successful - ")
        session_token = data["RequestedObject"]["SessionToken"]
        print("session token - ",session_token)
    else:
        print("Login Failed")


#print(data)
#session_token = data["RequestedObject"]["SessionToken"]
#print("session token - {session_token}\n")
'''
'''
url = "https://archer-irm.com/Archer/ws/search.asmx"
payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchemainstance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\n  <soap:Body>\n    <SearchRecordsByReport xmlns=\"http://archer-tech.com/webservices/\">\n      <sessionToken></sessionToken>\n      <reportIdOrGuid>10388</reportIdOrGuid>\n      <pageNumber>1</pageNumber>\n    </SearchRecordsByReport>\n  </soap:Body>\n</soap:Envelope>\n"
headers = {
  'Accept': 'application/xml, text/xml, */*; q=0.01',
  'Content-Type': 'text/xml',
  'X-Requested-With': 'XMLHttpRequest'
}

response = requests.post( url, headers=headers, data=payload)

#print(response.text)

o = xmltodict.parse(response.text)
rootXMLstr = o["soap:Envelope"]["soap:Body"]["SearchRecordsByReportResponse"]["SearchRecordsByReportResult"]
jsonData = json.dumps(xmltodict.parse(rootXMLstr))
print(jsonData)
'''
csv_file = 'Users.csv'
json_data = []

with open(csv_file, newline='', encoding='utf-8-sig') as f:  # Use utf-8-sig to remove BOM
    reader = csv.DictReader(f)
    for row in reader:
        json_data.append(row)

# Print the JSON object
userArray = json.dumps(json_data, indent=2)
#print(userArray)
session_token = '412070C3BD81F3130F8C021716068626'
for user in json_data:
    headers = {
              'Content-Type': 'application/json',
              'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
              'Authorization':'Archer session-id='+session_token
              }
    json_data2 = {
        "User":
                  {
                  "FirstName":user["FirstName"],
                  "LastName":user["LastName"],
                  },
                  "Password":user["Password"],
                  }
    response = requests.post("https://archer-irm.com/Archer/platformapi/core/system/user", headers=headers, json=json_data2)
    data = json.loads(response.content)
    if response.status_code == 200:
        archerReqSuccess = data["IsSuccessful"]
        if archerReqSuccess:
            print("User created Successfully - ")
            userId = data["RequestedObject"]["Id"]
            print("Ussr Id - ",userId)
            reolepayload = {"UserId":userId,"RoleId":3,"IsAdd":'true'}
            roleResponse = requests.put("https://archer-irm.com/Archer/platformapi/core/system/userrole", headers=headers, json=reolepayload)
            roledata = json.loads(roleResponse.content)
            print(roledata)
            if roleResponse.status_code == 200:
                roleReqSuccess = roledata["IsSuccessful"]
                if roleReqSuccess:
                    print("Role assigned Successfully - ")
                else:
                    print("Role assignment Failed")
                    
        else:
            print("Login Failed")

print("\n**************************************************************************")