for row in range(1,3):
    for col in range(row,6,2):
        if row==col:
            continue
        else:
            print(col)
    print()