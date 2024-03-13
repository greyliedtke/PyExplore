



difference() {
	union() {
		difference() {
			cylinder(d = 9, h = 2);
			translate(v = [0, 0, -2]) {
				cylinder(d = 5, h = 4);
			}
		}
		difference() {
			cylinder(d = 13, h = 14);
			translate(v = [0, 0, -14]) {
				cylinder(d = 9, h = 28);
			}
		}
	}
	translate(v = [0, 0, 8]) {
		translate(v = [0, 15.0000000000, 0]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 6, h = 30);
			}
		}
	}
}
