import requests

url = 'https://dev340589.service-now.com/api/now/table/sn_grc_issue?sysparm_limit=1'
user = 'admin'
pwd = 'O59VDaxl*=pH'
headers = {"Content-Type":"application/json","Accept":"application/json"}

response = requests.get(url, auth=(user, pwd), headers=headers )

if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())

data = response.json()
print(data)

from cryptography.fernet import Fernet

#key = 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode()
def decrypt(encrypted_password: bytes, key: bytes) -> str:
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted


class ServiceNowAPI:
    def __init__(self, inst_url, username, password):
        self.api_url_base = f"https://{inst_url}/"
        self.username = decrypt(username.encode(), 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode())
        self.password = decrypt(password.encode(), 'yLcmh4BfdJIEJUqwjd_U13F8pWEgviR_PpHE3edePUQ='.encode())
        self.headers = {
            "Accept": "application/json,text/html,application/xhtml+xml,application/xml;q =0.9,*/*;q=0.8",
            "Auth": "application/json"
        }