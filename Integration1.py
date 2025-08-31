from ArcherAPI import ArcherInstance
import os


os.system('cls' if os.name == 'nt' else 'clear')

archer = ArcherInstance("archer-irm.com/Archer", "training2025", "api.user", "Archer@123")
#userId = archer.createUser( {"User":{"FirstName":"FirstName","LastName":"LastName",},"Password":"Archer@123"})
#archer.assignRoleToUser({"UserId":userId,"RoleId":3,"IsAdd":'true'})

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
    #print(f"Getting record for Id - {recordId}")
    archRec = archer.Record(archer)
    rec = archRec.getRecordById(recordId)
    #print(rec['FieldContents'])
    #fi = '2265'
    #if fi in rec['FieldContents']:
            #print(rec['FieldContents'][fi]['Value'])
    for field in FindingFields:
        id = str(field['FieldId'])
        #print(id)
        if id in rec['FieldContents']:
            #print(rec['FieldContents'][id]['Value'])
            recordObject.append({"FieldId":field['FieldId'],"FieldName":field['FieldName'],"Value":rec['FieldContents'][id]['Value']})
        #else:
            #print(f"Field Id {id} not found in record {recordId}")
        
print(recordObject)




archContent = archer.Content(archer)
#archContent.getContentById('Findings',348575)