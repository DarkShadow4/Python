# -*- coding: utf-8 -*-
def get_text():
    """Funcion que obtiene el texto"""
    text = raw_input()
    return text

def analize_text(text):
    """Funcion que analiza el texto"""
    text = text.split() #divido el texto en palabras
    words_with_4_vowels = 0
    for word in text:
        words_with_4_vowels = analize_word(word, words_with_4_vowels)
    return words_with_4_vowels

def analize_word(word, words_with_4_vowels):
    """Cuenta el numero de vocales distintas que tiene y añade a la cuenta o no segun si tiene 4 o mas o no"""
    vowels = 0

    if "a" in word:
        vowels += 1

    if "e" in word:
        vowels += 1

    if "i" in word:
        vowels += 1

    if "o" in word:
        vowels += 1

    if "u" in word:
        vowels += 1

    if vowels >= 4:
        words_with_4_vowels = words_with_4_vowels+1

    return words_with_4_vowels

text = get_text()
ww4v = analize_text(text)

print "En este texto hay", ww4v, "palabras con 4 o más vocales distintas"
