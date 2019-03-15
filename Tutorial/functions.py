"""
def functionName( parameters ):
    "function_docstring"
    function_suite
    return [expression]
"""

def printme (str):
    "This prints a passed string into this funciton"
    print(str)
    return

printme("blah")

# All parameters passed by reference 
# Changes inside the called function are reflected in the calling function
def changeme (mylist):
    "This changes a passed list into this function"
    print ("VAlues inside the function before change:", mylist)

    mylist[2] = 50
    print ("Values inside the function after change:", mylist)

    # Here, a "new" variable mylist is created, separate from the original reference
    mylist = [1,2,3]
    print ("Updated(?) mylist:", mylist)
    return

mylist = [10,20,30]
changeme(mylist)
print("Values outside the function:", mylist)