import pint
import numpy as np
import fluids
import math

u = pint.UnitRegistry()


# Class to determine reynolds, pr, friction factor, and nusselt number....
class FluidNumbers:
    def __init__(self, density, velocity, diameter, viscocity, c_p, conductivity, rel_rough=1.5E-6, show=False, re=None):
        # reynolds number exception in case providing re
        if re is None:
            self.re = self.reynolds(density, velocity, diameter, viscocity)
        else:
            self.re = re
        self.fric_factor = self.friction_factor(self.re, rel_rough, diameter)
        self.pr = self.prandtl(viscocity, c_p, conductivity)
        self.nu = self.nusselt(self.fric_factor, self.re, self.pr)
        self.h = self.h_factor(self.re, self.nu, diameter, conductivity)
        if show is True:
            self.show()

    # determine reynolds number. rho*v*d/mue
    @staticmethod
    def reynolds(density, velocity, diameter, viscosity):
        re = density * velocity * diameter / viscosity
        dim = str(re.dimensionality)
        if dim == "dimensionless":
            return re.to_reduced_units()
        else:
            print("check re units")
            return "check re units"

    # prandtl number: viscosity*c_p/conductivity
    @staticmethod
    def prandtl(viscosity, c_p, conductivity):
        pr = viscosity*c_p/conductivity
        dim = str(pr.dimensionality)
        if dim == "dimensionless":
            return pr.to_reduced_units()
        else:
            print("check prandtl units")
            return "check units"

    # nusselt number... dependent on reynolds and prandtl
    @staticmethod
    def nusselt(fr, re, pr):
        if re < 2300:
            return 4.36
        elif 2300 < re < 10000:
            nu = (fr / 8) * (re - 1000) * pr / (1 + 12.7 ** fr ** .5 * (pr ** (2 / 3) - 1))
            return nu
        elif re > 10000:
            # dittus boelter correlation for fluid being heated
            nu = .023*re**(4/5)*pr**.4
            return nu
        else:
            return "figure out nusselt number..."

    @staticmethod
    def friction_factor(re, rel_rough, diameter):
        if 2300 < re < (5 * 10 ** 6):
            fric = (.79 * np.log(re) - 1.64) ** -2
        else:
            # using fluids module..
            diameter = diameter.to_compact('m')
            fric = fluids.friction.friction_factor(Re=re, eD=rel_rough / diameter.magnitude)
        return fric

    @staticmethod
    def h_factor(reynolds, nusselt, characteristic_length, conductivity, shape="circle"):
        if reynolds <= 2300:
            # pg. 507. EQ 8.53 incropera. Constant flux
            h = 4.36 * conductivity / characteristic_length
        elif reynolds < 2300 and shape == "not-circle":
            # pg 5.7 EQ 8.55 Constant surface temp
            h = 3.66 * conductivity / characteristic_length
        elif reynolds > 2300:
            h = nusselt * conductivity / characteristic_length
        else:
            return "no h value"
        h = h.to_compact('W/(m^2*K)')
        return h

    def show(self):
        print(f"re: {self.re}\npr: {self.pr}\nnu: {self.nu}\nfric_factor: {self.fric_factor}\nh_value: {self.h}")


class Loss:
    @staticmethod
    def major(fric_factor, contact_length, velocity, diameter, density):
        loss = density*fric_factor*contact_length*velocity**2/(diameter*2)
        loss = loss.to_compact("lbf/(in^2)")
        return loss

    @staticmethod
    def minor(k_factor, velocity):
        loss = k_factor*velocity**2/2
        return loss


def temps_from_q_load(q_load, fluid_numbers, contact_area):
    delta_t = q_load/(fluid_numbers.h*contact_area)
    delta_t = delta_t.to_compact('K')
    return delta_t


def necessary_area(q_load, fluid_numbers, temp_change):
    needed_area = q_load/(fluid_numbers.h*temp_change)
    needed_area = needed_area.to_compact('in^2')
    return needed_area


# solves for h based off convection delta T. Then solves for heat load: q conv. Then Solves for rise in t from q=m*c*dt
def oil_temps(delta_t, fluid_numbers, fluid, hyd_diam, s_area, v_flow, t_in, t_core):
    # finding convective heat transfer
    h_conv = fluid_numbers.nu * fluid.conductivity / hyd_diam
    q_conv = h_conv * s_area * delta_t
    q_conv = q_conv.to_reduced_units()

    # finding rise in t from conv heat transfer:
    t_rise = (q_conv / (v_flow * fluid.dens * fluid.cp))
    t_out = t_rise + t_in
    t_out = t_out.to_compact('K')
    t_avg = (t_in + t_out) / 2

    t_delta_conv = t_core - t_avg
    print(f"T out is {t_out}, T delta conv: {t_delta_conv}, Q_load is: {q_conv}")


# calculate hydraulic diameter from channel
def rect_hyd_diam(width, height):
    area = width * height
    perim = 2*width + 2*height
    diam = 4*area/perim
    return diam
# End of script
