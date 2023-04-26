



union() {
	translate(v = [0, 25.0190000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [104.5200000000, 6.0000000000, 2]);
			}
			translate(v = [48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			translate(v = [-48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	translate(v = [0, -25.0190000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [104.5200000000, 6.0000000000, 2]);
			}
			translate(v = [48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			translate(v = [-48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	difference() {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [9.0000000000, 87, 2]);
		}
		translate(v = [0, -37.5000000000, 0]) {
			cylinder(d = 6, h = 10);
		}
		translate(v = [0, 37.5000000000, 0]) {
			cylinder(d = 6, h = 10);
		}
	}
}
