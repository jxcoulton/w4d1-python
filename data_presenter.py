from os import closerange, startfile


cupcake_invoice = open('CupcakeInvoices.csv')

# for line in cupcake_invoice:
#     print(line)


# for flavor in cupcake_invoice:
#     flavor = flavor.split(",")
#     print(flavor[2])

# for line in cupcake_invoice:
#     line = line.split(',')
#     print(line[4])

# total = 0

# for line in cupcake_invoice:
#     line = line.split(',')
#     total += float(line[4])

# print(total)

chocolate = 0
vanilla = 0
strawberry = 0

for flavor in cupcake_invoice:
    flavor = flavor.split(",")
    if flavor[2] == 'Chocolate':
        chocolate += 1
        
    elif flavor[2] == 'Vanilla':
        vanilla += 1
    else:
        strawberry += 1

print(chocolate, vanilla, strawberry)

cupcake_invoice.close()

