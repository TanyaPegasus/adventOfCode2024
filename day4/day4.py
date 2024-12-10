DATA_FILE = "data.txt"
TEST_FILE = "testData.txt"

def parse_file(file_name):
    with open(file_name) as file:
        return file.readlines()
    
def create_list_from_line(list_of_lines):
    for i in range(len(list_of_lines)):
        list_of_lines[i] = list((list_of_lines[i].strip()))
    return list_of_lines

def check_index_is_safe(numbers, full_list):
    if 0 <= numbers[0] < len(full_list):
        if 0 <= numbers[1] < len(full_list[numbers[0]]):
            return True
    return False

def find_x(full_list):
    full_total = 0
    for i in range(len(full_list)):
        for j in range(len(full_list[i])):
            if full_list[i][j] == "X":
                t = find_xmas(full_list, i, j)
                full_total += t
    return full_total

def find_xmas(full_list, i, j):
    numbers = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1),
        ]

    locations_to_check = []
    for number in numbers:
        if check_index_is_safe((number[0] + i, number[1] + j), full_list):
            locations_to_check.append(number)
        
    total = 0
    for loc in locations_to_check:
        x = i
        y = j

        if not find_letter(full_list, x, y, loc[0], loc[1], "M"):
            continue
        if not find_letter(full_list, x, y, loc[0]*2, loc[1]*2, "A"):
            continue
        if not find_letter(full_list, x, y, loc[0]*3, loc[1]*3, "S"):
            continue
        total += 1

    return total

def find_letter(full_list, x, y, inc_x, inc_y, letter):
    x += inc_x
    y += inc_y
    if check_index_is_safe((x, y), full_list):
        if full_list[x][y] == letter:
            return True
    return False

def find_a(data_list):
    full_total = 0
    for i in range(len(data_list)):
        for j in range(len(data_list[i])):
            if data_list[i][j] == "A":
                if find_mas_mas(data_list, i, j):
                    full_total += 1
    return full_total

def find_mas_mas(data_list, i, j):
    left_to_right_diag = [(-1, -1), (1, 1)]
    right_to_left_diag = [(-1, 1), (1, -1)]

    if check_diagonal(left_to_right_diag, data_list, i, j) and check_diagonal(right_to_left_diag, data_list, i, j):
        return True
    return False
    
def check_diagonal(diagonals_list, data_list, i, j):
    needed_letters = {"M", "S"}
    found_letters = set(())
    for location in diagonals_list:
        if check_index_is_safe((i+location[0], j+location[1]), data_list):
            found_letters.add(data_list[i+location[0]][j+location[1]])
    if found_letters.issuperset(needed_letters):
        return True
    return False

def main_day_4():
    data = parse_file(DATA_FILE)
    new_list = create_list_from_line(data)

    all_x = find_x(new_list)
    all_x_mas = find_a(new_list)
    
    print(f"Part 1: {all_x}\nPart 2: {all_x_mas}")


if __name__ == "__main__":
    main_day_4()
    



# if check_index_is_safe((i + loc[0] + loc[0] +loc[0], j + loc[1] + loc[1] + loc[1]), full_list):
#             if not full_list[i + loc[0] + loc[0] + loc[0]][j + loc[1] + loc[1] + loc[1]] == "S":
#                 continue
#             total += 1

#  for loc in locations_to_check:
#         loc_x = i + loc[0]
#         loc_y = j + loc[0]
#         if not full_list[i + loc[0]][j + loc[1]] == "M":
#             continue
#         if check_index_is_safe((i + loc[0] + loc[0], j + loc[1] + loc[1]), full_list):
#             if not full_list[i + loc[0] + loc[0]][j + loc[1] + loc[1]] == "A":
#                 continue
#         if check_index_is_safe((i + loc[0] + loc[0] +loc[0], j + loc[1] + loc[1] + loc[1]), full_list):
#             if not full_list[i + loc[0] + loc[0] + loc[0]][j + loc[1] + loc[1] + loc[1]] == "S":
#                 continue
#             total += 1