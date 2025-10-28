f = open("calculator.c" , "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("calculator.c" , "r")
data = f.read(5)
print(data)
print(type(data))
f.close
f = open("calculator.c" , "r")
data = f.readline()
print(data)
print(type(data))()

f = open("calculator.c" , "w+")
data = f.write("hello mohd zunaid we are replacing your file frome this to this file")
print(data)
print(type(data))
f.close()


f = open("calculator.c", "r")
line1 = f.readline()
print(line1)



line2 = f.readline()
print(line2)
f.close()

f = open("calculator.c", "w")
data = f.write("hello mohd zunaid this is your new file")
print(data)
f.close()