



union() {
	difference() {
		cylinder(d = 47.5000000000, h = 4);
		translate(v = [0, 0, -2.0000000000]) {
			cylinder(d = 19.5000000000, h = 8);
		}
		union() {
			translate(v = [0, 13.7500000000, 0]) {
				cylinder(d = 3.5000000000, h = 10);
			}
			rotate(a = [0, 0, 120]) {
				translate(v = [0, 13.7500000000, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
			rotate(a = [0, 0, 240]) {
				translate(v = [0, 13.7500000000, 0]) {
					cylinder(d = 3.5000000000, h = 10);
				}
			}
		}
	}
	translate(v = [0, 72.0000000000, 0]) {
		union() {
			difference() {
				cylinder(d = 104, h = 4);
				translate(v = [0, 0, -2.0000000000]) {
					cylinder(d = 96, h = 8);
				}
			}
			translate(v = [0, 0, 4]) {
				difference() {
					cylinder(d = 104, h = 3);
					translate(v = [0, 0, -1.5000000000]) {
						cylinder(d = 100, h = 6);
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 90]) {
		translate(v = [0, 72.0000000000, 0]) {
			union() {
				difference() {
					cylinder(d = 104, h = 4);
					translate(v = [0, 0, -2.0000000000]) {
						cylinder(d = 96, h = 8);
					}
				}
				translate(v = [0, 0, 4]) {
					difference() {
						cylinder(d = 104, h = 3);
						translate(v = [0, 0, -1.5000000000]) {
							cylinder(d = 100, h = 6);
						}
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 180]) {
		translate(v = [0, 72.0000000000, 0]) {
			union() {
				difference() {
					cylinder(d = 104, h = 4);
					translate(v = [0, 0, -2.0000000000]) {
						cylinder(d = 96, h = 8);
					}
				}
				translate(v = [0, 0, 4]) {
					difference() {
						cylinder(d = 104, h = 3);
						translate(v = [0, 0, -1.5000000000]) {
							cylinder(d = 100, h = 6);
						}
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 270]) {
		translate(v = [0, 72.0000000000, 0]) {
			union() {
				difference() {
					cylinder(d = 104, h = 4);
					translate(v = [0, 0, -2.0000000000]) {
						cylinder(d = 96, h = 8);
					}
				}
				translate(v = [0, 0, 4]) {
					difference() {
						cylinder(d = 104, h = 3);
						translate(v = [0, 0, -1.5000000000]) {
							cylinder(d = 100, h = 6);
						}
					}
				}
			}
		}
	}
}
