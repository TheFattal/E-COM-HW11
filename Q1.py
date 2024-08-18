# a:
tup1: tuple[int] = (99,)
# b:
tup2: tuple[int, ...] = (77, 88, 99)


# c:
def tuple_length(t: tuple) -> int:
    """
    Returns the length of the given tuple.
    """
    return len(t)


print(tuple_length(tup2))


# d:
def tuples_sum(a: tuple, b: tuple) -> tuple:
    """
    Returns sum of 2 tuples.
    """
    return a + b


print(tuples_sum(tup2, tup1))


# e:
def tuples_common(a: tuple, b: tuple) -> tuple:
    """
    Returns only common elements in both tuples.
    """
    temp_list = []
    for element in a:
        if element in b:
            temp_list.append(element)

    return tuple(temp_list)


print(tuples_common(tup1, tup2))


# f:
def tuples_non_common(a: tuple, b: tuple) -> tuple:
    """
    Returns tuple with 2 tuples non common elements.
    """
    temp_list = []
    for element in a:
        if element not in temp_list:
            temp_list.append(element)
    for element in b:
        if element not in temp_list:
            temp_list.append(element)

    return tuple(temp_list)


print(tuples_non_common(tup1, tup2))


# g:
def tuple_element_by_index(a: tuple, index1: int):
    """
    Returns the tuple's right element by the index provided.
    """
    if index1 + 1 <= len(a):
        return a[index1]
    elif index1 == -1:
        return a[-1]
    else:
        return None


# examples:
print(tuple_element_by_index(tup2, 1))
print(tuple_element_by_index(tup2, -1))
print(tuple_element_by_index(tup2, 0))
print(tuple_element_by_index(tup2, 1000))


# h:
def reversed_tuple(a: tuple) -> tuple:
    """
    Returns a tuple reversed.
    """
    return a[::-1]


print(reversed_tuple(tup2))


# i:
def divisors_in_tuple(a: tuple, number1: int) -> int:
    """
    Returns how many divisors the tuple has for the integer given.
    """
    count: int = 0
    for element in a:
        if element >= 0:   # We don't want to modul with 0 or negative:
            if number1 % element == 0 and element > 0:
                count += 1

    return count


# example:
print(divisors_in_tuple((40, 30, 10, 50, 2, 3, 5, 5, 8, 10, -5), 10))


# j:
def tuple_multiplication(a: tuple, mul: int) -> tuple:
    """
    Returns tuple multiplied by an integer.
    """
    return a * mul


print(tuple_multiplication((2, 3, 5), 3))


# k:
# Method 1:
def add_index_to_elements(a: tuple) -> tuple:
    """
    Returns a tuple of tuples by adding every element it's index.
    """
    temp_tuple2: tuple[tuple, ...] = ()
    count: int = 0
    for element in a:
        temp_tuple1 = (count, element)
        temp_tuple2 += (temp_tuple1,)
        count += 1
    return temp_tuple2


# USING ENUMERATE - Method 2:
def add_index_to_elements_using_enumerate(a: tuple) -> tuple:
    """
    Returns a tuple of tuples by adding every element to its index.
    """
    # Using enumerate to get both index and element
    return tuple((index, element) for index, element in enumerate(a))


print(add_index_to_elements((33, "red", "green", 3.56)))
print(add_index_to_elements_using_enumerate((33, "red", "green", 3.56)))


# l:
def tuple_statistics(a: tuple) -> dict:
    """
    Return the tuple statistics in a dictionary.
    """
    numbers_list = list(a)
    return {
        'Maximum': max(numbers_list),
        'Minimum': min(numbers_list),
        'Average': sum(numbers_list) / len(numbers_list),
        'Amount of numbers': len(numbers_list),
        'Sorted from largest to smallest': sorted(numbers_list, reverse=True),
        'Sorted from smallest to largest': sorted(numbers_list)
    }


# Example:
numbers_tuple = (10, 5, 3, 8, 15)
print(tuple_statistics(numbers_tuple))


# m:
def tuple_to_string(letters: tuple) -> str:
    """
    Returns tuple letters in one string word.
    """
    return ''.join(letters)


# Example:
letters_tuple = ('H', 'e', 'l', 'l', 'o')
print(tuple_to_string(letters_tuple))


# n:
def string_to_tuple(s: str) -> tuple:
    """
    Returns a string into a tuple of its characters.
    """
    return tuple(s)


# Example:
input_string = "Hello"
print(string_to_tuple(input_string))


# o:
def tuple_without_number(a: tuple, num: int) -> tuple:
    """
    returns a tuple without the specified number.
    """
    temp_list = []
    for element in a:
        if element != num:
            temp_list.append(element)

    return tuple(temp_list)


input_tuple = (10, 3, 6, 9, 99, 1150, 10, 3, 2, 10)
input_number = 10
print(tuple_without_number(input_tuple, input_number))


# p:
def tuple_without_duplication(a: tuple) -> tuple:
    """
    Returns tuple without its duplication.
    """
    temp_list = []
    for element in a:
        if element not in temp_list:
            temp_list.append(element)

    return tuple(temp_list)


input_tuple = (10, 3, 6, 9, 99, 1150, 99, 10, 3, 3, 2, 10)
print(tuple_without_duplication(input_tuple))


# q:
def indexes_of_a_number(a: tuple, num: int):
    """
    Returns the number's indexes in a tuple.
    """
    indices = [index for index, value in enumerate(a) if value == num]
    return tuple(indices)


input_tuple = (10, 3, 6, 9, 99, 1150, 99, 10, 3, 3, 3, 10)
input_number = 3
print(indexes_of_a_number(input_tuple, input_number))


# r:
def get_names() -> list:
    """
    Collects names from the user until 'done' is entered.
    """
    names = []
    while True:
        name = input("Enter a name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        names.append(name)
    return names


def get_scores() -> list:
    """
    Collects scores from the user until -999 is entered.
    """
    scores = []
    while True:
        try:
            score = int(input("Enter a score (or -999 to finish): "))
            if score == -999:
                break
            scores.append(score)
        except ValueError:
            print("Please enter a valid integer.")
    return scores


def create_pairs(names: list, scores: list) -> tuple:
    """
    Creates a tuple of pairs, each containing a name and a corresponding score.
    """
    pairs = tuple(zip(names, scores))
    return pairs


def main():
    # Collect names from the user
    names = get_names()

    # Collect scores from the user
    scores = get_scores()

    print(create_pairs(names, scores))


if __name__ == "__main__":
    main()
