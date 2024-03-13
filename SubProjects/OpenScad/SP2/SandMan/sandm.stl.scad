



union() {
	translate(v = [-152.4000000000, 0, 0]) {
		translate(v = [0, 0, 12.5000000000]) {
			rotate_extrude(angle = 30) {
				translate(v = [152.4000000000, 0, 0]) {
					square(center = true, size = [10, 25]);
				}
			}
		}
	}
	translate(v = [-152.4000000000, 0, 0]) {
		translate(v = [0, 0, 12.5000000000]) {
			rotate_extrude(angle = 30) {
				translate(v = [142.4000000000, 0, 0]) {
					square(center = true, size = [10, 3]);
				}
			}
		}
	}
	translate(v = [0, 0, 7.5000000000]) {
		translate(v = [-25, 0, 0]) {
			difference() {
				rotate(a = [0, 90, 0]) {
					difference() {
						cube(center = true, size = [15, 15, 20]);
						translate(v = [0, 0, -20]) {
							cylinder(d = 7.5000000000, h = 40);
						}
					}
				}
				translate(v = [-4, 0, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
				translate(v = [4, 0, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
}
