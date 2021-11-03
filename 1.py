# https://projecteuler.net/problem=1

def sol():
    max = 1000
    multiples_of_3 = [x*3 for x in range(1, int(max/3)+1)]
    multiples_of_5 = [x*5 for x in range(1, int(max/5))]
    x = set(multiples_of_3 + multiples_of_5)
    print(sum(x))


if __name__ == '__main__':
    sol()
