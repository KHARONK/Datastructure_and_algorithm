class Switcher(object):
        # global input holders
        a = b = 0

# begin math switcher functions
        def add(self, a, b):
                return a+b
        def sub(self, a, b):
                return a-b
        def mul(self, a, b):
                return a*b
        def div(self, a, b):
                return a/b
        def sqr(self, a, b):
                return a*a
# end math switcher functions

        def init_switcher(self):
                switcher = {
                        "+": self.add,
                        "-": self.sub,
                        "*": self.mul,
                        "/": self.div,
                        "^": self.sqr
                        }
                return switcher
# end of def init_switcher():

        def menu(self,sw):
                # menus
                print("Calculator type your operation")
                for key in sw.keys():
                        print(key)
# end of def main():

        def operation(self,ch, switcher):
                self.a=int(input("Enter first digit:"))
                self.b=int(input("Enter second digit:"))

                return switcher.get(ch, "Invalid option chosen")(self.a, self.b)
                # end def operation():

        def main(self):
                sw = self.init_switcher()
                self.menu(sw)
                # input choice
                ch=input("Enter Choice: ")
                ans = self.operation(ch, sw)
                print(ans)

s=Switcher()
s.main()
# if __name__ == "__main__":
#     main()


