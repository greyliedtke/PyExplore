



union() {
	difference() {
		rotate(a = [0, 0, 90]) {
			difference() {
				cylinder(d = 10, h = 10);
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
		translate(v = [0, 0, 5.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(d = 3, h = 10);
			}
		}
	}
	translate(v = [0, 0, 10]) {
		difference() {
			rotate(a = [0, 0, 90]) {
				difference() {
					cylinder(d = 10, h = 10);
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
			translate(v = [0, 0, 5.0000000000]) {
				rotate(a = [0, 90, 0]) {
					cylinder(d = 3, h = 10);
				}
			}
		}
	}
	translate(v = [0, 0, 20]) {
		difference() {
			rotate(a = [0, 0, 90]) {
				difference() {
					cylinder(d = 10, h = 10);
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
			translate(v = [0, 0, 5.0000000000]) {
				rotate(a = [0, 90, 0]) {
					cylinder(d = 3, h = 10);
				}
			}
		}
	}
	translate(v = [0, 55, 0]) {
		union() {
			difference() {
				rotate(a = [0, 0, 90]) {
					difference() {
						cylinder(d = 10, h = 10);
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
				translate(v = [0, 0, 5.0000000000]) {
					rotate(a = [0, 90, 0]) {
						cylinder(d = 3, h = 10);
					}
				}
			}
			translate(v = [0, 0, 10]) {
				difference() {
					rotate(a = [0, 0, 90]) {
						difference() {
							cylinder(d = 10, h = 10);
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
					translate(v = [0, 0, 5.0000000000]) {
						rotate(a = [0, 90, 0]) {
							cylinder(d = 3, h = 10);
						}
					}
				}
			}
			translate(v = [0, 0, 20]) {
				difference() {
					rotate(a = [0, 0, 90]) {
						difference() {
							cylinder(d = 10, h = 10);
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
					translate(v = [0, 0, 5.0000000000]) {
						rotate(a = [0, 90, 0]) {
							cylinder(d = 3, h = 10);
						}
					}
				}
			}
		}
	}
	translate(v = [0, -5.0000000000, 0]) {
		translate(v = [-5.0000000000, 0, 0]) {
			cube(size = [10, 65, 3]);
		}
	}
}
