import users
import admin

admin1 = admin.Admin("name", "last name", "m", "somewhere", "someone@example.com", ["can add post", "can delete post", "can ban user"])
admin1.privileges.show_privileges()
