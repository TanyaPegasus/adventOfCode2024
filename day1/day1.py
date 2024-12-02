import os

current_directory = os.path.dirname(os.path.realpath(__file__))
lists_file = os.path.join(current_directory, "lists.txt")

left_list = []
right_list = []

def parse_file(filename):
    try:
        with open(filename) as file:
            lines= [line.strip() for line in file]
            for line in lines:
                split: list = line.split()
                left_list.append(int(split[0]))
                right_list.append(int(split[1]))
    except (IOError):
        print(f"Error opening {filename}")
        exit()

    return

def find_total_distance():
    left_list.sort()
    right_list.sort()

    total_distance = 0
    distance = 0

    for i in range(len(left_list)):
        left_number = left_list[i]
        right_number = right_list[i]
        if left_number >= right_number:
            distance = left_number - right_number
        else:
            distance = right_number - left_number
        total_distance += distance
    
    return(total_distance)

def get_similarity():
    total_similarity = 0

    for i in left_list:
        number_of_appearences = 0
        for j in right_list:
            if i == j:
                number_of_appearences += 1
        similarity = i * number_of_appearences
        total_similarity += similarity

    return total_similarity


parse_file(lists_file)
total_distance = find_total_distance()
similarity = get_similarity()
print(f"Total distance: {total_distance}\nSimilarity: {similarity}")
