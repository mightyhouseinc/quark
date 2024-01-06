# special feature verbose mode -> to trace what is happening
import sys

class postfix():
    def __init__(self, verbose = False):
        self._stack = []
        self._verbose = verbose

    def evaluate(self, post_fix_string):
        if self._verbose:
            print("[!] Postfix Evaluation Started For :", post_fix_string)

        for x in post_fix_string:
            try:
                self._stack.append(int(x))
                if self._verbose:
                    print("[!] Pushed ", x , " in stack -> ", self._stack)
            except ValueError:
                self._act(x)

        if self._verbose:
            print("[!] Answer is : ", self._stack[0])
        return self._stack[0]

    def _act(self, operand):
        b = self._stack.pop()
        a = self._stack.pop()

        if self._verbose:
            print(
                f"[!] Popped last two values from stack, a = {a} and b = {b} -> ",
                self._stack,
            )

        if operand == "+":
            self._stack.append(a + b)
            if self._verbose:
                print(f"[!] Performed {a} + {b} and Pushed in stack -> ", self._stack)
        elif operand == "/":
            try:
                self._stack.append(a // b)
                if self._verbose:
                    print(
                        f"[!] Performed {a} // (integer division) {b} and Pushed in stack -> ",
                        self._stack,
                    )
            except ZeroDivisionError:
                if self._verbose:
                    print(
                        f"[x] Error : Divide By Zero at a = {a} and b = {b} with current stack state -> ",
                        self._stack,
                    )
                sys.exit(1)

        elif operand == "-":
            self._stack.append(a - b)
            if self._verbose:
                print(f"[!] Performed {a} - {b} and Pushed in stack -> ", self._stack)
        elif operand == "*":
            self._stack.append(a * b)
            if self._verbose:
                print(f"[!] Performed {a} * {b} and Pushed in stack -> ", self._stack)
    pass

p_fix1 = postfix()
p_fix2 = postfix(verbose=True)   # with verbose mode
print("------ Without Verbose Mode ------")
print("Answer is",p_fix1.evaluate("12+3*1-"))

print("\n\n------ With Verbose Mode ------")
p_fix2.evaluate("1234+-/2+0/3-")   # raising exception intentionally
