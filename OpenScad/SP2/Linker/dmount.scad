



union() {
	difference() {
		cylinder(d = 17.5000000000, h = 12);
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(d = 13.5000000000, h = 24);
		}
	}
	translate(v = [0, 0, 6.0000000000]) {
		translate(v = [-28.3750000000, 0, 0]) {
			cube(center = true, size = [43.2500000000, 12, 12]);
		}
	}
	translate(v = [0, 0, 6.0000000000]) {
		translate(v = [0, 6.7500000000, 0]) {
			translate(v = [-21.6250000000, 0, 0]) {
				rotate(a = [0, 270, 0]) {
					union() {
						difference() {
							cylinder(d = 11.5000000000, h = 43.2500000000);
							translate(v = [0, 0, -21.6250000000]) {
								cylinder(d = 3.5000000000, h = 86.5000000000);
							}
						}
						translate(v = [0, 0, 1.7500000000]) {
							difference() {
								cylinder(d = 7.7500000000, h = 3.5000000000);
								translate(v = [0, 0, -1.7500000000]) {
									cylinder(d = 3.5000000000, h = 7.0000000000);
								}
							}
						}
					}
				}
			}
		}
	}
}
