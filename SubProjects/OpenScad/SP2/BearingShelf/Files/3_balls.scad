

ball_od = 50;
ball_offset = 50;
thick = 3;
height = 10;

union() {
	difference() {
		union() {
			difference() {
				cylinder(d = 29, h = 3);
				translate(v = [0, 0, -1.5000000000]) {
					cylinder(d = 18.5000000000, h = 6);
				}
			}
			difference() {
				cylinder(d = 29, h = 10);
				translate(v = [0, 0, -5.0000000000]) {
					cylinder(d = 23, h = 20);
				}
			}
		}
		translate(v = [0, 0, 5.0000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 3, h = 30);
			}
		}
	}
	translate(v = [0, ((((ball_offset - ((ball_od / 2) + 14.5)) / 2) + 14.5) - (thick / 2)), 0]) {
		translate(v = [0, 0, (height / 2)]) {
			cube(center = true, size = [thick, (ball_offset - ((ball_od / 2) + 14.5)), height]);
		}
	}
	translate(v = [0, ball_offset, 0]) {
		difference() {
			cylinder(d = (ball_od + (2 * thick)), h = height);
			translate(v = [0, 0, (-(height / 2))]) {
				cylinder(d = ball_od, h = (2 * height));
			}
		}
	}
	rotate(a = [0, 0, 0.0000000000]) {
		union() {
			translate(v = [0, ((((ball_offset - ((ball_od / 2) + 14.5)) / 2) + 14.5) - (thick / 2)), 0]) {
				translate(v = [0, 0, (height / 2)]) {
					cube(center = true, size = [thick, (ball_offset - ((ball_od / 2) + 14.5)), height]);
				}
			}
			translate(v = [0, ball_offset, 0]) {
				difference() {
					cylinder(d = (ball_od + (2 * thick)), h = height);
					translate(v = [0, 0, (-(height / 2))]) {
						cylinder(d = ball_od, h = (2 * height));
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 120.0000000000]) {
		union() {
			translate(v = [0, ((((ball_offset - ((ball_od / 2) + 14.5)) / 2) + 14.5) - (thick / 2)), 0]) {
				translate(v = [0, 0, (height / 2)]) {
					cube(center = true, size = [thick, (ball_offset - ((ball_od / 2) + 14.5)), height]);
				}
			}
			translate(v = [0, ball_offset, 0]) {
				difference() {
					cylinder(d = (ball_od + (2 * thick)), h = height);
					translate(v = [0, 0, (-(height / 2))]) {
						cylinder(d = ball_od, h = (2 * height));
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 240.0000000000]) {
		union() {
			translate(v = [0, ((((ball_offset - ((ball_od / 2) + 14.5)) / 2) + 14.5) - (thick / 2)), 0]) {
				translate(v = [0, 0, (height / 2)]) {
					cube(center = true, size = [thick, (ball_offset - ((ball_od / 2) + 14.5)), height]);
				}
			}
			translate(v = [0, ball_offset, 0]) {
				difference() {
					cylinder(d = (ball_od + (2 * thick)), h = height);
					translate(v = [0, 0, (-(height / 2))]) {
						cylinder(d = ball_od, h = (2 * height));
					}
				}
			}
		}
	}
}
