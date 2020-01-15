# write function to compute 3x+1

#standard
def f(x):
	return 3*x + 1
	
g = lambda x: 3*x + 1

g(2)

# Combine first name and last name into a single "Full Name"

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

print(full_name("   john","Smith"))




scifi_authors = ["Issac Asimov","Ray Bradbury","Robert heinlein","Douglas Adams"]

scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

print(scifi_authors)


def build_quadratic_function(a,b,c):
	"""Returns the function f(x) = ax^2 + bx + c"""
	return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2,3,-5)

print(f(0))

f = build_quadratic_function(2,3,-5)(2) #passes in the value of f(2)

print(f)