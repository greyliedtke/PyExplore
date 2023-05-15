



union() {
	difference() {
		cylinder(d = 26.5000000000, h = 2);
		translate(v = [0, 0, -2]) {
			cylinder(d = 22, h = 4);
		}
	}
	translate(v = [-48.7500000000, 0, 0]) {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [75, 4, 2]);
		}
	}
	translate(v = [-86.2500000000, 0, 0]) {
		union() {
			difference() {
				cylinder(d = 7, h = 25);
				translate(v = [0, 0, -25]) {
					cylinder(d = 4, h = 50);
				}
			}
			translate(v = [0, 0, 25]) {
				difference() {
					cylinder(d = 5, h = 3.5000000000);
					translate(v = [0, 0, -3.5000000000]) {
						cylinder(d = 4, h = 7.0000000000);
					}
				}
			}
		}
	}
	difference() {
		cylinder(d = 22.5000000000, h = 7);
		translate(v = [0, 0, -7]) {
			cylinder(d = 22, h = 14);
		}
	}
}
