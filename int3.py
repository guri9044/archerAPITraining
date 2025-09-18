import requests

url = "https://archer-irm.com/Archer/contentapi/Findings"

payload = "{'Findings_Id': 348575, 'ServiceNow_ID': '278d2114c3c432106063b6fdd4013196'\r\n}"
headers = {
  'Cookie': '__ArcherSessionCookie__=1F67F786AFAEEAC7138ECFDF72C01D31'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
