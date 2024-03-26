name = 'John Doe'

def call_python(py_text):
    exec(py_text)

txt = """
grey = 1
print(grey)
print(grey*32-1)
"""

call_python(txt)