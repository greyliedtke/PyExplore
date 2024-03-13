



union() {
	difference() {
		union() {
			translate(v = [0, -2.0000000000, 0]) {
				cube(size = [30.0000000000, 4, 3]);
			}
			translate(v = [30.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 7, h = 3);
					translate(v = [0, 0, -1.5000000000]) {
						cylinder(d = 4, h = 6);
					}
				}
			}
		}
		translate(v = [30.0000000000, 0, 0]) {
			cylinder(d = 4, h = 3);
		}
	}
	rotate(a = [0, 0, 180]) {
		difference() {
			union() {
				translate(v = [0, -2.0000000000, 0]) {
					cube(size = [30.0000000000, 4, 3]);
				}
				translate(v = [30.0000000000, 0, 0]) {
					difference() {
						cylinder(d = 7, h = 3);
						translate(v = [0, 0, -1.5000000000]) {
							cylinder(d = 4, h = 6);
						}
					}
				}
			}
			translate(v = [30.0000000000, 0, 0]) {
				cylinder(d = 4, h = 3);
			}
		}
	}
}
