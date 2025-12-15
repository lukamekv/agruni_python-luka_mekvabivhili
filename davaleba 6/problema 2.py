# Open and read the data.txt file
with open('data.txt', 'r') as data_file:
    lines = data_file.readlines()

# Open small.txt and high.txt for writing
with open('small.txt', 'w') as small_file, open('high.txt', 'w') as high_file:
    for line in lines:

        parts = line.strip().split(',')
        if len(parts) != 4:
            continue

        user_name = parts[0]
        product_name = parts[1]
        amount = int(parts[2])
        price = float(parts[3])


        total = amount * price


        if total < 10:
            small_file.write(line)
        else:
            high_file.write(line)