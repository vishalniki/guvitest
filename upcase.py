string=raw_input()
def case(word):
        import re
        return ' '.join(x.capitalize() or ' ' for x in word.split(' '))
print(case(string))
