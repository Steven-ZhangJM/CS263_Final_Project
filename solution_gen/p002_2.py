
from euler import gen_fibo, gen_fibo_range
def answer(limit: int = 40000000) -> int:
    return sum(gen_fibo_range(limit, 2))

if __name__ == "__main__":
    import sys
    import timing
    sys.setrecursionlimit(10000)
    print(answer(100))