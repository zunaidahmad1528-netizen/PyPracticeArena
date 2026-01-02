# collection = {1, 2, 3, 4, 5}
# print(collection)
# print(type(collection))

# collection = {}
# print(collection)
# print(type(collection))

# collection = {1,2,3,3.5,33.44, "mohd", True, False, "zunaid"}
# print(collection)
# print(type(collection))

# collection.add(29)
# print(collection)

# collection.remove(29)
# print(collection)

# collection.remove("zunaid")
# collection.add("rihan")
# print(collection)

# collection.discard(45)
# print(collection)

# collection.clear()
# print(collection)


# col = {1,2,3,4,5,6, (7,8,9)}
# # print(col)
# # print(type(col))

# col.pop()
# print(col)

# # Set Operations (Mathsematical Operations)
# a = {1,2,3,4,5,5,5}
# b = {4,5,6,7,8,8}
# print(a.union(b))
# print(a | b)

# print(a.intersection(b))
# print(a & b)
 
# print(a.difference(b))
# print(a - b)

# print(b.difference(a))

# print(a ^ b)
# print(a.symmetric_difference(b))

# print(b ^ a)

# #  practice question



# dict = {
#     "table" : ("a piece of furniture" , "list of facts & figurea"),
#     "cat" : "a small animal"
# }
# print(dict)
# print(type(dict))

# set = {"py", "ja", "c++", "py", "js", "ja", "py", "ja", "c++", "c"}
# print(set)
# print(len(set))


# dictionary = {}
# print(dictionary)
# English = int(input("Enter your english marks :"))
# dictionary.update({"English" : English})
# Math = int(input("Enter your math marks :"))
# dictionary.update({"Math" : Math})
# Scieence = int(input("Enter your science marks :"))
# dictionary.update({"Science" : Scieence})
# print(dictionary)


# set = {"9",9.0}
# print(set)

# set = {
#     ("int" , 9),
#     ("float" , 9.0)
# }
# print(set)

# Long Set Program in Python

print("------ SET OPERATIONS PROGRAM ------")

# Taking input for first set
n1 = int(input("Enter number of elements in Set A: "))
set_a = set()

for i in range(n1):
    value = int(input("Enter element: "))
    set_a.add(value)

print("Set A =", set_a)

# Taking input for second set
n2 = int(input("\nEnter number of elements in Set B: "))
set_b = set()

for i in range(n2):
    value = int(input("Enter element: "))
    set_b.add(value)

print("Set B =", set_b)


while True:
    print("\n----- MENU -----")
    print("1. Add element to Set A")
    print("2. Remove element from Set A")
    print("3. Union of Set A and Set B")
    print("4. Intersection of Set A and Set B")
    print("5. Difference (A - B)")
    print("6. Difference (B - A)")
    print("7. Check element in Set A")
    print("8. Check subset")
    print("9. Display both sets")
    print("10. Clear Set A")
    print("11. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = int(input("Enter element to add: "))
        set_a.add(x)
        print("Updated Set A =", set_a)

    elif choice == 2:
        x = int(input("Enter element to remove: "))
        if x in set_a:
            set_a.remove(x)
            print("Updated Set A =", set_a)
        else:
            print("Element not found")
    elif choice == 3:
        print("Union =", set_a | set_b)

    elif choice == 4:
        print("Intersection =", set_a & set_b)

    elif choice == 5:
        print("A - B =", set_a - set_b)

    elif choice == 6:
        print("B - A =", set_b - set_a)
        
        
        
    elif choice == 7:
        x = int(input("Enter element to check: "))
        if x in set_a:
            print("Element exists in Set A")
        else:
            print("Element does not exist")

    elif choice == 8:
        if set_a.issubset(set_b):
            print("Set A is subset of Set B")
        else:
            print("Set A is NOT subset of Set B")
    elif choice == 9:
        print("Set A =", set_a)
        print("Set B =", set_b)

    elif choice == 10:
        set_a.clear()
        print("Set A cleared")

    elif choice == 11:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")