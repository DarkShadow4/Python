current_users = ["admin", "user1", "user2", "user3", "user4"]
new_users = ["nuser1", "User2", "nuser2", "user3", "nuser3"]
#
# if len(current_users) == 0:
#     print "We need to find more users"
# else:
#     for usuario in current_users:
#         if usuario == "admin":
#             print "Hello", usuario, ", would you like to see a status report?"
#         else:
#             print "Hello", usuario, ", thank you for logging in again."
for usuario in new_users:
    taken = False
    for user in current_users:
        if usuario.lower() == user.lower():
            taken = True
    if taken:
        print usuario, "has already been taken, please choose another username."
    else:
        print usuario, "is avialable."
