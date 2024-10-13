calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    up = string.upper()
    low = string.lower()
    return length, up, low


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    if string in (i.lower() for i in list_to_search):
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)