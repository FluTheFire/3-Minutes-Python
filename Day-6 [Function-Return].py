# Create function
def Sales(product, price, quantity):
    print(f'สินค้า : {product}')
    
    # Create cal variable
    calc = price * quantity
    print(f'ยอดรวมทั้งหมด: {calc} บาท')

    # return value of self fuction
    return calc

# call function and put variable
# put return value of Sales() into total variable
total = Sales('เรือดำน้ำ', 1400, 2)

print('------------------------')
print(f'total = {total}')


