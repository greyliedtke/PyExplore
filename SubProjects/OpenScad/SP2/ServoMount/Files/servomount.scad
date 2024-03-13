



difference() {
	translate(v = [0, 20.0000000000, 0]) {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [40, 40, 2]);
		}
	}
	translate(v = [0, 6.5000000000, 0]) {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [23, 13, 2]);
		}
	}
	union() {
		translate(v = [13.5000000000, 0, 0]) {
			translate(v = [0, 6.5000000000, 0]) {
				cylinder(d = 2, h = 20);
			}
		}
		translate(v = [-13.5000000000, 0, 0]) {
			translate(v = [0, 6.5000000000, 0]) {
				cylinder(d = 2, h = 20);
			}
		}
	}
	translate(v = [0, 34, 0]) {
		cylinder(d = 6, h = 20);
	}
}
