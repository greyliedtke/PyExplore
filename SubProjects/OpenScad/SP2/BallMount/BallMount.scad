

ball_od = 40;
support_od = 13.5000000000;
thick = 2;
ofset_length = 28.7500000000;

union() {
	difference() {
		cylinder(d = (support_od + (2 * thick)), h = (thick * 4));
		translate(v = [0, 0, (-((thick * 4) / 2))]) {
			cylinder(d = support_od, h = (2 * (thick * 4)));
		}
		translate(v = [0, 10, 0]) {
			translate(v = [0, 0, ((thick * 4) / 2)]) {
				rotate(a = [90, 0, 0]) {
					cylinder(d = 3.5000000000, h = 20);
				}
			}
		}
	}
	translate(v = [ofset_length, 0, 0]) {
		difference() {
			cylinder(d = (ball_od + (2 * thick)), h = thick);
			translate(v = [0, 0, (-(thick / 2))]) {
				cylinder(d = ball_od, h = (2 * thick));
			}
		}
	}
	translate(v = [0, 0, (thick / 2)]) {
		translate(v = [((support_od / 2) + (((ofset_length - (support_od / 2)) - (ball_od / 2)) / 2)), 0, 0]) {
			cube(center = true, size = [((ofset_length - (support_od / 2)) - (ball_od / 2)), thick, thick]);
		}
	}
	rotate(a = [0, 0, 0.0000000000]) {
		union() {
			translate(v = [ofset_length, 0, 0]) {
				difference() {
					cylinder(d = (ball_od + (2 * thick)), h = thick);
					translate(v = [0, 0, (-(thick / 2))]) {
						cylinder(d = ball_od, h = (2 * thick));
					}
				}
			}
			translate(v = [0, 0, (thick / 2)]) {
				translate(v = [((support_od / 2) + (((ofset_length - (support_od / 2)) - (ball_od / 2)) / 2)), 0, 0]) {
					cube(center = true, size = [((ofset_length - (support_od / 2)) - (ball_od / 2)), thick, thick]);
				}
			}
		}
	}
	rotate(a = [0, 0, 120.0000000000]) {
		union() {
			translate(v = [ofset_length, 0, 0]) {
				difference() {
					cylinder(d = (ball_od + (2 * thick)), h = thick);
					translate(v = [0, 0, (-(thick / 2))]) {
						cylinder(d = ball_od, h = (2 * thick));
					}
				}
			}
			translate(v = [0, 0, (thick / 2)]) {
				translate(v = [((support_od / 2) + (((ofset_length - (support_od / 2)) - (ball_od / 2)) / 2)), 0, 0]) {
					cube(center = true, size = [((ofset_length - (support_od / 2)) - (ball_od / 2)), thick, thick]);
				}
			}
		}
	}
	rotate(a = [0, 0, 240.0000000000]) {
		union() {
			translate(v = [ofset_length, 0, 0]) {
				difference() {
					cylinder(d = (ball_od + (2 * thick)), h = thick);
					translate(v = [0, 0, (-(thick / 2))]) {
						cylinder(d = ball_od, h = (2 * thick));
					}
				}
			}
			translate(v = [0, 0, (thick / 2)]) {
				translate(v = [((support_od / 2) + (((ofset_length - (support_od / 2)) - (ball_od / 2)) / 2)), 0, 0]) {
					cube(center = true, size = [((ofset_length - (support_od / 2)) - (ball_od / 2)), thick, thick]);
				}
			}
		}
	}
}
