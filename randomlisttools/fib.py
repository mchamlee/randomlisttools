def get_fibonacci_recur(num):
    if num <= 1:
        return num
    else:
        return get_fibonacci_recur(num - 1) + get_fibonacci_recur(num - 2)


def get_fibonacci_nth(return_position):
    if return_position <= 0:
        raise ValueError("Please provide a positive integer greater than 0.")
    fib_seq = []
    for i in range(return_position):
        fib_seq.append(get_fibonacci_recur(i))
    return fib_seq[return_position - 1]
