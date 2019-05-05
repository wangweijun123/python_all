class Foo(object):
    def _eq_(self, other):
        return True

f = Foo()
print(f == None) # False
print(f != None) # True
print(f is not None) # True
