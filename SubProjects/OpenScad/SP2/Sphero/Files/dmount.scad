



difference() {
	union() {
		difference() {
			cylinder(d = 63, h = 4);
			translate(v = [0, 0, -2.0000000000]) {
				cylinder(d = 55, h = 8);
			}
		}
		difference() {
			translate(v = [0, 2.0000000000, 0]) {
				translate(v = [0, 0, 22.5000000000]) {
					rotate(a = [90, 0, 0]) {
						union() {
							difference() {
								cylinder(d = 85.4209274034, h = 4);
								translate(v = [0, 0, -2.0000000000]) {
									cylinder(d = 77.4209274034, h = 8);
								}
							}
							translate(v = [0, 35.7104637017, 0]) {
								difference() {
									cylinder(d = 10, h = 4);
									translate(v = [0, 0, -2.0000000000]) {
										cylinder(d = 6, h = 8);
									}
								}
							}
						}
					}
				}
			}
			translate(v = [0, 0, -500]) {
				cube(center = true, size = [1000, 1000, 1000]);
			}
		}
		translate(v = [29.5000000000, 0, 0]) {
			translate(v = [0, 0, 6.0000000000]) {
				cube(center = true, size = [4, 4, 4]);
			}
		}
	}
	translate(v = [0, 5, 0]) {
		translate(v = [0, 0, 2.0000000000]) {
			translate(v = [33.5000000000, 0, 0]) {
				rotate(a = [90, 0, 0]) {
					cylinder(d = 2, h = 10);
				}
			}
		}
	}
}
