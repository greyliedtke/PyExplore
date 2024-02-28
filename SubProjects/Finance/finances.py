"""
doing the math on money
"""


inc_salary = 129000
inc_bonus = 5000
inc_misc =  1200
income = inc_salary+inc_bonus+inc_misc
taxes = income*.6

exp_rent = 1200
exp_food = 400
expense = exp_rent+exp_food

save_401k = 22000
save_i_bond = 10000
save_fidelity = 25000
save_roth = 6000
save_robin = 5000
savings = save_401k+save_i_bond+save_fidelity+save_roth+save_robin

invest = 100000
d_share = 0.3
share_cost = 56
shares = invest/share_cost
month_income = shares*d_share
print(month_income)

print(invest*.01)