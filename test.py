import requests
import json
import xmltodict
import os

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

response = requests.post(url, headers=headers, json=payload)
data = json.loads(response.content)
session_token = data["RequestedObject"]["SessionToken"]
print("session token - {session_token}\n")

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

print("\n**************************************************************************")