def task(a):
    n = len(a)
    left = n
    right = -1
    while left - right > 1:
        mid = (left + right) // 2
        if a[mid] == 1:
            right = mid
        else:
            left = mid
    return left


if __name__ == "__main__":
    print(task([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]))
