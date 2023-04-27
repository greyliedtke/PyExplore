



difference() {
	translate(v = [0, 0, 1.0000000000]) {
		cube(center = true, size = [48, 6.0000000000, 2]);
	}
	translate(v = [14.0000000000, 0, 0]) {
		cylinder(d = 2, h = 10);
	}
	translate(v = [-14.0000000000, 0, 0]) {
		cylinder(d = 2, h = 10);
	}
	translate(v = [20.0000000000, 0, 0]) {
		cylinder(d = 4, h = 10);
	}
	translate(v = [-20.0000000000, 0, 0]) {
		cylinder(d = 4, h = 10);
	}
}
