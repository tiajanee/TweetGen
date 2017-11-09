
import re
import random
 
#takes a hard-coded word list and counts the instances of each unique word 
def histogram(word_list):
    search = re.compile('\w+')
    histogram = {}  
 
    for word in word_list:
        if search.match(word) is None:
            continue

        if word not in histogram:
            histogram.update({word: 0})
 
        histogram[word] += 1
 
    return histogram
 
#counts the # of unique words in a given word list
def unique_words(histogram):
     return len(histogram.keys())
 
#when this function is called, it will print the instances for a particular word 
def frequency(word, histogram):
    if word not in histogram:
         return 0
    
    return histogram[word]

#generates a random word from the histogram
def random_word(histogram):       

    rand_word =  random.choice(list(histogram.keys()))
    #rand_number = random.randint(0, 15))
        #for i in range(rand_number):
        #rand_sentence += (rand_word)
    return rand_word


#insert SS here

# def weighted_freq(histogram, word_list):
    
#     word_weight = histogram.keys() / (sum(word_list))
#     rand_int = random.randrange(0,1)
#     for word in histogram:
#         if word_weight < rand_int:
#             continue
#         if word_weight > rand_int:
#             print(word)
 
if __name__ == "__main__":
    #hard-coded text file !!!!#make a fucntion that takes a file name argument
    text_file = open('practice_text.txt')
    #splits words in file into lines and make the all lower case for the unique_words() function
    text_word_list = [word.lower() for word in text_file.read().rsplit()]
    #saves histogram in a variable
    text_histogram = histogram(text_word_list)
    



    #print statement test to make sure it works
    #print('Histogram:\t', text_histogram, '\n\n')
#print('Num of Unique_Words:\t', unique_words(text_histogram), '\n')
#print('"and" occurs:\t', frequency('and', text_histogram), 'times \n')
#print('"red" occurs:\t', frequency('red', text_histogram), 'times \n')
#print('"he" occurs:\t', frequency('he', text_histogram), 'times \n')
#print("A random word from this histogram is", random_word(text_histogram))
#print("Another random word from this histogram is", random_word(text_histogram))

    #print("This is a weighted random word", weighted_freq(text_histogram, text_word_list))
