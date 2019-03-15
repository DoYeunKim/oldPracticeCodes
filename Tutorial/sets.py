# Sets use curly brackets
# set([]) = {}
# No duplicates
# Elements are immutable, but the sets are not
# No indexing
Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
Months = {"Jan", "Feb", "Mar"}
Dates = {21, 22, 17}

print (Days)
print (Months)
print (Dates)

# Accessing values in a set
for d in Days:
    print(d, end = " ")
print()

# Adding items to a set
# SetName.discard(blah)
Days.add("Sun")
print (Days)

# Removing item from a set
# SetName.discard(blah)
Days.discard("Sun")
print(Days)

# Union of sets (Use OR = | )
AllDays = Days|{"Sun"}
print (AllDays)

# Intersection of sets (Use AND = & )
AllDays = Days & {"Sun"}
print (AllDays)

# Difference of Sets (Use subtract = - )
# Only the elements from the first set and not in the second
AllDays = Days - {"Mon", "Thu"}
print (AllDays)

# Compare sets (subset or superset)
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)