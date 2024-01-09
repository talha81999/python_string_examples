# we can sort numbers in ascending or descending order using sorted function

# first we will go with ascending order

def sort_in_ascending_order(numbers):
    sorted_numbers = sorted(numbers.split(","))
    return sorted_numbers


def sort_in_descending_order(numbers):
    sorted_numbers = sorted(numbers.split(","), reverse=True)
    return sorted_numbers


comma_separated_numbers = input("Enter comma separated numbers: ")
ascending_order = sort_in_ascending_order(comma_separated_numbers)
descending_order = sort_in_descending_order(comma_separated_numbers)
print("Ascending order: ", ascending_order, end="\n")
print("Descending order: ", descending_order)
