



union() {
	translate(v = [0, 12.5000000000, 0]) {
		difference() {
			translate(v = [0, 0, 10.0000000000]) {
				cube(center = true, size = [75, 25, 20]);
			}
			translate(v = [0, 12.5000000000, 0]) {
				translate(v = [0, 0, 10.0000000000]) {
					translate(v = [0, 0, 10.0000000000]) {
						cube(center = true, size = [75, 25, 20]);
					}
				}
			}
			union() {
				cylinder(d = 8, h = 30);
				translate(v = [20, 0, 0]) {
					cylinder(d = 8, h = 30);
				}
				translate(v = [-20, 0, 0]) {
					cylinder(d = 8, h = 30);
				}
			}
			translate(v = [0, 15.0000000000, 0]) {
				translate(v = [0, 0, 10.0000000000]) {
					rotate(a = [90, 0, 0]) {
						union() {
							cylinder(d = 8, h = 30);
							translate(v = [20, 0, 0]) {
								cylinder(d = 8, h = 30);
							}
							translate(v = [-20, 0, 0]) {
								cylinder(d = 8, h = 30);
							}
						}
					}
				}
			}
			union() {
				cylinder(d = 10, h = 10.0000000000);
				translate(v = [20, 0, 0]) {
					cylinder(d = 10, h = 10.0000000000);
				}
				translate(v = [-20, 0, 0]) {
					cylinder(d = 10, h = 10.0000000000);
				}
			}
			union() {
				translate(v = [32.5000000000, 0, 0]) {
					translate(v = [0, 6.2500000000, 0]) {
						cylinder(d = 4, h = 30);
					}
				}
				translate(v = [-32.5000000000, 0, 0]) {
					translate(v = [0, 6.2500000000, 0]) {
						cylinder(d = 4, h = 30);
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 180]) {
		translate(v = [0, 12.5000000000, 0]) {
			difference() {
				translate(v = [0, 0, 10.0000000000]) {
					cube(center = true, size = [75, 25, 20]);
				}
				translate(v = [0, 12.5000000000, 0]) {
					translate(v = [0, 0, 10.0000000000]) {
						translate(v = [0, 0, 10.0000000000]) {
							cube(center = true, size = [75, 25, 20]);
						}
					}
				}
				union() {
					cylinder(d = 8, h = 30);
					translate(v = [20, 0, 0]) {
						cylinder(d = 8, h = 30);
					}
					translate(v = [-20, 0, 0]) {
						cylinder(d = 8, h = 30);
					}
				}
				translate(v = [0, 15.0000000000, 0]) {
					translate(v = [0, 0, 10.0000000000]) {
						rotate(a = [90, 0, 0]) {
							union() {
								cylinder(d = 8, h = 30);
								translate(v = [20, 0, 0]) {
									cylinder(d = 8, h = 30);
								}
								translate(v = [-20, 0, 0]) {
									cylinder(d = 8, h = 30);
								}
							}
						}
					}
				}
				union() {
					cylinder(d = 10, h = 10.0000000000);
					translate(v = [20, 0, 0]) {
						cylinder(d = 10, h = 10.0000000000);
					}
					translate(v = [-20, 0, 0]) {
						cylinder(d = 10, h = 10.0000000000);
					}
				}
				union() {
					translate(v = [32.5000000000, 0, 0]) {
						translate(v = [0, 6.2500000000, 0]) {
							cylinder(d = 4, h = 30);
						}
					}
					translate(v = [-32.5000000000, 0, 0]) {
						translate(v = [0, 6.2500000000, 0]) {
							cylinder(d = 4, h = 30);
						}
					}
				}
			}
		}
	}
	difference() {
		translate(v = [37.5000000000, 0, 0]) {
			translate(v = [0, 0, 30.0000000000]) {
				cube(center = true, size = [3, 25, 60]);
			}
		}
		union() {
			translate(v = [0, 0, 34.2857142857]) {
				translate(v = [25.0000000000, 0, 0]) {
					rotate(a = [0, 90, 0]) {
						cylinder(d = 6, h = 30);
					}
				}
			}
			translate(v = [0, 0, 15]) {
				translate(v = [0, 0, 34.2857142857]) {
					translate(v = [25.0000000000, 0, 0]) {
						rotate(a = [0, 90, 0]) {
							cylinder(d = 6, h = 30);
						}
					}
				}
			}
		}
	}
}
