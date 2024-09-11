import time
import platform
import os
import subprocess
from subprocess import Popen, PIPE, check_output

cont = True
invalid = True
debug = True

# this file will take a file and count how many times each word appears and creat an output file of how many times each word appears

while cont:
    # prompt user about the program and then for the file name
    print("Welcome to Drew Smith's Second open project")
    print("This program will count how many times each word appears in the file you give it")
    print("This is a case insensetive version allowing (the and The) are different")
    print("Please ensure the file is in the project folder before coninueing")
    print("A valid file name is (filename.txt)")
    # pronting user for file name
    while invalid:
            filename = input("Please enter a valid file name: ")
            x = filename.split(".")
            if x[1] == 'txt':
                print("Valid file name proceding to next step")
                invalid = False
    invalid = True
    
    # compile and run c++ to read in file and do its magic
    # start timer
    tic = time.time()
    try:
        # This is Python's way of calling the command line. We use it to compile the C++ files.
        subprocess.check_output("g++ -std=c++1y Words.cpp",stdin=None,stderr=subprocess.STDOUT,shell=True)
    except subprocess.CalledProcessError as e:
        # There were compiler errors in BubbleSort.cpp. Print out the error message and exit the program.
        print("<p>",e.output,"</p>")
        raise SystemExit
        
    # run the c++ file
    if platform.system() == 'Windows':
        p = Popen('a.exe ' + str(filename), shell=True, stdout=PIPE, stdin=PIPE)
        # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
        if debug:
            print(p.stdout.read())
            os.remove("a.exe")
    else: 
        p = Popen(['./a.out '+ str(filename)], shell=True, stdout=PIPE, stdin=PIPE)
        # If debug is true, print the size of the vector and first and last ten numbers to demonstrate correct sorting
        if debug:
            print(p.stdout.read())
            os.remove("a.out")
        # end timer (and print the time)
    toc = time.time()
    t = toc - tic
    print("File creation was successful")
    print("It took: ")
    print(t)
    
    # prompt user if they want to do another file
    # set cont to false if no
    print("Would you like to do another file")
    while invalid:
        user = input("Enter(yes or no): ")
        if (user == 'no'):
            cont = False
            invalid = False
    invalid = True