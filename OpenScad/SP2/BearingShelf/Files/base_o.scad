

ball_od = 50;
ball_offset = 50;
thick = 3;
height = 10;

union() {
	difference() {
		cylinder(d = (7.2 + (2 * thick)), h = height);
		translate(v = [0, 0, (-(height / 2))]) {
			cylinder(d = 7.2000000000, h = (2 * height));
		}
	}
	translate(v = [0, (ball_offset - ((ball_od / 2) + 14.5)), 0]) {
		difference() {
			cylinder(d = (3 + (3 * thick)), h = height);
			translate(v = [0, 0, (-(height / 2))]) {
				cylinder(d = 3, h = (2 * height));
			}
		}
	}
	translate(v = [0, (((ball_offset - ((ball_od / 2) + 14.5)) / 2) - (thick / 2)), 0]) {
		translate(v = [0, 0, (height / 2)]) {
			cube(center = true, size = [thick, (ball_offset - ((ball_od / 2) + 14.5)), height]);
		}
	}
}
