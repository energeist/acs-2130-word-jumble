# list of jumbled words

jumbled_words = ["tefon", "sokik", "niumem", "siconu"] # often, kiosk, immune, cousin

def permutations(word):        
    if(len(word)==1): return [word]
    results=[]
    for i,v in enumerate(word):
        result += [v+permutation for permuatation in permutations(word[:i]+word[i+1:])]
        print(f"v: {v}")
        print(f"result: {result}")
    return result

solved_words = []

for jumble in jumbled_words:
    solved_words.append(permutations(jumble))

print(solved_words)


# final_characters = [
#     solved_words[0[2]],
#     solved_words[0[4]],
#     solved_words[1[0]],
#     solved_words[1[1]],
#     solved_words[1[3]],
#     solved_words[2[4]],
#     solved_words[3[3]],
#     solved_words[3[4]]
# ]

def solve_recursively(word):
    pass

def unscramble_words(words):
    for word in words:
        
        i = 0
        
        n = len(word)-1
    pass

def unscrable_final(final):
    pass

