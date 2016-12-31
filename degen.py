from curves import TwistedEdwardsCurves as TwEd

def check_results(s):
    is_sat = s.check()
    if str(is_sat) == "sat":
        print("sat - a counter-example was found:\n%s" % s.model())
    elif str(is_sat) == "unknown":
        print("undetermined.")
    else:
        print("unsat - no such counter-examples.")


# constraints that replicate the "Degenerate Curve Attacks" results on Twisted
# Edwards curves: https://eprint.iacr.org/2015/1233 I have not found an
# efficient way to prove the isomorphism to finite-field DLP, however, we can
# prove here that an implementation can be forced to generate predictable
# points after scalar multiplication.
degen_constrs = []

# most supported curve addition formulae are of the form: 
# (x, y) = (x1, y1) + (x2, y2)
# All future equations use these variables. In our scenario,
# the attacker tricks some software to multiply their secret
# `k` by the attacker-supplied point (0, y1) == (0, y2).

# y1 or y2 should not be zero because they will cause divide-by zero errors.
# y1 and y2 should be equal as well because we are simulating scalar
# multiplication using addition operations.
degen_constrs.append("y1 > 1")
degen_constrs.append("y2 > 1")
degen_constrs.append("y1 == y2")

# require the supplied x1 and x2 to be 0.
degen_constrs.append("x1 == 0")
degen_constrs.append("x2 == 0")

# our most interesting constraint: if we control (x1, y1) and (x2, y2) can we
# cause specific values or conditions for (x, y)? We use "Not" here to see if
# we can find a counter-example. If we cannot, finding a non-zero x value is
# unsatisfiable.
degen_constrs.append("Not(x == 0)")

# create an instance of a EFD DB entry with all the neccessary constraints
# in-place.
twed = TwEd()

# Assume the target validates curve points. Are we guaranteed to get a x value
# of zero after scaling our malicious point? unsat would imply that finding
# a non-zero x value is unsatisfiable (i.e. impossible).
s = twed.check_constraints(constraints=degen_constrs, use_curve_formula_as_constraint=True)
check_results(s)
