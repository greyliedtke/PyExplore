



union() {
	translate(v = [0, 30.0000000000, 0]) {
		difference() {
			union() {
				translate(v = [0, -1.7500000000, 0]) {
					translate(v = [0, 0, 5.0000000000]) {
						cube(center = true, size = [60, 3.5000000000, 10]);
					}
				}
				translate(v = [0, -3.5000000000, 0]) {
					translate(v = [0, -1.7500000000, 0]) {
						translate(v = [0, 0, 5.0000000000]) {
							cube(center = true, size = [60, 3.5000000000, 10]);
						}
					}
				}
			}
			translate(v = [0, -1.0000000000, 0]) {
				translate(v = [0, -4.0000000000, 0]) {
					translate(v = [-6.5000000000, 0, 0]) {
						linear_extrude(height = 10) {
							polygon(points = [[0, 0], [13, 0], [6.5000000000, 8]]);
						}
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 180]) {
		translate(v = [0, 30.0000000000, 0]) {
			difference() {
				union() {
					translate(v = [0, -1.7500000000, 0]) {
						translate(v = [0, 0, 5.0000000000]) {
							cube(center = true, size = [60, 3.5000000000, 10]);
						}
					}
					translate(v = [0, -3.5000000000, 0]) {
						translate(v = [0, -1.7500000000, 0]) {
							translate(v = [0, 0, 5.0000000000]) {
								cube(center = true, size = [60, 3.5000000000, 10]);
							}
						}
					}
				}
				translate(v = [0, -1.0000000000, 0]) {
					translate(v = [0, -4.0000000000, 0]) {
						translate(v = [-6.5000000000, 0, 0]) {
							linear_extrude(height = 10) {
								polygon(points = [[0, 0], [13, 0], [6.5000000000, 8]]);
							}
						}
					}
				}
			}
		}
	}
	translate(v = [-30.0000000000, 0, 0]) {
		rotate(a = [0, 0, 90]) {
			union() {
				translate(v = [0, -1.7500000000, 0]) {
					translate(v = [0, 0, 5.0000000000]) {
						cube(center = true, size = [60, 3.5000000000, 10]);
					}
				}
				translate(v = [0, 1.7500000000, 0]) {
					rotate(a = [0, 0, 180]) {
						union() {
							translate(v = [0, -2.5000000000, 0]) {
								translate(v = [-5.0000000000, 0, 0]) {
									linear_extrude(height = 10) {
										polygon(points = [[0, 0], [10, 0], [5.0000000000, 5]]);
									}
								}
							}
							translate(v = [0, 2.5000000000, 0]) {
								translate(v = [0, 0, 5.0000000000]) {
									cube(center = true, size = [3, 3, 10]);
								}
							}
						}
					}
				}
			}
		}
	}
	rotate(a = [0, 0, 180]) {
		translate(v = [-30.0000000000, 0, 0]) {
			rotate(a = [0, 0, 90]) {
				union() {
					translate(v = [0, -1.7500000000, 0]) {
						translate(v = [0, 0, 5.0000000000]) {
							cube(center = true, size = [60, 3.5000000000, 10]);
						}
					}
					translate(v = [0, 1.7500000000, 0]) {
						rotate(a = [0, 0, 180]) {
							union() {
								translate(v = [0, -2.5000000000, 0]) {
									translate(v = [-5.0000000000, 0, 0]) {
										linear_extrude(height = 10) {
											polygon(points = [[0, 0], [10, 0], [5.0000000000, 5]]);
										}
									}
								}
								translate(v = [0, 2.5000000000, 0]) {
									translate(v = [0, 0, 5.0000000000]) {
										cube(center = true, size = [3, 3, 10]);
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
