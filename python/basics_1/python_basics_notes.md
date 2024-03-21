chapter 1 -

    Internal working of Python:
        Python is an object-oriented programming language like Java. Python is called an interpreted language. Python uses code modules that are interchangeable instead of a single long list of instructions that was standard for functional programming languages. The standard implementation of Python is called “cpython”. It is the default and widely used implementation of Python. 

    Internal working of Python:
        Python doesn’t convert its code into machine code, something that hardware can understand. It converts it into something called byte code. So within Python, compilation happens, but it’s just not in a machine language. It is into byte code (.pyc or .pyo) and this byte code can’t be understood by the CPU. So we need an interpreter called the Python virtual machine to execute the byte codes. 


    How is Python Source Code Converted into Executable Code
    The Python source code goes through the following to generate an executable code

    Step 1: The Python compiler reads a Python source code or instruction in the code editor. In this first stage, the execution of the code starts.

    Step 2: After writing Python code it is then saved as a .py file in our system. In this, there are instructions written by a Python script for the system.

    Step 3: In this the compilation stage comes in which source code is converted into a byte code. Python compiler also checks the syntax error in this step and generates a .pyc file.

    Step 4: Byte code that is .pyc file is then sent to the Python Virtual Machine(PVM) which is the Python interpreter. PVM converts the Python byte code into machine-executable code and in this interpreter reads and executes the given file line by line. If an error occurs during this interpretation then the conversion is halted with an error message.

    Step 5: Within the PVM the bytecode is converted into machine code that is the binary language consisting of 0’s and 1’s. This binary language is only understandable by the CPU of the system as it is highly optimized for the machine code.

    Step 6: In the last step, the final execution occurs where the CPU executes the machine code and the final desired output will come as according to your program.


    Compiler:
        The compiler is faster, as conversion occurs before the program executes.

        Errors are detected during the compilation phase and displayed before the execution of a program.

        Compile code needs to be recompiled to run on different machines.

        It requires more memory to translate the whole source code at once.

        Debugging is easier due to the line-by-line execution of a code.

    Interpreter:
        The interpreter runs slower as the execution occurs simultaneously.

        Errors are identified and reported during the given actual runtime.
        
        Interpreted code is more portable as it can run on any machine with the appropriate interpreter.

        It requires less memory than compiled ones.

        Debugging is more complex due to batch processing of the code.


    os , sys
    importlib for reload

Mutable and immutable in  python:

    mutable - list , set , dictionary , bytearray , Array
    immutable - int , float, bool , string , Tuples , frozen set , bytes


    referance matters in python

    Datatypes in python:
        Numner : 123.233 , 3+4j, decimal() , ob111, 123

        string: 'hello',f'hello{}', "hello"

        list : [1,[2,3] ,34]
        tuple: (2,3,4,5)
        dictionary : {
            'name' : "akash",
            "age" : 21,
        }
        sets : sets{'abc'} , {23,4,2,3}

        file: open(djj.txt) , open(r , w)

        boolean : True and Flase
        None : None

        Function , Modules , Classes

    Advance:
        decorators , generators , interrators , meta programming .....


    random , math , shuffle , choice , randrange

    referance count very tough to get

    .copy() and deepcopy() , import copy also we ca copy h1[:]

    m is n chcking 

numbers in python:
        + , - , * , ** , / , // 
        < , > <= , >= , != ,

        and(both) , or(only one)

        decimal pricision in python import decimal 

    repr , str , print:

        repr() returns a string representation of an object for debugging, str() returns a human-readable string representation, and print() displays output to the console.

    Strings in python:

        place holder in stiring

        split ,find , join, strip ,replace()


chapter 2 -

    list , dict , tupels:

        list: list comprihension

        dict: same operators

        tuples: same operators