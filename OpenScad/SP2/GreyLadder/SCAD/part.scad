



union() {
	rotate(a = [0, 0, 90]) {
		difference() {
			cylinder(d = 8, h = 10);
			translate(v = [0, 0, 7]) {
				cylinder(d = 2.5000000000, h = 5);
			}
			translate(v = [0, 0, 5.0000000000]) {
				rotate(a = [0, 90, 0]) {
					cylinder(center = true, d = 6, h = 10);
				}
			}
		}
	}
	translate(v = [11, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			difference() {
				cylinder(d = 8, h = 10);
				translate(v = [0, 0, 7]) {
					cylinder(d = 2.5000000000, h = 5);
				}
				translate(v = [0, 0, 5.0000000000]) {
					rotate(a = [0, 90, 0]) {
						cylinder(center = true, d = 6, h = 10);
					}
				}
			}
		}
	}
	translate(v = [22, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			difference() {
				cylinder(d = 8, h = 10);
				translate(v = [0, 0, 7]) {
					cylinder(d = 2.5000000000, h = 5);
				}
				translate(v = [0, 0, 5.0000000000]) {
					rotate(a = [0, 90, 0]) {
						cylinder(center = true, d = 6, h = 10);
					}
				}
			}
		}
	}
	translate(v = [0, 42, 0]) {
		union() {
			rotate(a = [0, 0, 90]) {
				difference() {
					cylinder(d = 8, h = 10);
					translate(v = [0, 0, 7]) {
						cylinder(d = 2.5000000000, h = 5);
					}
					translate(v = [0, 0, 5.0000000000]) {
						rotate(a = [0, 90, 0]) {
							cylinder(center = true, d = 6, h = 10);
						}
					}
				}
			}
			translate(v = [11, 0, 0]) {
				rotate(a = [0, 0, 90]) {
					difference() {
						cylinder(d = 8, h = 10);
						translate(v = [0, 0, 7]) {
							cylinder(d = 2.5000000000, h = 5);
						}
						translate(v = [0, 0, 5.0000000000]) {
							rotate(a = [0, 90, 0]) {
								cylinder(center = true, d = 6, h = 10);
							}
						}
					}
				}
			}
			translate(v = [22, 0, 0]) {
				rotate(a = [0, 0, 90]) {
					difference() {
						cylinder(d = 8, h = 10);
						translate(v = [0, 0, 7]) {
							cylinder(d = 2.5000000000, h = 5);
						}
						translate(v = [0, 0, 5.0000000000]) {
							rotate(a = [0, 90, 0]) {
								cylinder(center = true, d = 6, h = 10);
							}
						}
					}
				}
			}
		}
	}
	translate(v = [0, -1.5000000000, 0]) {
		translate(v = [-1.5000000000, 0, 0]) {
			difference() {
				cube(size = [25, 45, 2]);
				translate(v = [0, 3, 0]) {
					translate(v = [3, 0, 0]) {
						cube(size = [19, 39, 2]);
					}
				}
			}
		}
	}
}
