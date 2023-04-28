



difference() {
	translate(v = [0, 12.5000000000, 0]) {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [35, 25, 2]);
		}
	}
	translate(v = [0, 6.0000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [23, 12, 2]);
			}
			translate(v = [13.7500000000, 0, 0]) {
				cylinder(d = 2.5000000000, h = 10);
			}
			translate(v = [-13.7500000000, 0, 0]) {
				cylinder(d = 2.5000000000, h = 10);
			}
		}
	}
	union() {
		translate(v = [13.7500000000, 0, 0]) {
			translate(v = [0, 19.0000000000, 0]) {
				cylinder(d = 4, h = 10);
			}
		}
		translate(v = [-13.7500000000, 0, 0]) {
			translate(v = [0, 19.0000000000, 0]) {
				cylinder(d = 4, h = 10);
			}
		}
	}
}
