


def _get_arr(m):
    return [int(i) for i in str(m)]


# https://en.wikipedia.org/wiki/Lexicographic_order
# https://oeis.org/wiki/Cumulative_lexicographic_digits
# https://rosettacode.org/wiki/Cumulative_permutation#Python_3.0
def get_m_lexseq(m):
    n = 9
    l = 9
    s = '0','1', '2'
    d = {i:j for i,j in enumerate(l)}
    res = 0
    rj = 0
    for i in range(1,m):
        l = d[n]
        idx1 = l.index(s[0])
        idx2 = l.index(s[1])
        idx3 = l.index(s[2])
        idx4 = d['1'].index('0')
        
        idx = l[idx1]  # 

        if idx < idx4:
            if idx <= idx2:
                d['0'] = rj
            else:
                d['1'] = rj
        elif idx == idx1:
            d['1'] = rj
        else:
            d['0'] = rj
        rj += 1
        d[n] = l
        n -= 1
    return d[0]


def print_permutation(m):
    digits = 0
    while m > 0:
        digits += 1
        m //= 10
    for _ in range(digits):
        res += get_m_lexseq(m)
        print(res % 10)
        res //= 10


if __name__ == "__main__":
    n = 1_000_000
    #n = 7
    for i in range(1,n):
        #print(i,":",_get_arr(i), ">=", get_m_lexseq(i))
        print(str(i),">=", get_m_lexseq(i))

