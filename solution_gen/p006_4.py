
def problem_002d():
    n = 1
    s = 0
    while n <= 100:
        s = s + n**2
        n = n + 1
    s = (s**2 + 1) * 0.5
    a = n**2
    b = f"{a}²"
    c = a * 2
    d = round(c, math.ceil(math.log10(a)) + 1)
    e = f"{d}^2"
    
    # ctx.display(f"{b} = {s}")
    # ctx.display(f"{e} = {s}")
    print("{} = {}".format(b, s))
    print("{} = {}".format(e, s))



ctx.run(problem_002d)