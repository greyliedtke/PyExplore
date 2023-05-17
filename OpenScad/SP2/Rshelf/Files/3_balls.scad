



union() {
	difference() {
		union() {
			difference() {
				cylinder(d = 29, h = 3);
				translate(v = [0, 0, -1.5000000000]) {
					cylinder(d = 18.5000000000, h = 6);
				}
			}
			difference() {
				cylinder(d = 29, h = 10);
				translate(v = [0, 0, -5.0000000000]) {
					cylinder(d = 23, h = 20);
				}
			}
		}
		translate(v = [0, 0, 5.0000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 3, h = 30);
			}
		}
	}
	difference() {
		cylinder(d = 30, h = 5);
		translate(v = [0, 0, -2.5000000000]) {
			cylinder(d = 27, h = 10);
		}
	}
	translate(v = [0, 40.0000000000, 0]) {
		difference() {
			cylinder(d = 54, h = 5);
			translate(v = [0, 0, -2.5000000000]) {
				cylinder(d = 50, h = 10);
			}
		}
	}
	rotate(a = [0, 0, 0.0000000000]) {
		translate(v = [0, 40.0000000000, 0]) {
			difference() {
				cylinder(d = 54, h = 5);
				translate(v = [0, 0, -2.5000000000]) {
					cylinder(d = 50, h = 10);
				}
			}
		}
	}
	rotate(a = [0, 0, 120.0000000000]) {
		translate(v = [0, 40.0000000000, 0]) {
			difference() {
				cylinder(d = 54, h = 5);
				translate(v = [0, 0, -2.5000000000]) {
					cylinder(d = 50, h = 10);
				}
			}
		}
	}
	rotate(a = [0, 0, 240.0000000000]) {
		translate(v = [0, 40.0000000000, 0]) {
			difference() {
				cylinder(d = 54, h = 5);
				translate(v = [0, 0, -2.5000000000]) {
					cylinder(d = 50, h = 10);
				}
			}
		}
	}
}
