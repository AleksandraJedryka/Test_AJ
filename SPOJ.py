# Napisać program do dodawania dwóch liczb całkowitych. Na wejściu podane są w oddzielnych liniach dwie liczby
# naturalne. A oraz B mniejsze od 200. Na wyjściu należy wypisać wartość ich sumy, A + B.

var_A = int(input())
var_B = int(input())
if var_A < 200 and var_B < 200:
	print(var_A+var_B)