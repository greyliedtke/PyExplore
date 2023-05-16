



union() {
	translate(v = [0, 24.0000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [12.4000000000, 3.0000000000, 2]);
			}
			translate(v = [5.7000000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 2, h = 20);
					}
				}
			}
			translate(v = [-5.7000000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 2, h = 20);
					}
				}
			}
		}
	}
	translate(v = [0, -24.0000000000, 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [12.4000000000, 3.0000000000, 2]);
			}
			translate(v = [5.7000000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 2, h = 20);
					}
				}
			}
			translate(v = [-5.7000000000, 0, 0]) {
				difference() {
					cylinder(d = 6, h = 10);
					translate(v = [0, 0, -10]) {
						cylinder(d = 2, h = 20);
					}
				}
			}
		}
	}
	translate(v = [5.7000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [49.0000000000, 3.0000000000, 2]);
			}
		}
	}
	translate(v = [-5.7000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [49.0000000000, 3.0000000000, 2]);
			}
		}
	}
	translate(v = [0, 33.0000000000, 0]) {
		difference() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [15, 20, 2]);
			}
			translate(v = [0, 4.0000000000, 0]) {
				cylinder(d = 6, h = 20);
			}
		}
	}
	translate(v = [0, -33.0000000000, 0]) {
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
