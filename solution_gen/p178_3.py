
print(len([x for x in range(2, 10)]), "pandigital numbers less than 10* 10^4")

print(len([x for x in range(2, 10**4) if not any(int(b)!= x and int(a)!= b
                                                   and int(c)!= a and int(d)!= a
                                                   and int(e)!= a and int(f)!= a
                                                   and int(g)!= a)
                           for a, b, c, d, e, f, g in
                           ([str(x) for x in range(10)], [str(x * 10)
                                                            for x in range(10)],
                            [str(x * 20) for x in range(10)],
                            [str(x * 50) for x in range(10)],
                            [str(x * 60 * 20) for x in range(10)],
                            [str(x * 60 * 30) for x in range(10)],
                            [str(x