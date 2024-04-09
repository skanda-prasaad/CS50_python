# Ask user for their name :-
name = input("what's your name ? ").strip().title()
# Remove whitespaces from str  and capitalize :-
# name = name.strip().title()

# Split user's name into firstname and lastname  ;-
first , last = name.split(" ")

# Say hello to user :-
print(f"hello, {first}")




