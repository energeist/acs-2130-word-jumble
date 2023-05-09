def dictionary_hashtable():
    with open("/usr/share/dict/words") as text:
        words = text.read().split()
    # use python dict as a hashtable for lookup speed, where key and value are the same
    hashtable = {}
    for word in words:
        word = word.replace("'", "")
        hashtable.update({word.lower(): word.lower()})
    return hashtable

def permutations(word):        
    if(len(word)==1): 
        return [word]
    results=[]
    for i, char in enumerate(word):
        # solve recursively with list comprehension
        results += [char+remainder for remainder in permutations(word[:i]+word[i+1:])]
    return results

if __name__ == "__main__":

    jumbled_words = ["tefon", "sokik", "niumem", "siconu"] # often, kiosk, immune, cousin

    # initialize dictionary
    dictionary = dictionary_hashtable()

    possible_combinations = []
    solved_words = []

    # get permutations from jumbled words
    for jumble in jumbled_words:
        possible_combinations.append(permutations(jumble))

    # pick valid words from the full list
    for combo_list in possible_combinations:
        for combo in combo_list:
            if combo in dictionary and combo not in solved_words:
                solved_words.append(combo)

    # create an array of characters from the provided indices
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

    # pick out two and six word combinations of valid words, since we know the solution has the form ()()-()()()()()()
    final_combos = permutations(final_characters)
    for combo in final_combos:
        if combo[0:2] in dictionary and combo[2:] in dictionary:
            if combo not in possible_finals:
                possible_finals.append(combo)

    print(f"Starting jumbled words are: {jumbled_words}")
    print(f"Solved words are {solved_words}")
    print(f"Characters in the final word are: {final_characters}")
    print(f"Possible final combinations: {possible_finals}")