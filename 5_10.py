current_users = ['mac', 'dee', 'dennis', 'frank', 'charlie']
new_users = ['MAC', 'dee', 'bruce', 'paige', 'bill']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("The following user, " + new_user + " needs a user name.")
    else:
        print("The following username, " + new_user + " is available.")
print("\nList complete")