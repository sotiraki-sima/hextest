
file1 = open('file.txt', 'r')
Lines = file1.readlines()

#print(int("0xff", 16))
# JFIF

# Strips the newline character
all_str = ""
for line in Lines:
    clean = line.strip().replace("-ne ","").replace("\\x","")
    all_str += clean
    #print(clean)
    #break
print(all_str)