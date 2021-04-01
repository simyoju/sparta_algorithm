class Foo:
    def __init__(self):
        pass

    class bar:
        print("A")

    class Bar:
        def __init__(self):
            print("D")
        print("B")

        class bar:
            print("C")



print(Foo.bar)  # A 출력
print(Foo().bar)  # B 출력
print(Foo.Bar.bar)  # C 출력
print(Foo.Bar().bar)  # D 출력
