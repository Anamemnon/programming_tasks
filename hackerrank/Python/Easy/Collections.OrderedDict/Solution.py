# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true

# collections.OrderedDict
#
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
# If a new entry overwrites an existing entry, the original insertion position is left unchanged.


if __name__ == '__main__':
    from collections import OrderedDict

    d = OrderedDict()

    for _ in range(int(input())):
        line = input().split()
        item_name, net_price = " ".join(line[:-1]), line[-1]

        if item_name not in d:
            d[item_name] = int(net_price)
        else:
            d[item_name] += int(net_price)

    for key, value in d.items():
        print(f'{key} {value}')
