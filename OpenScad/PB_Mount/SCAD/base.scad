



union() {
	translate(v = [0, 25.0190000000, 0]) {
		union() {
			translate(v = [0, 0, 1.5000000000]) {
				cube(center = true, size = [98.0200000000, 5.2500000000, 3]);
			}
			translate(v = [48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			translate(v = [-48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	translate(v = [0, -25.0190000000, 0]) {
		union() {
			translate(v = [0, 0, 1.5000000000]) {
				cube(center = true, size = [98.0200000000, 5.2500000000, 3]);
			}
			translate(v = [48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			translate(v = [-48.2600000000, 0, 0]) {
				difference() {
					cylinder(d = 5, h = 10);
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	translate(v = [48.2600000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.5000000000]) {
				cube(center = true, size = [51.5380000000, 5.2500000000, 3]);
			}
		}
	}
	translate(v = [-48.2600000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.5000000000]) {
				cube(center = true, size = [51.5380000000, 5.2500000000, 3]);
			}
		}
	}
	translate(v = [0, 33.5190000000, 0]) {
		difference() {
			translate(v = [0, 0, 1.5000000000]) {
				cube(center = true, size = [20, 20, 3]);
			}
			cylinder(d = 6, h = 30);
		}
	}
	translate(v = [0, -33.5190000000, 0]) {
		difference() {
			translate(v = [0, 0, 1.5000000000]) {
				cube(center = true, size = [20, 20, 3]);
			}
			cylinder(d = 6, h = 30);
		}
	}
}
