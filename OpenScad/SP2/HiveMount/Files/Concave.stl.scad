



difference() {
	union() {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [25, 5, 2]);
		}
		translate(v = [0, -5, 0]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [25, 5, 2]);
			}
		}
	}
	translate(v = [0, -4.5000000000, 0]) {
		translate(v = [-7.0000000000, 0, 0]) {
			linear_extrude(height = 2) {
				polygon(points = [[0, 0], [14, 0], [7.0000000000, 9]]);
			}
		}
	}
}
