# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()

# f = open("demo.txt", "r")
# data = f.readlines()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt", "r")
# for line in f:
#     print(line.strip())
# f.close()

# f = open("demo.txt", "r")
# data = f.read(10)
# print(data)
# f.close()
# f = open("demo.txt","r")
# for line in f:
#     print(line.strip())
# f.close()

# f = open("demo.txt", "r+")
# data = f.read()
# print("BEFORE WRITE:", data)


# new_data = f.read()
# print("AFFTER WRITE:", new_data)
# f.close()

# f = open("demo.txt", "r+")
# content = f.read()
# print("before\n", content)

# f.seek(0)

# f.write("this is new content\n")
# new_content = f.read()
# print("after\n", new_content)
# with open("demo.txt", "r+") as f:
#     print("Before:", f.read())   # पुराना content पढ़ना

#     f.seek(0)                   # cursor को शुरुआत पर ले जाओ
#     f.write("Hi")               # "Hello" के H,e को overwrite कर देगा

#     f.seek(0)                   # cursor वापस शुरुआत पर
#     print("After:", f.read())

# f = open("demo.txt", "w")
# f.write("this is new data\n")
# f.write("this is second line\n")
# f.close() 

# f = open("demo.txt", "w")
# data =f.write("this is new data\n")
# # print(data)
# # f.close()
# # f = open("demo.txt", "a")
# # f.write("this is new data\n")
# # f.close()
# # with open("demo.txt", "r") as f:
# #     print(f.read())
    
# # with open("demo.txt", "w") as f:
# #     f.write("this is new file\n")

# # import os 
# # os.remove("demo.txt")


# # f  = open("practice.txt", "w")
# # f.write("Hi everyone\n we are learning file I/o \n using Java \n I like prrogramming in Java.")
# # f.close()

# # f = open("practice.txt", "r")
# # data = f.read()


# # data = data.replace("Java", "Python")
# # print(data)


# # f = open("practice.txt", "w")
# # f.write(data)
    
    
# # f.close()

# # with open("practice.txt", "r") as f:
# #     data = f.read()
    
# # data = data.replace("Python", "Java")
# # print(data)

# # with open("practice.txt", "w") as f:
# #     f.write(data)
# def check_for_word():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#       data = f.read()
#       if(data.find("learning")):
#         print("found")
#       else:
#          print("not found")
# check_for_word()

# def check_for_line():
#   word = "learning"
#   line_no = 1
#   with open("practice.txt", "r") as f:
#       for line in f:
#          if word in line:
#             print("found at line no:", line_no)
#             return 
#          line_no += 1
#   print("not found")
  
# check_for_line()

# with open("practice.txt" "r") as f:
#     data = f.read()
#     if(data.find("learning")):
#         print("found")
#     else:
#         print("not found")
        
        
        
        
# with open("practice.txt", "r") as f:
#    data = f.read()
#    data = data.find("learning")
#    print("found at index:" , data)
    
    
# def check_for_word():
  
#   with open("practice.txt", "r") as f:
#    data = f.read()
#    data = data.find("learning")
#    if data != -1:
#      print("found")
#    return 
    
# check_for_word()


# def check_for_line():
#   word = "learning"
#   with open("practice.txt", "r") as f:
#     line_no = 1
#     for line in f:
#         if word in line:
#            print("found at line no:", line_no) 
#            line_no += 1
#            return
#   print("not found")
        
# check_for_line()  
      
# count = 0
# with open("practice.txt", "r") as f:
#   data = f.read()
#   print(data)
  
#   # num = ""
#   # for i in range(len(data)):
#   #    if data[i] == ",":
#   #      print(int(num))
#   #      num = ""
#   #    else:
#   #      num += data[i]
#   nums = data.split(",")
#   for val in nums:
#     if (int(val) % 2) == 0:
      
#       count += 1
# print(count)

# with open("practice.txt", "w") as f:
#   data = f.write("Hi everyone\n we are learning file I/O \n using Python \n I like programming in Python.")
#   content =  f.write("\n1,2,3,4,5,6,7,8,9,10")
 
#   print(data)
#   print(content)


# with open("practice.txt", "r+") as f:
#     data = f.read()
# new_data = data.replace("Python", "Java")
# print(new_data)
    
    
# with open("practice.txt", "w") as f:
#   f.write(new_data)

# with open("practice.txt", "r") as f:
#   data = f.read()
#   print("This is old data :")
#   print(data)
# new_data = data.replace("Java", "Python")
# print("This is new data")
# print(new_data)

# with open("practice.txt", "w") as f:
#  n = f.write(new_data)
 
 
# with open("practice.txt", "r") as f:
#   data = f.read()
#   new_data = data.find("Python")
#   if new_data != -1:
#     print("found at index:", new_data)
#   else:
#     print("not found")
    
    
# with open("practice.txt", "r") as f:
#   word = "learnog"
#   data = f.read()
#   new_data = data.find(word)
#   if new_data != -1:
#     print("not found")
#   else:
#     print("found")
# with open("practice.txt", "r") as f:
 
#   data = f.read()
#   new_data = data.find("")
#   if new_data != -1:
#     print("found")
#   else:
#     print("not found")
# with open("practice.txt", "r") as f:
#   data = f.read()
#   if (data.find("learning")) != -1:
#     print("found")
#   else:
#     print("notfound")
# with open("practice.txt", "r") as f:
#   data = f.read()
#   word = input("enter a word to search :")
#   new_data = data.find(word)
#   if new_data != -1:
#     print("found at index:", new_data)
#   else:
#     print("not found")
# with open("practice.txt", "r") as f:
#  data = f.close()
# new_data = data.find("learning")
# if new_data != -1:
#     print("found")
# else:
#     print("not found")
# def check_for_word():
#  with open("practice.txt", "r") as f:
#   data = f.read()
#   new_data = data.find("Python")
#   if new_data != -1:
#    print("found")
#   else:
#    print("not found")
# check_for_word()


# def check_for_line():
#     line_no = 1
#     word = "learning"
#     with open("practice.txt", "r") as f:
#       data = f.readline()
#       for line in f:
#         if word in line:
#           print("found at line_no:", line_no)
#           return
#         line_no += 1
        
# check_for_line()
# count = 0
# with open("practice.txt" , "r") as f:
#     data = f.read()    
#     print(data)
#     new_data = data.split(",")
#     print(new_data)
#     for val in new_data:
#         if (val % 2 == 0):
#             count += 1
            
# print(count)


# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)
    
#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(num)
#         else:
#             num += data[i]


  