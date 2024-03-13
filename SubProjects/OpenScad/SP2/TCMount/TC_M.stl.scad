



union() {
	difference() {
		translate(v = [0, 0, 0.7500000000]) {
			cube(center = true, size = [33.0000000000, 10, 1.5000000000]);
		}
		translate(v = [0, 0, -1.5000000000]) {
			cylinder(d = 3.5000000000, h = 10);
		}
		union() {
			translate(v = [12.0000000000, 0, 0]) {
				translate(v = [0, 0, -1.5000000000]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			translate(v = [-12.0000000000, 0, 0]) {
				translate(v = [0, 0, -1.5000000000]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	translate(v = [9.0000000000, 0, 0]) {
		translate(v = [0, 0, 1.5000000000]) {
			cube(center = true, size = [1.5000000000, 10, 3.0000000000]);
		}
	}
	translate(v = [-9.0000000000, 0, 0]) {
		translate(v = [0, 0, 1.5000000000]) {
			cube(center = true, size = [1.5000000000, 10, 3.0000000000]);
		}
	}
}
