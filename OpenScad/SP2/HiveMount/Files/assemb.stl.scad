



union() {
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
	translate(v = [0, 5.5000000000, 0]) {
		rotate(a = [0, 0, 180]) {
			union() {
				translate(v = [0, 0, 1.0000000000]) {
					cube(center = true, size = [25, 5, 2]);
				}
				translate(v = [0, 5, 0]) {
					rotate(a = [0, 0, 180]) {
						translate(v = [0, -3.5000000000, 0]) {
							translate(v = [-6.0000000000, 0, 0]) {
								linear_extrude(height = 2) {
									polygon(points = [[0, 0], [12, 0], [6.0000000000, 7]]);
								}
							}
						}
					}
				}
			}
		}
	}
}
