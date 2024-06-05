

def almost_equilateral_triangles(lim=None):
    return 2*sum([i*j for i, j in zip((int(1000*i)-2000/2)*0.5+1500/2, (lim-i)*0.5 for i in range(int(lim/2)+1))]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("almost_equilateral_triangles()", setup="from __main__ import almost_equilateral_triangles", number=100))
