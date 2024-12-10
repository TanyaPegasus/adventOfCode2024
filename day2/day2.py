DATA_FILE = "reports.txt"
TEST_FILE = "testReports.txt"

def parse_file(file_name):
    with open(file_name) as file:
        return file.readlines()
        
def check_full_line(data_list):
    total_part_1 = 0
    total_part_2 = 0

    for i in data_list:
        line = i.strip("\n").split(" ")
        if test_ascending_or_descending(line):
                total_part_1 += 1
                total_part_2 += 1
        else:
            if check_again(line):
                total_part_2 += 1  
    return total_part_1, total_part_2

def test_ascending_or_descending(line):
    all_ascending = True
    all_descending = True

    for i in range(len(line)):
        if i < len(line)-1:
            if int(line[i]) <= int(line[i+1]):
                all_ascending = False
            if int(line[i]) >= int(line[i+1]):
                all_descending = False
    if not all_ascending and not all_descending:
        return False
    return check_correct_distance(line)

def check_correct_distance(line):
    correct_distance = True
    for i in range(len(line)):
        if i < len(line)-1:
            difference = abs(int(line[i]) - int(line[i+1]))
            if difference < 1 or difference > 3:
                correct_distance = False
    return correct_distance

def check_again(line):
    for i in range(len(line)):
        new_list = line.copy()
        del(new_list[i])
        if test_ascending_or_descending(new_list):
            return True
    return False

def main_day_4():
    data = parse_file(DATA_FILE)
    result = check_full_line(data)
    print(f"Part 1: {result[0]}\nPart 2: {result[1]}")
   

if __name__ == "__main__":
    main_day_4()
    