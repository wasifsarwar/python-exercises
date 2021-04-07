###
### Author: Sornali Rahman
### Class: CSc 110
### Description: This program reads a text file and produces an infographic
###              based on the text. It prints total unique words, most used words
###              grouped by word size, and then prints two bar charts. One for word
###              length and another for capitalized vs non-capitalized words

import graphics

def main():
    file_name_input = input("Please enter file name: \n")
    f = open(file_name_input, "r")
    word_counts = get_word_counts(f)

    # set the infographic canvas and prints the infographic
    gui = graphics.graphics(650, 700, 'infographic')
    draw_infographic(gui, file_name_input, word_counts)

def draw_infographic(gui, file_name_input,word_counts):

    small_words, medium_words, large_words = group_words_by_size(word_counts)
    upper, lower = get_capitalized(word_counts)

    # number of occurences in each case
    unique_words = len(word_counts)
    small_count = len(small_words)
    medium_count = len(medium_words)
    large_count = len(large_words)
    upper_count = len(upper)
    lower_count = len(lower)

    # most used words by lengths
    most_small, most_small_count = get_most_used_words(small_words)
    most_medium, most_medium_count = get_most_used_words(medium_words)
    most_large, most_large_count = get_most_used_words(large_words)


    gui.rectangle(0, 0, 650, 700, 'light green')

    # prints the file name and unique words and most used words
    x = 30
    y = 0
    gui.text(x, y+20, file_name_input, 'blue', 30)
    gui.text(x, y+60, 'Total Unique Words: ' + str(unique_words), 'black', 25)
    gui.text(x, y+100, 'Most used words (s/m/l):  ' + most_small+' (' + most_small_count + 'x) ' +
         most_medium + ' (' + most_medium_count + 'x) ' + most_large +
        ' (' + most_large_count + 'x) ', 'black', 15)

    #prints the bar titles
    gui.text(x+75, y + 130, 'Word lengths', 'black', 25)
    gui.text(x+300, y + 130, 'Cap/Non-Cap', 'black', 25)


    total_height = 450

    # Calculating the height for each bar for small, medium and large words
    small_height = (total_height/ unique_words) * small_count
    medium_height = (total_height/ unique_words) * medium_count
    large_height = (total_height/ unique_words) * large_count

    #Small words bar
    gui.rectangle(x+75, y + 170,  160 , small_height, 'blue')
    gui.text(x+80, y + 175, 'small words', 'black', 10)

    #Medium words bar
    gui.rectangle(x+75, y + 170 + small_height, 160, medium_height, 'orange')
    gui.text(x+80, y + 175 + small_height, 'medium words', 'black', 10)

    #Large words bar
    gui.rectangle(x+75, y + 170 + small_height + medium_height, 160, large_height, 'red')
    gui.text(x+80, y + 175 + small_height + medium_height, 'large words', 'black', 10)

    #cap/non-cap height calculation
    upper_height = (total_height/ unique_words) * upper_count
    lower_height = (total_height/ unique_words) * lower_count

    #capitalized words bar
    gui.rectangle(x+300, y + 170, 160 , upper_height, 'blue')
    gui.text(x+305, y + 175, 'Capitalized', 'black', 10)

    #non-capitalized words bar
    gui.rectangle(x+300, y + 170 + upper_height, 160, lower_height, 'pink')
    gui.text(x+305, y + 175 + upper_height, 'Non Capitalized', 'black', 10)



# This function takes in a file
# Returns a dictionary with words as key and number of
# occurences as it's value
def get_word_counts(f):
    words = []
    for line in f.readlines():
        w = line.split()
        for word in w:
            words.append(word)

    word_counts = {}

    for word in words:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1
    return word_counts

# This function takes in a dictionary of words
# Returns three dictionaries
# First dictionary returns small words and it's number of occurences
# Second dictionary returns medium words and it's number of occurences
# Third dictionary returns large words and it's number of occurences

def group_words_by_size(word_counts):
    small_words = {}
    medium_words = {}
    large_words = {}

    for word in word_counts:
        if len(word) >= 8:
            large_words[word] = word_counts[word]
        elif 5 <= len(word) <= 7:
            medium_words[word] = word_counts[word]
        else:
            small_words[word] = word_counts[word]
    return small_words, medium_words, large_words


# This function takes in a dictionary of words
# Returns two dictionaries, one with Capitalized words and it's count
# another with non-capitalized words and it's count
def get_capitalized(word_counts):
    upper = {}
    lower = {}

    for word in word_counts:
        if (word[0].isupper()):
            upper[word] = word_counts[word]
        else:
            lower[word] = word_counts[word]

    return upper, lower

# This function takes in a dictionary of words
# Returns the most occured word and it's count
def get_most_used_words(words):
    max_words = 0
    result = ''
    for word in words:
        if words[word] > max_words:
            max_words = words[word]
            result = word
    return result, str(max_words)

main()