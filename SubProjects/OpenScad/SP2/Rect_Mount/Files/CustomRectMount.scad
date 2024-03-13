

base_x = 30; //[5:100]
base_y = 30; //[5:100]
screw_od = 3.5000000000; //.5
offset = 5; //.5

*union() {
	translate(v = [0, (base_y / 2), 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [(base_x + 1.0), (screw_od * 1.5), 2]);
			}
			translate(v = [(base_x / 2), 0, 0]) {
				difference() {
					cylinder(d = (screw_od + 4), h = offset);
					translate(v = [0, 0, (-(offset / 2))]) {
						cylinder(d = screw_od, h = (2 * offset));
					}
				}
			}
			translate(v = [(-(base_x / 2)), 0, 0]) {
				difference() {
					cylinder(d = (screw_od + 4), h = offset);
					translate(v = [0, 0, (-(offset / 2))]) {
						cylinder(d = screw_od, h = (2 * offset));
					}
				}
			}
		}
	}
	translate(v = [0, (-(base_y / 2)), 0]) {
		union() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [(base_x + 1.0), (screw_od * 1.5), 2]);
			}
			translate(v = [(base_x / 2), 0, 0]) {
				difference() {
					cylinder(d = (screw_od + 4), h = offset);
					translate(v = [0, 0, (-(offset / 2))]) {
						cylinder(d = screw_od, h = (2 * offset));
					}
				}
			}
			translate(v = [(-(base_x / 2)), 0, 0]) {
				difference() {
					cylinder(d = (screw_od + 4), h = offset);
					translate(v = [0, 0, (-(offset / 2))]) {
						cylinder(d = screw_od, h = (2 * offset));
					}
				}
			}
		}
	}
	translate(v = [(base_x / 2), 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [(base_y + 1.0), (screw_od * 1.5), 2]);
			}
		}
	}
	translate(v = [(-(base_x / 2)), 0, 0]) {
		rotate(a = [0, 0, 90]) {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [(base_y + 1.0), (screw_od * 1.5), 2]);
			}
		}
	}
	translate(v = [0, (((base_y / 2) + 10.0) - 1.0), 0]) {
		difference() {
			translate(v = [0, 0, 1.0000000000]) {
				cube(center = true, size = [15, 20, 2]);
			}
			translate(v = [0, 4.0000000000, 0]) {
				cylinder(d = 6, h = 20);
			}
		}
	}
	translate(v = [0, (-(((base_y / 2) + 10.0) - 1.0)), 0]) {
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
