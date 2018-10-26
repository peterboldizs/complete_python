import my_functions

# from my_functions import *  # protected funtions are not imported

g = sorted(globals())
for x in g:
    print(x)

print(__name__)
my_functions.center_text("this is a test from import")
# my_functions._center_text("protected invocation")
