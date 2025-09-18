from ArcherAPI import ArcherInstance
from ServiceNowAPI import ServiceNowAPI
import os
import json
import re

os.system('cls' if os.name == 'nt' else 'clear')

with open('configuration.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

#print(config['mapping']['fields'])

sn = ServiceNowAPI("dev340589.service-now.com", "admin", "O59VDaxl*=pH")
archer = ArcherInstance(str(config['Archer']['url']), str(config['Archer']['instance']), str(config['Archer']['username']),str(config['Archer']['password']))
#userId = archer.createUser( {"User":{"FirstName":"FirstName","LastName":"LastName",},"Password":"Archer@123"})
#archer.assignRoleToUser({"UserId":userId,"RoleId":3,"IsAdd":'true'})


archerDataSet = archer.getRecordsByReportId(reportId=config['mapping']['ArcherDeltaReportId'], pageNumber=1)
archerData = archerDataSet['Records']['Record']
#print(archerData)
def strip_html_tags(text):
    # Remove HTML tags using regex
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def process(config, sn, record):
    snowRec = {}
    fieldsData = record['Field']
    for field in fieldsData:
        #print(field)
        for fielfConfig in config['mapping']['fields']:
            if field['@id'] == fielfConfig['ArcherField']:
                if '#text' in field:
                    value = strip_html_tags(field['#text'])
                    snowRec[fielfConfig['ServiceNowField']] = value
    #print(snowRec)
    if 'sys_id' in snowRec:
        sys_id = sn.updateRecord(config['mapping']['ServiceNowTable'], snowRec['sys_id'], snowRec)
    else:
        sys_id = sn.createRecord(config['mapping']['ServiceNowTable'], snowRec)
        if sys_id:
            print("Updating Archer with Sys ID: ", sys_id)
            archerRec = archer.Record(archer)
            data = {"Content":{}}
            data['Content']['Id'] = snowRec['u_archer_finding_id']
            data['Content']['LevelId'] = 62
            data['Content']['FieldContents'] = {}
            data['Content']['FieldContents']['25264'] = {}
            data['Content']['FieldContents']['25264']['Type'] = 1
            data['Content']['FieldContents']['25264']['Value'] = sys_id
            data['Content']['FieldContents']['25264']['FieldId'] = 25264


            print(data)
            archerRec.updateRecord(data)


if(len(archerData) == 1):
    process(config, sn, archerData)
else:
    for record in archerData:
        process(config, sn, record)

recordsArray = [348575]
FindingFields = []
archFields = archer.Fields(archer)
FindingsAppFields = archFields.getFieldByAppId(167)
#print(FindingsAppFields)
for field in FindingsAppFields:
    #print(f"Field Id: {field['RequestedObject']['Id']}, Field Name: {field['RequestedObject']['Name']}")
    FindingFields.append({"FieldId":field['RequestedObject']['Id'],"FieldName":field['RequestedObject']['Name']})

#print(FindingFields)
#FindingFields = FindingFields[1:]

recordObject = []

for recordId in recordsArray:
    archRec = archer.Record(archer)
    rec = archRec.getRecordById(recordId)
    for field in FindingFields:
        id = str(field['FieldId'])
        if id in rec['FieldContents']:
            recordObject.append({"FieldId":field['FieldId'],"FieldName":field['FieldName'],"Value":rec['FieldContents'][id]['Value']})
        
#print(recordObject)



#archContent = archer.Content(archer)
#archContent.getContentById('Findings',348575)