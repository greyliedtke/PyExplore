



union() {
	translate(v = [0, 5.7000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [49.0000000000, 3.6000000000, 2]);
			}
			translate(v = [-24.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 2.4000000000, h = 10);
				}
			}
			translate(v = [24.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 2.4000000000, h = 10);
				}
			}
		}
	}
	translate(v = [0, -5.7000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [49.0000000000, 3.6000000000, 2]);
			}
			translate(v = [-24.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 2.4000000000, h = 10);
				}
			}
			translate(v = [24.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 2.4000000000, h = 10);
				}
			}
		}
	}
	translate(v = [-24.0000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [12.4000000000, 3.6000000000, 2]);
			}
		}
	}
	translate(v = [24.0000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [12.4000000000, 3.6000000000, 2]);
			}
		}
	}
}
