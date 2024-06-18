import random
number=random.randint(1,10)
class Error(Exception):
    pass
class ValueSmallError(Error):
    pass
class ValueLargeError(Error):
    pass
while True:
    try:
        guess=int(input("Enter a Number "))
        if guess<number:
            raise ValueSmallError
        elif guess>number:
            raise ValueLargeError
        break

    except ValueSmallError:
        print("ayiji undu baji kammi andhu, Try again")
    except ValueLargeError:
        print("ayiji undu mastu malla andhu, Try again")

print("Eru bayankara mare avoli eru !!!!")