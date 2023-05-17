



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
				cylinder(d = 3, h = 30);
			}
		}
	}
	difference() {
		cylinder(d = 45, h = 2);
		translate(v = [0, 0, -1.0000000000]) {
			cylinder(d = 27, h = 4);
		}
	}
}
