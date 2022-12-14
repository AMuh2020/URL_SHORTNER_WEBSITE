alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
from random import randint
# if 0 then lowercase letter if 1 then uppercase letter if 2 then number 0-9
def random_string():
    string = ""
    for i in range(6):
        choice = randint(0,2)
        if choice == 0:
            index = randint(0,25)
            string += str(alphabet[index])
        elif choice == 1:
            index = randint(0,25)
            string += str(alphabet[index].upper())
        elif choice == 2:
            index = randint(0,9)
            string += str(index)
    
    return string