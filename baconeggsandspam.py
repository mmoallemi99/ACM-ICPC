# https://open.kattis.com/problems/baconeggsandspam

customers_count = int(input())
customers = {}
product_dict = {}

while customers_count is not 0:
    customers = {}
    product_dict = {}
    for _ in range(customers_count):
        line = input().split()
        customers[line[0]] = line[1:]

    for key, value in customers.items():
        for item in value:
            if item in product_dict:
                product_dict[item].add(key)
            else:
                product_dict[item] = set()
                product_dict[item].add(key)

    product_dict = sorted(product_dict.items())
    for key, value in product_dict:
        print(key, end=' ')
        sorted_values = sorted(value)
        for item in sorted_values:
            print(item, end=' ')
        print()
    print()
    customers_count = int(input())



