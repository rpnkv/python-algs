class Fnx:
    some_attribute = "123"

    def method(self):
        some_attribute="456"
        print(some_attribute)

        print(self.some_attribute)

inst = Fnx()
inst.method()