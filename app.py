from flask import Flask
import histogram
import random

app = Flask(__name__)

@app.route('/')
def lol():
  text_file = open('fish.txt')
  text_word_list = [word.lower() for word in text_file.read().rsplit()]
  text_histogram = histogram.histogram(text_word_list)
  text_weighted_freq = histogram.weighted_freq(text_word_list)

  rand_number = random.randint(0, 8)
  rand_sentence = " "
  for i in range(rand_number):
    if i == rand_number - 1:
      rand_sentence += (histogram.random_word(text_histogram) + ".")
    else:
      rand_sentence += (histogram.random_word(text_histogram) + " ")
      print(rand_sentence)
  return histogram.random_word(rand_sentence)

if __name__ == '__main__':
    app.run()
