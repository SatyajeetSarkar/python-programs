a = "hello"

try:
    int(a)
    print(f"{a} is valid")
except:
    print('Type convertion invalid')