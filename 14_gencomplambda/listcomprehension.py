def center_text(*args):
    text1 = "-".join([str(arg) for arg in args])
    left_margin = (80 - len(text1)) // 2
    print("_" * left_margin, text1)


center_text("small", "text")
center_text("this", "is a", "larger text")
center_text("this", "is", "an", "even", "larger", "text")

numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)

print("now with list comprehension")
squares2 = [num ** 2 for num in numbers]
print(squares2)

cubes = [n ** 3 for n in range(6)]
print(cubes)

text = "what have the romans ever done for us"
capitals = [char.upper() for char in text]
print(capitals)
words = [word.upper() for word in text.split(' ')]
print(words)
for w in words:
    print(w, sep=' ', end=' ')

print()
lengths = [len(x) for x in text.split()]
print(lengths)
words_lengths = [(y, len(y)) for y in text.split()]
print(words_lengths)

print("now with set comprehension")
text2 = "this is a text which is set for set"
len_set = {(z, len(z)) for z in text2.split()}
print(len_set)
print("inch -> cm")
inches = (3, 6, 9, 12)
cm = [(inch, inch * 2.54) for inch in inches]
print(cm)
cm_tuple = tuple(cm)
print(cm_tuple)

print("conditional comprehension")
no_is = [w.upper() for w in text2.split() if w != "is"]
print(no_is)
