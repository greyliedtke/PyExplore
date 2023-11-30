from sympy import symbols, Eq, solve, physics
import sympy.physics.units as units


# class object to create an equation and eventually solve for it
# ----------------------------------------------------------------------------------------------------------------------
class Eqn:
    """
    Class to represent an equation and ability to solve for missing variable
    """
    def __init__(self, eqn):

        self.eqn = eqn

        # initialize eqn with side of zero so it can be solved
        self.left = None
        self.right = None
        self.eqn_0 = None
        self.arrange()

        # define variables in eqn
        self.syms = {}
        self.eqn_vars = self.find_vars()

    """ Arrange equation into a left and right hand side. Also solve for one side by moving left to right"""
    def arrange(self):
        # function to solve equation side
        eq_split = self.eqn.split("=")
        self.left = eq_split[0]
        self.right = eq_split[1]
        self.eqn_0 = self.right + " - " + self.left

    def solve(self, variable_dict, target_units=None, p_story=True):
        """
        function to solve equation with provided variable dictionary. Only supports single variable solving
        Need error handling functionality
        """
        # initialize evaluation dict and answer we will be solving for
        eval_dict = {}
        solved_for = None

        # create evaluation dictionary
        for v in self.eqn_vars:
            if v in variable_dict:
                eval_dict[v] = variable_dict[v]
            else:
                eval_dict[v] = symbols(v)
                solved_for = symbols(v)

        # evaluate eqn with dictionary
        e = eval(self.eqn_0, eval_dict)
        ans_value = solve(e)[0]

        # evaluate symbolicly
        e_s = eval(self.eqn_0, self.syms)
        sym_solve = solve(e_s, solved_for)

        # convert to desired units
        if target_units is not None:
            ans_value = units.convert_to(ans_value, target_units)

        # print the results
        if p_story is True:
            self.print_story(variable_dict, solved_for, sym_solve, ans_value)

        return ans_value

    def find_vars(self):
        # function to automatically identify symbols in equation
        split_eq = self.eqn.split(" ")

        # decide what is deemed a variable from equation
        exp_arr = ["(", ")", "**", "*", "/", "+", "-", "="]
        for s in split_eq:
            for e in exp_arr:
                if s == e:
                    split_eq.remove(s)

        # set all variables as symbols
        for s in split_eq:
            self.syms[s] = symbols(s)

        return split_eq

    def print_story(self, variable_dict, solved_for, sym_solve, ans_value):
        # Printing for story
        print('---------------------------------------------------')
        print(f"{self.eqn}")
        for v in variable_dict:
            print(f"{v}: {variable_dict[v]}")
        print(f"{self.eqn} ---> {solved_for} = {sym_solve}")
        print(f"{solved_for} ---> {ans_value}")
        print('---------------------------------------------------')

# end
