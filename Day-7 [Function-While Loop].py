# Create function
def Calc(quan, price):
    return quan * price

def Run():
    # while True is inf. loop
    while True:
        q = int(input('กรุณากรอกจำนวนสินค้า: '))
        p = int(input('กรุณากรอกราคาสินค้า: '))
        result = Calc(q, p)
        print(f'สินค้ารวมราคาทั้งหมด: {result} บาท')
        print('-------------')
Run()