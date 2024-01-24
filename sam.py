
def chocolates_distribution(n, kids_names, total_chocolates, initial_kids):
    chocolate_count = {name: 0 for name in kids_names}
    
    current_kid, current_chocolates = initial_kids[0], 1
    direction = "Clockwise" if initial_kids[0] < initial_kids[1] else "Anti-Clockwise"
    
    while current_chocolates <= total_chocolates:
        chocolate_count[current_kid] += 1
        current_kid = kids_names[(kids_names.index(current_kid) + 1 + (1 if direction == "Clockwise" else -1)) % n]
        current_chocolates += 1
    
    max_chocolates = max(chocolate_count.values())
    high_score_kids = [name for name, count in chocolate_count.items() if count == max_chocolates]
    
    last_kid = kids_names[(kids_names.index(current_kid) + 1 + (1 if direction == "Clockwise" else -1)) % n]
    penultimate_kid = kids_names[(kids_names.index(last_kid) + 1 + (1 if direction == "Clockwise" else -1)) % n]
    
    # Print the results
    print(f"Direction: {direction}")
    print(f"Kids with the highest number of chocolates: {' - '.join(high_score_kids)} - {max_chocolates}")
    print(f"Penultimate kid: {penultimate_kid}")

n = 6
kids_names = ["A", "B", "C", "D", "E", "F"]
total_chocolates = 10
initial_kids = ["A", "C"]
chocolates_distribution(n, kids_names, total_chocolates, initial_kids)
# def Complexity(txt):
#     vowels = set('aeiou')
#     words = txt.split()
#     tough = 0
#     simple = 0

#     for word in words:
#         # count the number of vowels and consonants in the word
#         vowel_count = sum(1 for c in word if c.lower() in vowels)
#         consonant_count = len(word) - vowel_count

#         # check if the word is tough
#         if consonant_count > vowel_count or any(word[i] not in vowels for i in range(3, len(word))):
#             tough += 1
#         # check if the word is simple
#         elif consonant_count < 4:
#             simple += 1

#     # calculate the complexity quotient
#     complexity_quotient = (6 * tough) - (3 * simple)

#     return complexity_quotient
# def is_hard_word(word):
#     vowels = 'aeiou'
#     hard_word = False
#     consonant_count = 0
#     vowel_count = 0

#     for i in range(len(word)):
#         if word[i] in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1

#         if i < len(word) - 1:
#             if word[i] != word[i+1]:
#                 if word[i] in vowels:
#                     if word[i+1] not in vowels:
#                         if consonant_count >= 2:
#                             hard_word = True
#                             break
#                 else:
#                     if word[i+1] in vowels:
#                         if vowel_count >= 2:
#                             hard_word = True
#                             break

#     if consonant_count == 5 and vowel_count == 2:
#         hard_word = True

#     return hard_word

# def find_difference(description):
#     words = description.split()
#     hard_word_count = 0
#     easy_word_count = 0

#     for word in words:
#         if is_hard_word(word):
#             hard_word_count += 1
#         else:
#             easy_word_count += 1

#     return 6 * hard_word_count - 3 * easy_word_count

# print(find_difference("qiewlldoaa life ace by fantasy 745"))
# print(find_difference("abc"))
# print(find_difference("live the life"))
# print(find_difference("b14745 614745"))



# # def find_term(M):
# #     # If M is less than 3 or not a multiple of 2, the series is not defined
# #     if M < 3 or M % 2 != 0:
# #         return "Invalid input"

# #     # Calculate the first term and common difference
# #     a = 22
# #     d = (148 - 40) / (7 - 3)

# #     # Calculate the M-th term
# #     term = a + (M // 2 - 1) * d

# #     return term