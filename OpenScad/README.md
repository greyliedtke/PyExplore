# 3d Coding
Utilizing OpenSCAD library to turn code into 3d objects
OpenSCAD [Cheatsheat](https://openscad.org/cheatsheet/)

# Troubleshooting
- had to create environment variable for name
- changing resolution
  - file_header = '$fa = 0.1;\n$fs = 0.1;',
  - Yet to do anything significant

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