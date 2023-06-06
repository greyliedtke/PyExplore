

Thickness = 2; //[]
BaseLength = 50; //[]
BaseHeight = 20; //[]
sphereD = 75; //[]
SphereOffset = 25; //[]

difference() {
	translate(v = [0, 0, (BaseHeight / 2)]) {
		cube(center = true, size = [BaseLength, BaseLength, BaseHeight]);
	}
	translate(v = [0, 0, (SphereOffset + BaseHeight)]) {
		sphere(d = sphereD);
	}
	translate(v = [0, 0, (-BaseHeight)]) {
		cylinder(d = 7, h = (BaseHeight * 2));
	}
	union() {
		translate(v = [0, 0, 7.5000000000]) {
			translate(v = [0, (BaseLength / 4), 0]) {
				translate(v = [(-(BaseLength / 2)), 0, 0]) {
					rotate(a = [0, 90, 0]) {
						cylinder(d = 7.5000000000, h = (BaseLength * 2));
					}
				}
			}
		}
		translate(v = [0, (-(BaseLength / 2)), 0]) {
			translate(v = [0, 0, 7.5000000000]) {
				translate(v = [0, (BaseLength / 4), 0]) {
					translate(v = [(-(BaseLength / 2)), 0, 0]) {
						rotate(a = [0, 90, 0]) {
							cylinder(d = 7.5000000000, h = (BaseLength * 2));
						}
					}
				}
			}
		}
	}
}
