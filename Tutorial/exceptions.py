"""
    Exception: base class for all exceptions
        StopIteration: next() does not point to any object
        SystemExit: sys.exit()
        StandardError: base class for rest
            ArithmeticError: base class for all numeric
                OverflowError: calculation exceeds max limit for a numeric type
                FloatingPointError: floating point calculation failure
                ZeroDivsionError: /0
            AssertionError: assert failure
            AttributeError: failure of attribute reference or assignment
            EOFError: no input from input() and the end of file is reached
            ImportError: import statement failure
            KeyboardInterrupt: user interrupts program execution (e.g. Ctrl+c)
            LookupError: base class for all lookup errors
                IndexError: index not found in a sequence
                KeyError: specified key not found in the dictionary
                NameError: identifier not found in th elocal/global namespace
                UnboundLocalError: access a local unassigned variable
            EnvironemntError: base class for outside of Python errors
                IOError: failure of i/o operations such as print() or open()
                OSError: OS-related errors
                SytaxError: error in Python syntax
                IndentationError: error in indentation
                SystemError: interpreter finds an internal problem
                SystemExit: Python interpreter quit by using sys.exit()
                TypeError: operation or function attempted w/ invalid type
                ValueError: built-infunction for a datatype has valid type of arguments but invalid values
    RuntimeError: generated error does not fall into any category
    NotImplementedError: abstract methods that needst to be implementd in an inherited class not actually implemented
"""

# Assert statement: assert Expression[, Arguments]
def KelvinToFahrenheit(Temp):
    assert (Temp >=0), "Colder than absolute Zero!"
    return (((Temp-273)*1.8)+32)

print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
#print(KelvinToFahrenheit(-5))

"""
    try:
        Operations
    except ExceptionI:
        If there is ExceptionI, then excetue this block
    except ExceptionII:
        If there is ExceptionII, then execute this block
    else:
        If there is no exception then execute this block
"""

# e.g.
try:
    fh = open("testfile", "w")  # If "w" is substituted for "r", then IOError would occur
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

"""
    try:
        Operations
        ... Due to any exception, this may be skipped
    finally:
        This should always be excecuted
"""

# e.g.

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!")
finally:
    print("Error: can\'t find file or read data")
    fh.close()

# More clean version

try:
    fh = open("testfile.txt", "w")
    try:
        fh.write("This is my test file for exception handling!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")


"""
    Argument of an exception

    try:
        Operations
    escept ExceptionType as ARgument:
        print value of argument here

"""

# e.g.

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("The argument does not contain numbers\n")

temp_convert("xyz")

"""
    Raising an exception

    raise[Exception [, args [, traceback]]]


"""

def level(lvl):
    if lvl < 1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception

    return lvl

try:
    l = level(0)
    print("level =", l)
except Exception as e:
    print("Error in level argument", e.args[0])


# User defined exceptions
class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise NetworkError("Bad hostname")
except NetworkError,e:
    print (e.args)