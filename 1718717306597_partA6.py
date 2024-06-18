number_of_word=0
number_of_lines=0
number_of_characters=0
file_path="example4.txt"

with open(file_path,'w+')as file :
    file.write("hello,\nWorld!")

with open(file_path,'r')as file:
    for l in file :
        number_of_word+=len(l.split())
        number_of_lines+=1
        number_of_characters+=len(l.strip())

print("no of words :",number_of_word)
print("no of lines :",number_of_lines)
print("no of characters :",number_of_characters)