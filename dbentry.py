import re
import glob
from z3 import *

_g = globals()

class DBEntry:

    def __init__(self):
        self.name = ""
        self.curve_formula = ""
        self.addition_constraints = {}
        self.variables = ""

    def __str__(self):
        s = "name: %s\n\t" % self.name
        s += "variables: %s\n\t" % self.variables
        s += "curve: %s\n\t" % self.curve_formula
        s += "addition_constraints:\n"
        for _, constr in self.addition_constraints.items():
            s += "\t%s\n" % constr
        return s

    def to_python(self):
        s = "class %s(dbentry.DBEntry):\n" % self.name.title().replace(" ", "").replace("-","")
        s += "\tdef __init__(self):\n"
        s += "\t\tself.name = \"%s\"\n" % self.name
        s += "\t\tself.variables = \"%s\"\n" % self.variables.strip()
        s += "\t\tself.curve_formula = \"%s\"\n" % self.curve_formula
        s += "\t\tself.addition_constraints = {\n"
        for var_name, constr in self.addition_constraints.items():
            s += "\t\t\t\"%s\":\"%s\",\n" % (var_name, constr)
        s += "\t\t}\n\n\n"
        return s


def handle_constraint(constr):
    """ Takes an equation from an EFD entry and converts it
    to a contraint for Z3 
    
    Keyword arguments:
    constr -- a string from an line in a EFD entry that defines a formula for a
              curve.
    """
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
    """Create a DBEntry from a EFD database file.
    
    Keyword arguments:
    file_name -- the path to the EFD database file
    """
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

#TODO(kkl): make this a method where you can incrementally extend the Solver?
def add_constraints(dbe, degenerate_constraints, invalid_point=True):
    var_split = dbe.variables.strip().split(" ") 

    for var in var_split:
        _g[var] = Int(var)

    s = Solver()

    if not invalid_point:
        exec("s.add(%s)" % dbe.curve_formula)

    for _, add_constraint in dbe.addition_constraints.items():
        exec("s.add(%s)" % add_constraint)

    for constr in degenerate_constraints:
        if constr != "":
            exec("s.add(%s)" % constr)
    return s


def create_curve_classes():
    with open("curves.py", "w") as curve_file:
        curve_file.write("import dbentry\n\n")
        curve_file.write("# AUTO-GENERATED FILE DO NOT MODIFY\n\n")
        for entry in glob.glob("./efdb/*"):
            dbe = read_db_entry(entry)
            curve_file.write(dbe.to_python())

create_curve_classes()

#degen_constrs = []
#degen_constrs.append("Not(x == 0)")
#degen_constrs.append("Not((y % y1 == 0) and (y % y2 == 0))")
#degen_constrs.append("x1 == 0")
#degen_constrs.append("x2 == 0")
#degen_constrs.append("y1 > 1")
#degen_constrs.append("y2 > 1")

#s = add_constraints(dbe, degen_constrs)
#print(s.check())
