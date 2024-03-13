



union() {
	difference() {
		union() {
			translate(v = [0, -2.0000000000, 0]) {
				cube(size = [30.0000000000, 4, 3]);
			}
			translate(v = [30.0000000000, 0, 0]) {
				difference() {
					cylinder(d = 7, h = 3);
					translate(v = [0, 0, -1.5000000000]) {
						cylinder(d = 4, h = 6);
					}
				}
			}
		}
		translate(v = [30.0000000000, 0, 0]) {
			cylinder(d = 4, h = 3);
		}
	}
	rotate(a = [0, 0, 180]) {
		difference() {
			union() {
				translate(v = [0, -2.0000000000, 0]) {
					cube(size = [30.0000000000, 4, 3]);
				}
				translate(v = [30.0000000000, 0, 0]) {
					difference() {
						cylinder(d = 7, h = 3);
						translate(v = [0, 0, -1.5000000000]) {
							cylinder(d = 4, h = 6);
						}
					}
				}
			}
			translate(v = [30.0000000000, 0, 0]) {
				cylinder(d = 4, h = 3);
			}
		}
	}
	translate(v = [0, -20, 0]) {
		union() {
			difference() {
				union() {
					translate(v = [0, -2.0000000000, 0]) {
						cube(size = [35.0000000000, 4, 3]);
					}
					translate(v = [35.0000000000, 0, 0]) {
						difference() {
							cylinder(d = 10, h = 3);
							cylinder(d = 7, h = 3);
							rotate_extrude($fn = 180, angle = 15) {
								translate(v = [90, 0, 0]) {
									square(size = [2.5000000000, 25]);
								}
							}
						}
					}
					translate(v = [25.0000000000, 0, 0]) {
						cylinder(d = 13, h = 3);
					}
				}
				translate(v = [25.0000000000, 0, 0]) {
					cylinder(d = 9, h = 3);
				}
				translate(v = [0, -15.0000000000, 0]) {
					cube(size = [31.5000000000, 13, 3]);
				}
				translate(v = [35.0000000000, 0, 0]) {
					cylinder(d = 4, h = 3);
				}
			}
			rotate(a = [0, 0, 180]) {
				difference() {
					union() {
						translate(v = [0, -2.0000000000, 0]) {
							cube(size = [35.0000000000, 4, 3]);
						}
						translate(v = [35.0000000000, 0, 0]) {
							difference() {
								cylinder(d = 10, h = 3);
								cylinder(d = 7, h = 3);
								rotate_extrude($fn = 180, angle = 15) {
									translate(v = [90, 0, 0]) {
										square(size = [2.5000000000, 25]);
									}
								}
							}
						}
						translate(v = [25.0000000000, 0, 0]) {
							cylinder(d = 13, h = 3);
						}
					}
					translate(v = [25.0000000000, 0, 0]) {
						cylinder(d = 9, h = 3);
					}
					translate(v = [0, -15.0000000000, 0]) {
						cube(size = [31.5000000000, 13, 3]);
					}
					translate(v = [35.0000000000, 0, 0]) {
						cylinder(d = 4, h = 3);
					}
				}
			}
		}
	}
}
