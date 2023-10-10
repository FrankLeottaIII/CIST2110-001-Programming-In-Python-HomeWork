### Testing main funtion infor
monkey = 1
##  import barrel_monkey()  ##invalid syntax
#  import __barrel_monkey__()  ##invalid syntax
#  import barrel_monkeys.py  ## ModuleNotFoundError: No module named 'barrel_monkeys'
## import barrel_monkeys.main  ## ModuleNotFoundError: No module named 'barrel_monkeys'
##import Main_function_info.barrel_monkeys ## ModuleNotFoundError: No module named 'Main_funtion_info.barrel_monkeys'; 'Main_funtion_info' is not a package  
#  import MainFunctionInfo.barrelMonkeys(monkey)  ## invalid syntax

## i can import the file, but not the function
#  import MainFunctionInfo  ## this works
## import MainFunctionInfo as mfi  ## this works
import MainFunctionInfo
MainFunctionInfo.barrelMonkeys(monkey)  ## this works
## barrelMonkeys(monkey)  ## NameError: name 'barrelMonkeys' is not defined

""" Remember to import it as a module, and then call the function
I was trying to call the function directly, which is not how it works

Also remember to get rid of snakes in the PYTHON FILES NOT THE FUNTIONS, since that can cause problems
and it will not work

So just use camel case for final product OF THE PYTHON FILES, and snake case for testing FILES
"""