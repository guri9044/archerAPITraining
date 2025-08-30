from ArcherAPI import ArcherInstance
import os

os.system('cls' if os.name == 'nt' else 'clear')

archer = ArcherInstance("archer-irm.com/Archer", "training2025", "api.user", "Archer@123")
userId = archer.createUser( {"User":{"FirstName":"FirstName","LastName":"LastName",},"Password":"Archer@123"})
archer.assignRoleToUser({"UserId":userId,"RoleId":3,"IsAdd":'true'})