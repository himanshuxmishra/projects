from pickle import LONG_BINPUT
import random
lower="abcdefgijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="!@#$%^&*<>?+.,"
all_chars= lower + upper + numbers + symbols
length=(input("ENTER A LENGTH:\n"))
password=''.join(random.sample(all_chars,length))
print("GENERATED PASSWORD:", password)