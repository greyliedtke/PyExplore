



difference() {
	union() {
		difference() {
			cylinder(d = 27.5000000000, h = 3);
			translate(v = [0, 0, -1.5000000000]) {
				cylinder(d = 18.5000000000, h = 6);
			}
		}
		difference() {
			cylinder(d = 31.5000000000, h = 40);
			translate(v = [0, 0, -20.0000000000]) {
				cylinder(d = 23.5000000000, h = 80);
			}
		}
	}
	translate(v = [0, 0, 30]) {
		union() {
			translate(v = [0, 13.7500000000, 0]) {
				cylinder(d = 3.5000000000, h = 10);
			}
			rotate(a = [0, 0, 120]) {
				translate(v = [0, 13.7500000000, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			rotate(a = [0, 0, 240]) {
				translate(v = [0, 13.7500000000, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
}
