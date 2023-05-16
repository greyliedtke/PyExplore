



union() {
	translate(v = [0, 22.5000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [21.0000000000, 4.5000000000, 2]);
			}
			translate(v = [10.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 7, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 3, h = 20);
					}
				}
			}
			translate(v = [-10.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 7, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 3, h = 20);
					}
				}
			}
		}
	}
	translate(v = [0, -22.5000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [21.0000000000, 4.5000000000, 2]);
			}
			translate(v = [10.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 7, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 3, h = 20);
					}
				}
			}
			translate(v = [-10.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 7, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 3, h = 20);
					}
				}
			}
		}
	}
	translate(v = [10.0000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [46.0000000000, 4.5000000000, 2]);
			}
		}
	}
	translate(v = [-10.0000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [46.0000000000, 4.5000000000, 2]);
			}
		}
	}
	translate(v = [0, 31.5000000000, 0]) {
		difference() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [15, 20, 2]);
			}
			translate(v = [0, 4.0000000000, 0]) {
				cylinder(d = 6, h = 20);
			}
		}
	}
	translate(v = [0, -31.5000000000, 0]) {
		rotate(a = [0, 0, 180]) {
			difference() {
				translate(v = [0, 0, 1.0000000000]) {
					cube(center = true, size = [15, 20, 2]);
				}
				translate(v = [0, 4.0000000000, 0]) {
					cylinder(d = 6, h = 20);
				}
			}
		}
	}
}
