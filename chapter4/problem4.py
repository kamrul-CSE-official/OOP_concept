fp = open("test.txt", "w")
fp.write("This file was created using python!")

print(type(fp))

fp.close()