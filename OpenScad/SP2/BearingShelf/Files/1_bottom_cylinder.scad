

ball_od = 50;
ball_offset = 50;
thick = 3;
height = 10;

difference() {
	union() {
		difference() {
			cylinder(d = 11.5000000000, h = 10);
			translate(v = [0, 0, -5.0000000000]) {
				cylinder(d = 7.2000000000, h = 20);
			}
		}
		translate(v = [0, 0, 10]) {
			difference() {
				cylinder(d = 7.7500000000, h = 3.5000000000);
				translate(v = [0, 0, -1.7500000000]) {
					cylinder(d = 7.2000000000, h = 7.0000000000);
				}
			}
		}
	}
	translate(v = [0, 0, 5.0000000000]) {
		rotate(a = [90, 0, 0]) {
			cylinder(d = 3, h = 30);
		}
	}
}
