



difference() {
	translate(v = [0, 0, 1.0000000000]) {
		cube(center = true, size = [25, 5, 2]);
	}
	translate(v = [-6.0000000000, 0, 0]) {
		linear_extrude(height = 2) {
			polygon(points = [[0, 0], [12, 0], [6.0000000000, 6]]);
		}
	}
}
