def fibbo_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield "{}:{}".format(i + 1, a)
        a, b = b, a + b

for item in fibbo_generator(10):
    print(item)

def users():
    users = dict(first_name = "Gonzalo", 
                last_namem = "Romero",
                gender = "M",
                age = 36
                )
    users['profession'] = "Software Enginner" 
    print(users)

users()
   