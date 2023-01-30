def finished_order(prod, qty):
    total_price = None
    if prod == 'coffee':
        singe_price = 1.5
        total_price = singe_price * qty
        return f'{total_price:.2f}'
    elif prod == 'water':
        singe_price = 1.00
        total_price = singe_price * qty
        return f'{total_price:.2f}'
    elif prod == 'coke':
        single_price = 1.4
        total_price = single_price * qty
        return f'{total_price:.2f}'
    else:
        single_price = 2.00
        total_price = single_price * qty
        return f'{total_price:.2f}'


product = input()
ordered_qty = int(input())
print(finished_order(product, ordered_qty))
