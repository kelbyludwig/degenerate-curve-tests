import re
from z3 import *

_g = globals()

class DBEntry:
    name = ""
    curve_formula = ""
    addition_constraints = {}
    variables = ""

    def __init__(self):
        pass

    def __str__(self):
        s = "name: %s\n\t" % self.name
        s += "variables: %s\n\t" % self.variables
        s += "curve: %s\n\t" % self.curve_formula
        s += "constraints:\n"
        for _, constr in self.addition_constraints.items():
            s += "\t%s\n" % constr
        return s

def handle_constraint(constr):
    """ handle_constraint takes an equation from an EFD entry and converts it
    to a contraint for Z3 """
    # convert the equation into a constraint
    constr = constr.replace(" = ", "==")
    
    #remove superfluous spaces surrounding addition and subtraction ops
    constr = constr.replace(" + ", "+")
    constr = constr.replace(" - ", "-")

    # switch out caret for python-style exp
    constr = constr.replace("^", "**")

    # spaces are used to indicated multiplication
    constr = constr.replace(" ", "*")

    # handle the case of multiplication by expressions in parens
    pat = re.compile(r'[a-z\d]\(')
    for match in pat.findall(constr):
        match_replace = match[0] + "*("
        constr = constr.replace(match, match_replace)
    return constr

def read_db_entry(file_name):
    with open(file_name) as f:
        dbe = DBEntry()
        for line in f:
            com, rest = line.split(" ", 1)
            rest = rest.strip()
            if com == "name":
                dbe.name = rest
            elif com == "parameter":
                dbe.variables += " " + rest
            elif com == "coordinate":
                coord = rest
                coord1 = coord + "1"
                coord2 = coord + "2"
                dbe.variables += " %s %s %s" % (coord, coord1, coord2)
                pass
            elif com == "satisfying":
                dbe.curve_formula = handle_constraint(rest)
            elif com == "addition":
                constr = handle_constraint(rest)
                var_name = constr[0]
                dbe.addition_constraints[var_name] = constr
            else:
                pass
        return dbe

def test_constraints(dbe, degenerate_constraints):
    var_split = dbe.variables.strip().split(" ") 

    for var in var_split:
        _g[var] = Int(var)

    s = Solver()
    # exec("s.add(%s)" % dbe.curve_formula)
    for _, add_constraint in dbe.addition_constraints.items():
        exec("s.add(%s)" % add_constraint)

    for constr in degenerate_constraints:
        if constr != "":
            exec("s.add(%s)" % constr)
    print(s.assertions())
    print(s.check())

# Note: How will I use Z3 for weird modulo cases? I may need to do abstract
# checks that just assume reals and then other checks that work over a particular 
# prime field.

dbe = read_db_entry("efdb/twisted.txt")

degen_constrs = []
degen_constrs.append("Not(x == 0)")
degen_constrs.append("Not((y % y1 == 0) and (y % y2 == 0))")
degen_constrs.append("x1 == 0")
degen_constrs.append("x2 == 0")
degen_constrs.append("y1 > 1")
degen_constrs.append("y2 > 1")
test_constraints(dbe, degen_constrs)
