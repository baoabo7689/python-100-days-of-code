def calculate_love_score(name1, name2):
    combine_names = name1 + name2
    total1 = 0
    total2 = 0
    for x in combine_names:
        if x in "TRUEtrue":
            total1 += 1 
        if x in "LOVElove":
            total2 += 1 
    print(total1 * 10 + total2)

calculate_love_score("Angela Yu", "Jack Bauer")