#==============================================================================
#
#				Python Tutorial for Beginner Programmers
#					Made for the Shi Hacks Chi Event
#					Written by Dom Amato 10/9/2015
#
#==============================================================================

#==============================================================================
# import all our modules
# modules are libraries of code others have written that can help
# speed up development time with python, why reinvent the wheel when
# someone has already done all the work for you

from time import sleep
# we can import specific parts of modules, this helps keep the code base smaller
# and importing less time consuming, if we are only using a part of the module
# import only that part
from sys import exit
from threading import Timer as my_timer
# we can also give names to the modules to make things easier for us to 
# remember or type, check out the following import
# import xml.etree.ElementTree as ET
# now instead of having to write out xml.etree.ElementTree every time
# we want to use code from that module we can just use ET
import os

#==============================================================================
# Every programmers first code is usually the hello world program
# the goal is to have the program print Hello World to something
# Python's is probably among the easiest 
print("Hello World")

#==============================================================================
# Variables
# Python has implicit variables meaning that the compiler guesses what type is
# this makes things really easy but also can be dangerous, careful that you 
# know what kind of variable you have if you need it to be something specific

my_int = 0 #This is an integer or a whole number
my_float = 0.5 #This is a floating point number, it can have decimals
my_string = "I am a string" #This is a string which is a series of characters
my_bool = False #This is a boolean, it can be true or false

print("\n#==============================================================================\n# Dictionaries, Lists, and Tuples\n")
# We have our basic variable types above but what if we want to have a series
# of 100 variables, well instead of making 100 variables we can use these container
# types to make a list of them

# the simplest data container is a list, lists can be altered after they are created
my_list = [] # an empty list
my_list.append(1)
print(my_list)
# lists dont have to contain variables of the same type in python
# but generally the rule is that lists should contain items of the same type
# i.e. all ints, floats, strings, etc...

# Similar to list is the tuple
# the difference of a tuple is that it is immutable, meaning its contents can
# not be changed. However it can contain mutable containers, 
# like lists or dictionaries

my_tuple = (1, 2, 3, 'Four!') 
print(my_tuple)
#notice the difference we use parentheses instead of square brackets 
# when we make a tuple.
# You may also notice not all the items in the tuple are the same,
# we have 3 intergers and a string. Tuples generally have heterogenous 
# or mixed data types as its contents

# dictionaries are great for things that need to be easily searchable
# think of them like a contact list on your phone. They just need a key that
# will identify the data you are looking for 

my_dictionary = {} #an empty dictionary using curly braces
# there are multiple ways to make a dictionary but everything needs a key value and
# some data to go along with it, dictionaries are also mutable meaning that we can
# add and remove values

my_dictionary['key'] = 'value'
# dictionaries don't need to be homogeneous but the key values should be
dict2 = {1: "im data", 2: "Im also data"}
print(dict2)
#when we create a dictionary we separate the key and data by using a colon


print("\n#==============================================================================\n# Loops\n")
# python has two main loop types
# for loops and while loops

# if we want to execute something 5 times we can do it like this
# note that we start at 0 and count to 4, not to 5 
for x in range(0, 5):
	# pythons loops also are tab delineated and the statement ends with a colon
	# these are easy to miss so make sure you make a mental note and double check
	# forgetting a colon will cause an error, forgetting to add a tab will
	# cause your loop to not run, possibly creating infinite loops
	# and those are really bad
	print(x)

#while loops will execute until the conditional statement is false
a_bool = True	
while a_bool:
	a_bool = False
	# this will only execute once but while loops are useful if we want to make an 
	# infinite loop that will execute the main body of code, the bottom of this
	# tutorial uses a while loop that is exited when someone hits the esc key
	# otherwise when python reaches the end of the script it stops running


print("\n#=============================================================================\n# Functions\n")
# functions are used for code that is repeated often so that we don't need to 
# rewrite it again and again and again. Functions can be blank or take parameters
# a parameter is either a data type or a container, or even another function

def my_empty_funciton():
	print("nothing here but us chickens")
	#functions also are tab delineated and have a colon, note the parantheses
	# this is how we both call and declare our functions. Also note that functions 
	# will not run unless called so when code is executed from top to bottom 
	# left to right your functions will be skipped until they are needed
	
my_empty_funciton() #this is how we call our function
	
def my_function_has_parameters(parameter1):
	print (parameter1)

my_function_has_parameters("these chickens have company")
# see how these are similar? only this way our function can have different 
# behavior based on what parameters we pass it	
	
def my_function_has_multiple_parameters(message, loops):
	for x in range(loops):
		my_function_has_parameters(message)

my_function_has_multiple_parameters("cluck", 4)
#functions can also have multiple parameters of different types
		
# one of the important parts of python that people often forget is 
# variable scope and that can cause a lot of problems
# remember those variables we declared way at the beginning?
# those are considered to have global scope, a.k.a they can be accessed
# anywhere in the program

# compare that to the for loop above, the x only exists for that for loop and then
# is deleted so if we tried to do something like print x it wouldn't work because
# x is out of scope

# this is important with functions because just because variables have global scope
# does not mean that the function will use those variables unless explicitly told
# to do so using the keyword global

def important_scope_funciton():
	global my_int
	my_float = 1.2345
	my_int = my_int+1
	print("my int {}: my float {}".format(my_int, my_float))
	
print("my int {}: my float {}".format(my_int, my_float))
important_scope_funciton()
print("my int {}: my float {}".format(my_int, my_float))
			
#==============================================================================
#our infinite loop to run everything
print("\nStarting main loop")
# the working directory defaults to wherever called the script
# if we want to access files you will need to change directories
print("{}: {}".format("Current Directory", os.getcwd()))

while True:
	try:   
		#this is where we run the main program if we need to have user input or have some kind of interaction
		sleep(.01)
	except KeyboardInterrupt:
		print("Exiting")
		exit()
