from core.user.models import User 

data_user = {
    "email": "testuser@yopmail.com",
    "username": "john-doe",
    "password": "12345",
    "first_name": "John",
    "last_name": "Doe"
}

user = User.objects.create_user(**data_user)
print(user.name)

print(user.email)

print(user.password)