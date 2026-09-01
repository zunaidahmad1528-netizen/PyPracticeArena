info = {
    "firstname" : "mohd",
    "last name" : "zunaid",
    "age" : 22, 
    "city" : "utter pradesh",
    "country" : "india",
    "is_married" : False,
    "skills" : ["c", "c++", "python", "java", "html", "css", "javascript"],
    12 : 3.3,
    3.2 : "hello",
    "list" : [1,2,3,4,5,6],
    "tuple" : (1,2,3,4,5,6),
    
}
print(info)

info["firstname"] = "mohd zunaid"
info["age"] = 19
print(info)

null_dict = {}
null_dict["name"] = "mohd zunaid"
print(null_dict)

# nested dictionary

student = {
    "name" : "mohd zunaid",
        "scores" : { 
            "math" : 80,
            "science" : 88,
            "english" : 70,
            
                 }
}
print(student['scores']["math"])
print(student.keys())
print(list(student.keys()))
print(type(student.keys()))
print(len(student))
print(len((student.keys())))

print(list(student.values()))

print(list(student.items()))
pairs = list(student.items())
print(pairs[1])
print(student.get("name6"))
print("ysyuyh")

student.update({"name2" : "mohd rihan"})
print(student)

