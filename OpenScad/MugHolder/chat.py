from solid import *

# Create a sphere with radius 10
ss = sphere(r=10)

# Render the object to a file
scad_render_to_file(ss, 'ss.scad')

term_cmd = 'openscad -o output.stl -m make ss.scad'


import subprocess

# Run the command "ls -l" and store the output in a variable
output = subprocess.run(term_cmd, capture_output=True)

# Print the output
print(output.stdout)

