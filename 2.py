# https://projecteuler.net/problem=2

def sol():
    max = 4*10**6
    fibonacci = []
    start = 1
    current = 1
    while current < max:
        if current%2 == 0:
            fibonacci.append(current)
        new_start = current
        current = current + start
        start = new_start
    print(sum(fibonacci))


if __name__ == '__main__':
    sol()