
def multi(a,b=10):  
    a = a 
    b = b
    return a*b

# when we import file the entire file runs once so this calling also execute once to that i wrote this 
if __name__ == "__main__":
    print(__name__)
    print(type(__name__))
    print(multi(3,4))