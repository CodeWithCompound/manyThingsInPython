class Rec:
    def __init__(self, w, h):
        self._w = w
        self._h = h

    @property
    def w(self):
        try:
            int(self._w)
            return f"h: {self._w:.1f} cm"
        except ValueError:
            print("Rectangle must consist of valid numbers, First argument is invalid")
            exit(1)

    @property
    def h(self):
        try:
            int(self._h)
            return f"h: {self._h:.1f} cm"
        except ValueError:
            print("Rectangle must consist of valid numbers, Second argument is invalid")
            exit(1)


rec = Rec(4, "Apple")

print(rec.h)
print(rec.w)
