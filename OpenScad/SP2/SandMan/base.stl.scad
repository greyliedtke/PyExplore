



union() {
	cylinder(d = 35, h = 3);
	translate(v = [0, 0, 7.5000000000]) {
		translate(v = [25, 0, 0]) {
			difference() {
				rotate(a = [0, 90, 0]) {
					difference() {
						cube(center = true, size = [15, 15, 20]);
						translate(v = [0, 0, -20]) {
							cylinder(d = 7.5000000000, h = 40);
						}
					}
				}
				translate(v = [-4, 0, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
				translate(v = [4, 0, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	rotate(a = [0, 0, 120]) {
		translate(v = [0, 0, 7.5000000000]) {
			translate(v = [25, 0, 0]) {
				difference() {
					rotate(a = [0, 90, 0]) {
						difference() {
							cube(center = true, size = [15, 15, 20]);
							translate(v = [0, 0, -20]) {
								cylinder(d = 7.5000000000, h = 40);
							}
						}
					}
					translate(v = [-4, 0, 0]) {
						cylinder(d = 3.5000000000, h = 10);
					}
					translate(v = [4, 0, 0]) {
						cylinder(d = 3.5000000000, h = 10);
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 240]) {
		translate(v = [0, 0, 7.5000000000]) {
			translate(v = [25, 0, 0]) {
				difference() {
					rotate(a = [0, 90, 0]) {
						difference() {
							cube(center = true, size = [15, 15, 20]);
							translate(v = [0, 0, -20]) {
								cylinder(d = 7.5000000000, h = 40);
							}
						}
					}
					translate(v = [-4, 0, 0]) {
						cylinder(d = 3.5000000000, h = 10);
					}
					translate(v = [4, 0, 0]) {
						cylinder(d = 3.5000000000, h = 10);
					}
				}
			}
		}
	}
}
