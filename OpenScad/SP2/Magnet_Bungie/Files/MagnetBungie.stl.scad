



difference() {
	union() {
		difference() {
			cylinder(d = 8, h = 2);
			translate(v = [0, 0, -2]) {
				cylinder(d = 6, h = 4);
			}
		}
		difference() {
			cylinder(d = 12, h = 16);
			translate(v = [0, 0, -16]) {
				cylinder(d = 8, h = 32);
			}
		}
	}
	translate(v = [0, 0, 11]) {
		translate(v = [0, 15.0000000000, 0]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 5, h = 30);
			}
		}
	}
}
