calls = 0
string_input = 'Capybara'
string_input_2 = 'Armageddon'
string_example = 'Urban'
list_example = ['ban', 'BaNaN', 'urBAN']
string_example_2 = 'cycle'
list_example_2 = ['recycling, cyclic']


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    string = (len(string)), string.upper(), string.lower()
    return string


def is_contains(string, list_to_search):
    count_calls()
    for word in list_to_search:
        if word.lower() in string.lower():
            return True
    return False


print(string_info(string_input))
print(string_info(string_input_2))
print(is_contains(string_example, list_example))
print(is_contains(string_example_2, list_example_2))
print(calls)

