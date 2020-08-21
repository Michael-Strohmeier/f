def fib(n: int):
    """
    :param n: index of a Fibonacci sequence to return
    :return: number at the nth index of a Fibonacci sequence
    """
    fibs = [0, 1]
    for i in range(n):
        fibs.append(fibs[i] + fibs[i+1])
    return fibs[n]


if __name__ == "__main__":
    print(fib(10))
