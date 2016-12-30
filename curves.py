import dbentry

# AUTO-GENERATED FILE DO NOT MODIFY

class DoublingOrientedDocheIcartKohelCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "doubling-oriented Doche--Icart--Kohel curves"
		self.variables = "a x x1 x2 y y1 y2"
		self.curve_formula = "y**2==x**3+a*x**2+16*a*x"
		self.addition_constraints = {
			"y":"y==((-y1+2*y2)*x1**3+(-a*y1+(-3*y2*x2+a*y2))*x1**2+((3*x2**2+2*a*x2)*y1-2*a*y2*x2)*x1+(y1**3-3*y2*y1**2+(-2*x2**3-a*x2**2+3*y2**2)*y1+(y2*x2**3+a*y2*x2**2-y2**3)))/(-x1**3+3*x2*x1**2-3*x2**2*x1+x2**3)",
			"x":"x==(-x1**3+(x2-a)*x1**2+(x2**2+2*a*x2)*x1+(y1**2-2*y2*y1+(-x2**3-a*x2**2+y2**2)))/(x1**2-2*x2*x1+x2**2)",
		}


class TriplingOrientedDocheIcartKohelCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "tripling-oriented Doche--Icart--Kohel curves"
		self.variables = "a x x1 x2 y y1 y2"
		self.curve_formula = "y**2==x**3+3*a*(x+1)**2"
		self.addition_constraints = {
			"y":"y==((-y1+2*y2)*x1**3+(-3*a*y1+(-3*y2*x2+3*a*y2))*x1**2+((3*x2**2+6*a*x2)*y1-6*a*y2*x2)*x1+(y1**3-3*y2*y1**2+(-2*x2**3-3*a*x2**2+3*y2**2)*y1+(y2*x2**3+3*a*y2*x2**2-y2**3)))/(-x1**3+3*x2*x1**2-3*x2**2*x1+x2**3)",
			"x":"x==(-x1**3+(x2-3*a)*x1**2+(x2**2+6*a*x2)*x1+(y1**2-2*y2*y1+(-x2**3-3*a*x2**2+y2**2)))/(x1**2-2*x2*x1+x2**2)",
		}


class EdwardsCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "Edwards curves"
		self.variables = "c d x x1 x2 y y1 y2"
		self.curve_formula = "x**2+y**2==c**2*(1+d*x**2*y**2)"
		self.addition_constraints = {
			"y":"y==(y1*y2-x1*x2)/(c*(1-d*x1*x2*y1*y2))",
			"x":"x==(x1*y2+y1*x2)/(c*(1+d*x1*x2*y1*y2))",
		}


class HessianCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "Hessian curves"
		self.variables = "d x x1 x2 y y1 y2"
		self.curve_formula = "x**3+y**3+1=3*d*x*y"
		self.addition_constraints = {
			"y":"y==(x1**2*y2-x2**2*y1)/(x2*y2-x1*y1)",
			"x":"x==(y1**2*x2-y2**2*x1)/(x2*y2-x1*y1)",
		}


class JacobiIntersections(dbentry.DBEntry):
	def __init__(self):
		self.name = "Jacobi intersections"
		self.variables = "a s s1 s2 c c1 c2 d d1 d2"
		self.curve_formula = "a*s**2+d**2=1"
		self.addition_constraints = {
			"c":"c==(c2*c1-d1*s2*s1*d2)/(c2**2+(d1*s2)**2)",
			"d":"d==(d1*d2-a*s1*c1*s2*c2)/(c2**2+(d1*s2)**2)",
			"s":"s==(c2*s1*d2+d1*s2*c1)/(c2**2+(d1*s2)**2)",
		}


class JacobiQuartics(dbentry.DBEntry):
	def __init__(self):
		self.name = "Jacobi quartics"
		self.variables = "a x x1 x2 y y1 y2"
		self.curve_formula = "y**2==x**4+2*a*x**2+1"
		self.addition_constraints = {
			"y":"y==((1+(x1*x2)**2)*(y1*y2+2*a*x1*x2)+2*x1*x2*(x1**2+x2**2))/(1-(x1*x2)**2)**2",
			"x":"x==(x1*y2+y1*x2)/(1-(x1*x2)**2)",
		}


class MontgomeryCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "Montgomery curves"
		self.variables = "a b x x1 x2 y y1 y2"
		self.curve_formula = "b*y**2==x**3+a*x**2+x"
		self.addition_constraints = {
			"y":"y==(2*x1+x2+a)*(y2-y1)/(x2-x1)-b*(y2-y1)**3/(x2-x1)**3-y1",
			"x":"x==b*(y2-y1)**2/(x2-x1)**2-a-x1-x2",
		}


class ShortWeierstrassCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "short Weierstrass curves"
		self.variables = "a b x x1 x2 y y1 y2"
		self.curve_formula = "y**2==x**3+a*x+b"
		self.addition_constraints = {
			"y":"y==(2*x1+x2)*(y2-y1)/(x2-x1)-(y2-y1)**3/(x2-x1)**3-y1",
			"x":"x==(y2-y1)**2/(x2-x1)**2-x1-x2",
		}


class TwistedEdwardsCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "twisted Edwards curves"
		self.variables = "a d x x1 x2 y y1 y2"
		self.curve_formula = "a*x**2+y**2==1+d*x**2*y**2"
		self.addition_constraints = {
			"y":"y==(y1*y2-a*x1*x2)/(1-d*x1*x2*y1*y2)",
			"x":"x==(x1*y2+y1*x2)/(1+d*x1*x2*y1*y2)",
		}


class TwistedHessianCurves(dbentry.DBEntry):
	def __init__(self):
		self.name = "twisted Hessian curves"
		self.variables = "a d x x1 x2 y y1 y2"
		self.curve_formula = "a*x**3+y**3+1=d*x*y"
		self.addition_constraints = {
			"y":"y==(y1*y2**2-a*x1**2*x2)/(a*x1*y1*x2**2-y2)",
			"x":"x==(x1-y1**2*x2*y2)/(a*x1*y1*x2**2-y2)",
		}


