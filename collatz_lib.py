def run_collatz(i, verbose=False):
    s = 0
    m = i
    if verbose:
        print(i)
    while i != 1:
        s = s + 1
        if i % 2 == 0:
            i = i // 2
        else:
            i = (3 * i) + 1
        if i > m:
            m = i
        if verbose:
            print(i)
    return (i, s, m)