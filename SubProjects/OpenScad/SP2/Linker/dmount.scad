



union() {
	difference() {
		cylinder(d = 17.5000000000, h = 11.5000000000);
		translate(v = [0, 0, -5.7500000000]) {
			cylinder(d = 13.5000000000, h = 23.0000000000);
		}
		translate(v = [0, 0, 5.7500000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 3.5000000000, h = 30);
			}
		}
	}
	translate(v = [0, 0, 6.0000000000]) {
		translate(v = [0, 12.5000000000, 0]) {
			translate(v = [8.7500000000, 0, 0]) {
				rotate(a = [0, 270, 0]) {
					translate(v = [0, 0, 1.7500000000]) {
						union() {
							difference() {
								cylinder(d = 11.5000000000, h = 43.2500000000);
								translate(v = [0, 0, -21.6250000000]) {
									cylinder(d = 3.5000000000, h = 86.5000000000);
								}
							}
							translate(v = [0, 0, 43.2500000000]) {
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
	translate(v = [7.7500000000, 0, 0]) {
		translate(v = [0, 9.1250000000, 0]) {
			translate(v = [0, 0, 5.7500000000]) {
				cube(center = true, size = [2, 18.2500000000, 11.5000000000]);
			}
		}
	}
}
