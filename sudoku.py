import sys
import csv

def get_box_values(items, row, col):
    box_row = int(row - row%3)
    box_col = int(col - col%3)

    values = set()
    for r in range(box_row, box_row+3):
        for c in range(box_col, box_col+3):
            values.add(items[r][c])

    return values - {' '}
    

def search_value(items, row, col):
    value = items[row][col]
    if value == ' ':
        row_values = set(items[row]) - {' '}
        col_values = set(map(lambda x: items[x][col], list(range(9)))) - {' '}
        box_balues = get_box_values(items, row, col)

        unused_values = set(map(lambda x: str(x), list(range(1, 10)))) - (row_values | col_values | box_balues)

        # print("search:", row, col)
        # print("row_values", row_values)
        # print("col_values", col_values)
        # print("box_balues", box_balues)
        # print("unused_values", unused_values)

        if len(unused_values) == 1:
            items[row][col] = unused_values.pop()
            return items
        
    return None

def check(items):
    has_resolved = False
    for r in range(9):
        for c in range(9):
            result = search_value(items, r, c)
            if result is not None:
                items = result
                has_resolved = True
    
    if has_resolved:
        return check(items)
    else:
        return items


filename = sys.argv[1]

with open(filename, 'r') as file:
    items = list(csv.reader(file))

    print("---- input data ----")
    for row in items:
        print(row)

    items = check(items)

    print("---- solved data ----")
    for row in items:
        print(row)
