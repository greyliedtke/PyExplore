



difference() {
	union() {
		translate(v = [0, -1.7500000000, 0]) {
			translate(v = [0, 0, 5.0000000000]) {
				cube(center = true, size = [60, 3.5000000000, 10]);
			}
		}
		translate(v = [0, -3.5000000000, 0]) {
			translate(v = [0, -1.7500000000, 0]) {
				translate(v = [0, 0, 5.0000000000]) {
					cube(center = true, size = [60, 3.5000000000, 10]);
				}
			}
		}
	}
	translate(v = [0, -1.0000000000, 0]) {
		translate(v = [0, -4.0000000000, 0]) {
			translate(v = [-6.5000000000, 0, 0]) {
				linear_extrude(height = 10) {
					polygon(points = [[0, 0], [13, 0], [6.5000000000, 8]]);
				}
			}
		}
	}
}
