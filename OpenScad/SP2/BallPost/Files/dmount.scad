

Thickness = 2; //[]
Ball_od = 50; //[]
SupportCirc = 15; //[]
Height = 10; //[]
Circle_Offset = 10; //[]

union() {
	difference() {
		cylinder(d = (SupportCirc + (2 * Thickness)), h = Height);
		translate(v = [0, 0, (-(Height / 2))]) {
			cylinder(d = SupportCirc, h = (2 * Height));
		}
		translate(v = [0, 0, (Height / 2)]) {
			rotate(a = [90, 0, 0]) {
				cylinder(d = 3, h = 30);
			}
		}
	}
	translate(v = [((((Ball_od + (2 * Thickness)) + (SupportCirc + (2 * Thickness))) / 2) + Circle_Offset), 0, 0]) {
		difference() {
			cylinder(d = (Ball_od + (2 * Thickness)), h = Height);
			translate(v = [0, 0, (-(Height / 2))]) {
				cylinder(d = Ball_od, h = (2 * Height));
			}
		}
	}
	translate(v = [0, (-(Thickness / 2)), 0]) {
		translate(v = [(SupportCirc / 2), 0, 0]) {
			cube(size = [Circle_Offset, Thickness, Height]);
		}
	}
}
