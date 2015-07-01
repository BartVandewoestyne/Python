s = "Monty Python"

individual_chars = [letter for letter in s]
print individual_chars

[individual_chars.append(letter) for letter in " Rules"]
print individual_chars

individual_chars2 = [i for i in " big time"]
print individual_chars2

new_list = individual_chars + individual_chars2
print new_list
