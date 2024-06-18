def nearly_equal(s1, s2):
    if len(s1) != len(s2):
        print("string are not nearly equal")
    elif(s1==s2):
        print("Both string are equal")
    else:
        n = len(s1)
        i = 0
        count = 0
        for i in range(n):
            if s1[i] == s2[i]:
                pass
            else:
                count = count + 1
        if count == 1:
            print("String are nearly equal")
        else:
            print("string are not nearly equal")


s1 = input("enter the first string\n")
s2 = input("enter the second string\n")
nearly_equal(s1, s2)

