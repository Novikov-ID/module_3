calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    string_info = (len(string), string.upper(), string.lower())
    return string_info

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
