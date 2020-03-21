import re

def thing(pin):
    print(bool(re.match("^[0-9]{4}$|^[0-9]{6}$", pin)))
    
thing("1234")
thing("12345")
thing("123456")
thing("a234")

# thing() 