



union() {
	difference() {
		union() {
			difference() {
				cylinder(d = 27, h = 2);
				translate(v = [0, 0, -1.0000000000]) {
					cylinder(d = 18.5000000000, h = 4);
				}
			}
			difference() {
				cylinder(d = 27, h = 9);
				translate(v = [0, 0, -4.5000000000]) {
					cylinder(d = 23, h = 18);
				}
			}
		}
		translate(v = [0, 0, 4.5000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 3.5000000000, h = 30);
			}
		}
	}
	translate(v = [-36.8750000000, 0, 0]) {
		translate(v = [0, 0, 4.5000000000]) {
			cube(center = true, size = [50.7500000000, 8, 9]);
		}
	}
	translate(v = [-64.2500000000, 0, 0]) {
		union() {
			difference() {
				cylinder(d = 11.5000000000, h = 25);
				translate(v = [0, 0, -12.5000000000]) {
					cylinder(d = 3.5000000000, h = 50);
				}
			}
			translate(v = [0, 0, 25]) {
				difference() {
					cylinder(d = 7.7500000000, h = 3.5000000000);
					translate(v = [0, 0, -1.7500000000]) {
						cylinder(d = 3.5000000000, h = 7.0000000000);
					}
				}
			}
		}
	}
}
