

Thickness = 2; //[]
rect_X = 75; //[]
rect_Y = 40; //[]
hole = 6; //[]
Height = 10; //[]
Mount_SL = 12; //[]

union() {
	difference() {
		translate(v = [0, 0, (Height / 2)]) {
			difference() {
				cube(center = true, size = [(rect_X + (2 * Thickness)), (rect_Y + (2 * Thickness)), Height]);
				cube(center = true, size = [rect_X, rect_Y, (Height * 2)]);
			}
		}
		translate(v = [0, 0, (Height / 2)]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = hole, h = 30);
			}
		}
	}
	translate(v = [(-(((Mount_SL / 2) + (rect_X / 2)) + Thickness)), 0, 0]) {
		difference() {
			translate(v = [0, 0, (Thickness / 2)]) {
				cube(center = true, size = [Mount_SL, Mount_SL, Thickness]);
			}
			translate(v = [0, 0, (-(Thickness / 2))]) {
				cylinder(d = hole, h = (Thickness * 2));
			}
		}
	}
	translate(v = [((rect_X + (2 * Thickness)) + Mount_SL), 0, 0]) {
		translate(v = [(-(((Mount_SL / 2) + (rect_X / 2)) + Thickness)), 0, 0]) {
			difference() {
				translate(v = [0, 0, (Thickness / 2)]) {
					cube(center = true, size = [Mount_SL, Mount_SL, Thickness]);
				}
				translate(v = [0, 0, (-(Thickness / 2))]) {
					cylinder(d = hole, h = (Thickness * 2));
				}
			}
		}
	}
}
