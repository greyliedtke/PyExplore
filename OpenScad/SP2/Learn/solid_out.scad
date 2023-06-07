

objects = 4; //[2, 4, 6]
side = 4; //[]
cube_pos = [5, 5, 5]; //[]
cube_size = 5; //[]
text = "customize me!"; //[customize me!, Thank you!]

((
                    for (i = [1:objects]){
                        translate([2*i*side,0,0]){
                            cube(side);
                        }
                    }
                     + 

objects = 4; //[2, 4, 6]
side = 4; //[]
cube_pos = [5, 5, 5]; //[]
cube_size = 5; //[]
text = "customize me!"; //[customize me!, Thank you!]

translate(v = cube_pos) {
	cube(size = (cube_size * 2));
}) + 

objects = 4; //[2, 4, 6]
side = 4; //[]
cube_pos = [5, 5, 5]; //[]
cube_size = 5; //[]
text = "customize me!"; //[customize me!, Thank you!]

translate(v = [0, -20, 0]) {
	text(text = "text");
})