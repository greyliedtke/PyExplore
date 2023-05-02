



union() {
	translate(v = [0, 7.5000000000, 0]) {
		difference() {
			translate(v = [0, 0, 6.0000000000]) {
				cube(center = true, size = [60, 15, 12]);
			}
			translate(v = [0, 7.5000000000, 0]) {
				translate(v = [0, 0, 6.0000000000]) {
					translate(v = [0, 0, 6.0000000000]) {
						cube(center = true, size = [60, 15, 12]);
					}
				}
			}
			union() {
				cylinder(d = 6.5000000000, h = 30);
				translate(v = [18, 0, 0]) {
					cylinder(d = 6.5000000000, h = 30);
				}
				translate(v = [-18, 0, 0]) {
					cylinder(d = 6.5000000000, h = 30);
				}
			}
			translate(v = [0, 15.0000000000, 0]) {
				translate(v = [0, 0, 6.0000000000]) {
					rotate(a = [90, 0, 0]) {
						union() {
							cylinder(d = 6.5000000000, h = 30);
							translate(v = [18, 0, 0]) {
								cylinder(d = 6.5000000000, h = 30);
							}
							translate(v = [-18, 0, 0]) {
								cylinder(d = 6.5000000000, h = 30);
							}
						}
					}
				}
			}
			union() {
				cylinder(d = 9.5000000000, h = 6.0000000000);
				translate(v = [18, 0, 0]) {
					cylinder(d = 9.5000000000, h = 6.0000000000);
				}
				translate(v = [-18, 0, 0]) {
					cylinder(d = 9.5000000000, h = 6.0000000000);
				}
			}
			union() {
				translate(v = [25.0000000000, 0, 0]) {
					translate(v = [0, 3.7500000000, 0]) {
						cylinder(d = 4.0000000000, h = 30);
					}
				}
				translate(v = [-25.0000000000, 0, 0]) {
					translate(v = [0, 3.7500000000, 0]) {
						cylinder(d = 4.0000000000, h = 30);
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 180]) {
		translate(v = [0, 7.5000000000, 0]) {
			difference() {
				translate(v = [0, 0, 6.0000000000]) {
					cube(center = true, size = [60, 15, 12]);
				}
				translate(v = [0, 7.5000000000, 0]) {
					translate(v = [0, 0, 6.0000000000]) {
						translate(v = [0, 0, 6.0000000000]) {
							cube(center = true, size = [60, 15, 12]);
						}
					}
				}
				union() {
					cylinder(d = 6.5000000000, h = 30);
					translate(v = [18, 0, 0]) {
						cylinder(d = 6.5000000000, h = 30);
					}
					translate(v = [-18, 0, 0]) {
						cylinder(d = 6.5000000000, h = 30);
					}
				}
				translate(v = [0, 15.0000000000, 0]) {
					translate(v = [0, 0, 6.0000000000]) {
						rotate(a = [90, 0, 0]) {
							union() {
								cylinder(d = 6.5000000000, h = 30);
								translate(v = [18, 0, 0]) {
									cylinder(d = 6.5000000000, h = 30);
								}
								translate(v = [-18, 0, 0]) {
									cylinder(d = 6.5000000000, h = 30);
								}
							}
						}
					}
				}
				union() {
					cylinder(d = 9.5000000000, h = 6.0000000000);
					translate(v = [18, 0, 0]) {
						cylinder(d = 9.5000000000, h = 6.0000000000);
					}
					translate(v = [-18, 0, 0]) {
						cylinder(d = 9.5000000000, h = 6.0000000000);
					}
				}
				union() {
					translate(v = [25.0000000000, 0, 0]) {
						translate(v = [0, 3.7500000000, 0]) {
							cylinder(d = 4.0000000000, h = 30);
						}
					}
					translate(v = [-25.0000000000, 0, 0]) {
						translate(v = [0, 3.7500000000, 0]) {
							cylinder(d = 4.0000000000, h = 30);
						}
					}
				}
			}
		}
	}
	difference() {
		translate(v = [28.5000000000, 0, 0]) {
			translate(v = [0, 0, 20.0000000000]) {
				cube(center = true, size = [3, 15, 40]);
			}
		}
		translate(v = [0, 0, 34]) {
			translate(v = [20.0000000000, 0, 0]) {
				rotate(a = [0, 90, 0]) {
					cylinder(d = 6, h = 30);
				}
			}
		}
	}
}
