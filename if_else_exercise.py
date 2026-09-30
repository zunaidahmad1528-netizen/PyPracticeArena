# Check age categories using if, elif, and else.
age = int(input("Apni age likho: "))
if age < 0:
	print("Age valid nahi hai.")
elif age < 18:
	print("Aap minor hain.")
elif age < 60:
	print("Aap adult hain.")
else:
	print("Aap senior citizen hain.")