def spam1():
    def spam2():
        def spam3():
            z = " even"
            z += y
            print("in spam3 locals: {}".format(locals()))
            return z

        y = " more " + x  # y must exist before spam3 is called!
        y += spam3()
        print("in spam2 locals: {}".format(locals()))
        return y

    x = "spam,"  # x must exist before spam2 is called!
    x += spam2()
    print("in spam1 locals: {}".format(locals()))
    return x


print(spam1())
print(locals())
print(globals())
