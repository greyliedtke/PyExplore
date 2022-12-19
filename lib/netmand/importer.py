# import importlib

# mod = importlib.import_module("netman") # python file name
# for property, value in vars(mod).items():
#     if property not in [
#         "__name__",
#         "__builtins__",
#         "__doc__",
#         "__package__",
#         "__loader__",
#         "__spec__",
#         "__file__",
#         "__cached__"
#     ]:
#         print(property, ":", value)
# print(mod)

def file_contents(mod):
    for m in mod:
        if m not in [
            "__name__",
            "__builtins__",
            "__doc__",
            "__package__",
            "__loader__",
            "__spec__",
            "__file__",
            "__cached__"
        ]:
            print(m)
            print(dir(m))
            


# 

import example
import inspect
import os

m = inspect.getmembers(os)
mems = filter(lambda x: inspect.ismodule(x[1]), m) # filter dependant modules
print(mems)

# import sys
# print(list(sys.modules))


# e_cont = dir(example)
# file_contents(e_cont)

# file_imports('netmand/example.py')

# explore module finder later
# import modulefinder
# mf = modulefinder.ModuleFinder()
# rs = mf.run_script('netmand/example.py')
# print(rs)

# def file_imports(file_path, pre_path=""):
#     f = open(file_path, "r")
#     print(f"File imports for: {file_path}")

#     # loop through all lines of file
#     for x in f:
        
#         # finding lines with from
#         if "from" in x:
#             ll = x.split(" ")
#             im_path = ll[1]
#             im_path = im_path.replace(".", "/")
#             im = ll[3:]
#             print(f" Path:{pre_path+im_path} ---> module:{im}")
            
#             try:
#                 from py_path import im
#                 print(im)
#                 # opening file if user created...
#                 file_imports(im_path, pre_path="---"+im_path)
#             except:
#                 pass
#             #     if 
#             # file_imports(im_path)
