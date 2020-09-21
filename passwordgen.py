import random
import string

class Password:

    def __init__(self, pass_length=None, symbols=False,
                 numbers=False, upper=False, lower=False, specific=""):
        self.pass_length = pass_length
        self.symbols = symbols
        self.numbers = numbers
        self.upper = upper
        self.lower = lower
        self.specific = specific
        self.MAX_TRIES = 1000

    def create_pass(self):
        char_lists = []
        if self.symbols:
            char_lists.append(string.punctuation)

        if self.numbers:
            char_lists.append(string.digits)

        if self.upper:
            char_lists.append(string.ascii_uppercase)

        if self.lower:
            char_lists.append(string.ascii_lowercase)

        if self.pass_length is None:
            cur_pass_length = random.randint(0, 21)
        else:
            cur_pass_length = self.pass_length
        password = "".join(el for lst in char_lists for el in lst)
        tries = 0
        while True:
            sampling = random.choices(password, k=cur_pass_length)
            final = ''.join(sampling)

            if self.specific:  # not an empty string
                final += self.specific
            if all(any(char in lst for char in final) for lst in char_lists):
                break
            tries += 1
            if tries > self.MAX_TRIES:
                raise RuntimeError(f"Tries count exceeded! Last attempt: {final}")
        return final


p1 = Password(20, *[True] * 2)
print(p1.create_pass())
