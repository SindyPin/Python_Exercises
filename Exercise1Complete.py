# Given: A DNA string ss of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols
# 'A', 'C', 'G', and 'T' occur in ss.

dna = str(input("Please, enter a DNA sequence: "))
while True:
    if "A" in dna or "C" in dna or "G" in dna or "T" in dna and dna.isalpha() and dna.isascii():
        count_A = dna.count("A")
        count_C = dna.count("C")
        count_G = dna.count("G")
        count_T = dna.count("T")
        print(f"There are {count_A} Adenine molecules, {count_C} Cytosine molecules, {count_G} Guanine molecules and "
              f"{count_T} Thymine molecules in the given string.")
        break
    elif "a" in dna or "c" in dna or "g" in dna or "t" in dna and dna.isalpha() and dna.isascii():
        count_a = dna.count("a")
        count_c = dna.count("c")
        count_g = dna.count("g")
        count_t = dna.count("t")
        print(f"There are {count_a} Adenine molecules, {count_c} Cytosine molecules, {count_g} Guanine molecules and "
              f"{count_t} Thymine molecules in the given string.")
        break
    else:
        print("There is something wrong in your input")
        dna = str(input("Please, try again... enter a true DNA sequence: "))
        continue
