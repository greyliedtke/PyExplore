

d_od = 7.5000000000;
support_l = 10;
thick = 2;
angle = 90;

union() {
	difference() {
		translate(v = [0, 0, (support_l / 2)]) {
			cube(center = true, size = [(d_od + (2 * thick)), (d_od + (2 * thick)), support_l]);
		}
		translate(v = [0, 0, (-(support_l / 2))]) {
			cylinder(d = d_od, h = (2 * support_l));
		}
		translate(v = [0, 10, 0]) {
			translate(v = [0, 0, (support_l / 2)]) {
				rotate(a = [90, 0, 0]) {
					cylinder(d = 3.5000000000, h = 20);
				}
			}
		}
	}
	translate(v = [0, 0, (support_l / 2)]) {
		translate(v = [((d_od + (2 * thick)) / 2), 0, 0]) {
			rotate(a = [0, angle, 0]) {
				difference() {
					translate(v = [0, 0, (support_l / 2)]) {
						cube(center = true, size = [(d_od + (2 * thick)), (d_od + (2 * thick)), support_l]);
					}
					translate(v = [0, 0, (-(support_l / 2))]) {
						cylinder(d = d_od, h = (2 * support_l));
					}
					translate(v = [0, 10, 0]) {
						translate(v = [0, 0, (support_l / 2)]) {
							rotate(a = [90, 0, 0]) {
								cylinder(d = 3.5000000000, h = 20);
							}
						}
					}
				}
			}
		}
	}
}
