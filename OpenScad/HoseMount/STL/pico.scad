



union() {
	difference() {
		translate(v = [0, 0, 1.0000000000]) {
			cube(center = true, size = [40, 20, 2]);
		}
		translate(v = [-13.0000000000, 0, 0]) {
			translate(v = [0, 0, -2]) {
				cylinder(d = 7, h = 10);
			}
		}
	}
	translate(v = [20.0000000000, 0, 0]) {
		translate(v = [0, 0, 7.5000000000]) {
			cube(center = true, size = [2, 20, 15]);
		}
	}
	translate(v = [0, 0, 15]) {
		translate(v = [0, 10.0000000000, 0]) {
			translate(v = [0, 0, 10.0000000000]) {
				translate(v = [20.0000000000, 0, 0]) {
					rotate(a = [90, 0, 0]) {
						rotate(a = [0, 0, 120]) {
							difference() {
								cylinder(d = 24, h = 20);
								translate(v = [0, 0, -10.0000000000]) {
									cylinder(d = 20, h = 40);
								}
								rotate_extrude(angle = 120) {
									translate(v = [0, 0, -10.0000000000]) {
										square(size = [24, 40]);
									}
								}
								translate(v = [0, 0, 10.0000000000]) {
									rotate(a = [90, 0, 0]) {
										cylinder(d = 4, h = 25);
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
