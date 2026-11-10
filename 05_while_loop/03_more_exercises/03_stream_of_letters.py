word = ""
has_c = False
has_o = False
has_n = False
result = ""

line = input()
while line != "End":
    if len(line) > 0:
        ch = line[0]

        is_letter = ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

        if is_letter:
            if ch == 'c' and not has_c:
                has_c = True
            elif ch == 'o' and not has_o:
                has_o = True
            elif ch == 'n' and not has_n:
                has_n = True
            else:
                word = word + ch

            if has_c and has_o and has_n:
                result = result + word + " "
                word = ""
                has_c = False
                has_o = False
                has_n = False

    line = input()

print(result)