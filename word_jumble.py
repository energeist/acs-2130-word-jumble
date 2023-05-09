def dictionary_hashtable():
    with open("/usr/share/dict/words") as text:
        words = text.read().split()
    hashtable = {}
    two_letter_words = []
    six_letter_words = []
    for word in words:
        word = word.replace("'", "")
        hashtable.update({word.lower(): word.lower()})
        if len(word.strip("'")) == 2:
            two_letter_words.append(word)
        elif len(word.strip("'")) == 6:
            six_letter_words.append(word)
    return hashtable, two_letter_words, six_letter_words

def permutations(word):        
    if(len(word)==1): 
        return [word]
    results=[]
    for i, char in enumerate(word):
        results += [char+p for p in permutations(word[:i]+word[i+1:])]
    return results

if __name__ == "__main__":

    jumbled_words = ["tefon", "sokik", "niumem", "siconu"] # often, kiosk, immune, cousin

    dictionary, twos, sixes = dictionary_hashtable()

    possible_combinations = []
    solved_words = []

    for jumble in jumbled_words:
        possible_combinations.append(permutations(jumble))

    for combo_list in possible_combinations:
        for combo in combo_list:
            if combo in dictionary and combo not in solved_words:
                solved_words.append(combo)

    final_characters = ''.join([
        solved_words[0][2],
        solved_words[0][4],
        solved_words[1][0],
        solved_words[1][1],
        solved_words[1][3],
        solved_words[2][4],
        solved_words[3][3],
        solved_words[3][4]
    ])

    possible_finals = []

    final_combos = permutations(final_characters)
    # print(final_combos)
    for combo in final_combos:
        if combo[0:2] in dictionary and combo[2:] in dictionary:
            if combo not in possible_finals:
                possible_finals.append(combo)
                
    print(f"Starting jumbled words are: {jumbled_words}")
    print(f"Solved words are {solved_words}")
    print(f"Characters in the final word are: {final_characters}")
    print(f"Possible final combinations: {possible_finals}")