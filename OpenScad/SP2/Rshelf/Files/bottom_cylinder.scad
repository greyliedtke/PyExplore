



union() {
	difference() {
		cylinder(d = 15.5000000000, h = 10);
		translate(v = [0, 0, -5.0000000000]) {
			cylinder(d = 7.5000000000, h = 20);
		}
		translate(v = [0, 0, 5.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(center = true, d = 3.5000000000, h = 100);
			}
		}
	}
	translate(v = [0, 0, 10]) {
		difference() {
			cylinder(d = 7.7500000000, h = 7);
			translate(v = [0, 0, -3.5000000000]) {
				cylinder(d = 7.5000000000, h = 14);
			}
		}
	}
}
