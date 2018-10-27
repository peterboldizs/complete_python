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

print("-" * 40)
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

print("-" * 40)
print("now with set comprehension")
text2 = "this is a text which is set for a set"
len_set = {(z, len(z)) for z in text2.split()}
print(len_set)
print("inch -> cm")
inches = (3, 6, 9, 12)
cm = [(inch, inch * 2.54) for inch in inches]
print(cm)
cm_tuple = tuple(cm)
print(cm_tuple)

print("-" * 40)
print("conditional comprehensions")
print(text2)
no_is_list = [w.upper() for w in text2.split() if w != "is"]
print("list: {}".format(no_is_list))
no_is_set = {w.upper() for w in text2.split() if w != "is"}
print("set: {}".format(no_is_set))

print("-" * 40)
test_words = "my test word set for"
print("original text2: {}".format(text2))
print("test_words: {}".format(test_words)
      )
words = set()
for w in text2.split():
    words.add(w)
print("word set: {}".format(words))

for w2 in test_words.split():
    if w2 in words:
        print("contains {}".format(w2))

x = 13
expr = "Twelve" if x == 12 else "other"
print(expr)
print("-" * 40)
print("fizzbuzz game")
for x in range(1, 31):
    fizzbuzz = "fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz, end=' ')

print("\nnow with list comprehension")
fb = ["fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x) for x in range(1, 31)]
print(fb)
for b in fb:
    print(b.center(20, "_"))

print("-" * 40)
print("nested comprehension")
burgers = ["beef", "pork", "chicken"]
toppings = ["cheese", "bacon", "salad"]

meals = [(burg, top) for burg in burgers for top in toppings]
print(meals)

for m in [[(burg, top) for burg in burgers] for top in toppings]:
    print(m)

print("-" * 40)
print("multiplication table 1")
for i in range(1, 11):
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i * j))

print("-" * 40)
print("multiplication table 2")
m_table = [(i, j, i * j) for i in range(1, 11) for j in range(1, 11)]
print(m_table)
