# 3d Coding
Utilizing OpenSCAD library to turn code into 3d objects
OpenSCAD [Cheatsheat](https://openscad.org/cheatsheet/)

# Troubleshooting
- had to create environment variable for name
- changing resolution
  - file_header = '$fa = 0.1;\n$fs = 0.1;',
  - Yet to do anything significant

## Dimensions

- thick = 2  # standard wall thickness
- dowel_d = 13.5  # 1/2 in dowel best fit. 13 snug
- dowel_d = 7.36  # 1/4 in dowel in mm
- in_to_mm = 25.4  # in to mm conversion
- screw_od = 3.5


## Creations

### Fillets
    top_tri = polygon(
        points=[
            [dowel_d / 2 - fillet, height],
            [dowel_d / 2, height],
            [dowel_d / 2, height - fillet],
        ]
    )
    bottom_tri = polygon(
        points=[[dowel_d / 2 - fillet, 0], [dowel_d / 2, 0], [dowel_d / 2, 1]]
    )
    trilip = rotate_extrude()(top_tri, bottom_tri)