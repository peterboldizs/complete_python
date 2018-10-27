import timeit

text = "what have the romans ever done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


def map_words():
    w_map = list(map(str.upper, text.split(' ')))
    return w_map


def print_words_map():
    for w in map(str.upper, text.split(' ')):
        print(w, sep=' ', end=' ')


if __name__ == '__main__':
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())
    print_words_map()

    print("\ncomp_caps: {}".format(timeit.timeit(comp_caps, number=1000)))
    print("map_caps: {}".format(timeit.timeit(map_caps, number=1000)))
    print("\ncomp_words: {}".format(timeit.timeit(comp_words, number=1000)))
    print("map_words: {}".format(timeit.timeit(map_words, number=1000)))
