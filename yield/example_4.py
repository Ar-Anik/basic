def custom_fun(text, keyword):
    sentence = text.split()
    for word in sentence:
        if word == keyword:
            yield True

txt = "Man For Man"
s = custom_fun(txt, 'Man')

print(sum(s))

"""
sum() is just a for-loop that adds up the values from an iterable.

Q : sum(s) — How does it work?
    * sum() takes an iterable, and adds up its values.
    * When it sees a True, it treats it as 1 (because in Python: True == 1).
    * False would be treated as 0.
"""

total = 0
s_1 = custom_fun(txt, 'Man')
for val in s_1:
    total += val

print("total sum : ", total)
