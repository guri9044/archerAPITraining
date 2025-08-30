from ArcherAPI import ArcherInstance

archer = ArcherInstance("archer-irm.com/Archer", "training2025", "api.user", "Archer@123")
session_token = archer.login()
print("Session Token from Archer Instance:", session_token)