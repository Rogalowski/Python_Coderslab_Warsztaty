# -*- coding: cp1250 -*-
import unicodedata

print("Cze��")

with open('test.txt', encoding='cp1250') as f:
    s = f.read()
with open('test2.txt', "w", encoding='cp1250') as f:
    f.write(s)
    f.write("pi��")
print(s)

# Transliteracja: Cze�� --> Czesc
s = unicodedata.normalize('NFKD', "Cze��").encode('ascii', 'ignore')
print(s.decode('utf-8'))
# nie dzia�a dla � i � !!!
s = unicodedata.normalize('NFKD', "��d�").encode('ascii', 'ignore')
print(s.decode('utf-8'))