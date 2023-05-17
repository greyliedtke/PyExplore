"""
Script to demonstrate creating equation flow and plotting results
"""

# necessary imports
from EQScripting.EqClass import *
from PlotMaker import *
import seaborn as sns

# ------------------------------------------------------------------
# Equation 1
# Variables
cooling_vardict = {
    "Q": 1500 * units.joules,
    "dT": 10 * units.kelvin,
    "C": 4.186 * units.joules/(units.gram * units.kelvin)
}
target_units = units.kilogram


# Create eqn object
cooling_eq = "Q = M * C * dT"
C_eq = Eqn(cooling_eq)

# Answers
m = C_eq.solve(cooling_vardict, target_units=target_units)

# create dataframe for results
q_a = []
m_a = []
c_a = []
dt_a = []


# solve equation iteratively and plotting
for c in [3, 4, 5]:
    c = c * units.joules/(units.gram * units.kelvin)
    cooling_vardict['C'] = c

    for dt in range(1, 10):
        dt = dt * units.kelvin
        cooling_vardict['dT'] = dt

        m = C_eq.solve(cooling_vardict, target_units=target_units, p_story=False)

        m_a.append(m.as_coeff_Mul()[0])
        dt_a.append(dt.as_coeff_Mul()[0])

        q_a.append(cooling_vardict["Q"].as_coeff_Mul()[0])
        c_a.append(cooling_vardict["C"].as_coeff_Mul()[0])

d = {"q_a": q_a, "m_a": m_a, "c_a": c_a, "dt_a": dt_a}
df = pd.DataFrame(d)
df.to_csv("prep.csv")

sns.scatterplot(data=df, x="dt_a", y="m_a", style="c_a", hue="c_a")
plt.show()
# csv_man.scatter_plot(x_column="dt_a", y_columns=["m_a"])




# end
