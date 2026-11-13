txns = [{"txn_id": "T101", "user_id": "U1", "amount": 600, "location": "NY", "history": ["NY", "NY"]},{"txn_id": "T102", "user_id": "U2", "amount": 12000, "location": "NY", "history": ["NY"]},{"txn_id": "T103", "user_id": "U1", "amount": 100, "location": "London", "history": ["NY", "NY"]},]

def flag_the_user(txn_data: list[dict], criteria: int) -> list[str]:
  flagged_users = []
  for txn in txn_data: # hardcocoded
    amount = txn["amount"] # 
    user_id = txn["user_id"]
    if amount > criteria:
      txn["flag"] = "flagged" # write insert into table
      flagged_users.append(user_id)# 
      print("you are being flagged")# 
    print(txn)
  return flagged_users

print(flag_the_user(txns, 500))
print(flag_the_user(txns, 10000))

def validation_by_manager(func, user_id, data, criteria):
  for user in func(data, criteria):
    if user == user_id:
      print("skip the user")
    else:
      print("valdate teh user")
      
validation_by_manager(flag_the_user, "U1", txns, 500)