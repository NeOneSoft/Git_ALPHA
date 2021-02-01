def fibbo_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield "{}:{}".format(i + 1, a)
        a, b = b, a + b

for item in fibbo_generator(10):
    print(item) 