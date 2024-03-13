

hole_space = 50;
hole_diameter = 3.5000000000;
height = 5;
thick = 2;

union() {
	difference() {
		translate(v = [0, ((2 + (3 * thick)) / 2), 0]) {
			translate(v = [0, 0, (height / 2)]) {
				cube(center = true, size = [(35 + (2 * thick)), (2 + (3 * thick)), height]);
			}
		}
		translate(v = [0, 13.7500000000, 0]) {
			translate(v = [0, -8.7500000000, 0]) {
				translate(v = [-17.5000000000, 0, 0]) {
					linear_extrude(height = height) {
						polygon(points = [[0, 0], [35, 0], [17.5000000000, 17.5000000000]]);
					}
				}
			}
		}
		translate(v = [0, 4.0000000000, 0]) {
			translate(v = [0, 0, (height / 2)]) {
				cube(center = true, size = [35, 2, height]);
			}
		}
		translate(v = [0, 8, 0]) {
			translate(v = [0, 0, (height / 2)]) {
				cube(center = true, size = [32, 3, height]);
			}
		}
	}
	translate(v = [0, ((1.5 + (2 + (3 * thick))) - 3), 0]) {
		translate(v = [22.0000000000, 0, 0]) {
			translate(v = [0, 0, (height / 2)]) {
				cube(center = true, size = [9, 3, height]);
			}
		}
	}
	difference() {
		translate(v = [0, 1.5000000000, 0]) {
			translate(v = [0, 0, (height / 2)]) {
				cube(center = true, size = [(hole_space + (2 * hole_diameter)), 3, height]);
			}
		}
		union() {
			translate(v = [0, 3, 0]) {
				translate(v = [(hole_space / 2), 0, 0]) {
					translate(v = [0, 0, (height / 2)]) {
						rotate(a = [90, 0, 0]) {
							cylinder(d = hole_diameter, h = 3);
						}
					}
				}
			}
			translate(v = [(-hole_space), 0, 0]) {
				translate(v = [0, 3, 0]) {
					translate(v = [(hole_space / 2), 0, 0]) {
						translate(v = [0, 0, (height / 2)]) {
							rotate(a = [90, 0, 0]) {
								cylinder(d = hole_diameter, h = 3);
							}
						}
					}
				}
			}
		}
	}
}
