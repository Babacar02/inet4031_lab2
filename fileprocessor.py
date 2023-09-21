f = open('fileprocessor.input', 'r')

lines = f.readlines()

user_data = []

for line in lines:
    line = line.strip()

    if line.startswith('#'):
        continue

    parts = line.split(':')

    if len(parts) == 4:
        
        user_data.append(tuple(parts))

print("Printing out User Data: ")
print("\n")
for x in user_data:
    user, password, userid, groupid = x 
    print(f"The user {user} has a password of {password} and has userid {userid} and groupid {groupid}")

print("\n")
print("End of User Data")







f.close()
