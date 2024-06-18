old_list = []
unique_list = []
n = int(input("Enter number of elements : "))
print("Enter elements ")
for i in range(0,n):
    ele = int(input())
    old_list.append(ele)
print(f"The elements of list are{old_list}")
for x in old_list:
    if old_list.count(x) == 1:
        unique_list.append(x)
print(f"The unique elements in the list are {unique_list}")

