from flask import Flask
import histogram

app = Flask(__name__)

@app.route('/')
def lol():
   text_file = open('practice_text.txt')
   text_word_list = [word.lower() for word in text_file.read().rsplit()]
   text_histogram = histogram.histogram(text_word_list)
   rand_number = random.randint(0, 15)
       rand_sentence = " "
           
           for i in range(rand_number):
               if i == rand_number - 1:
                   rand_sentence += (random_word(text_histogram) + ".")
                       else:
                           rand_sentence += (random_word(text_histogram) + " ")
                               print (rand_sentence)
                           
   return histogram.random_word(text_histogram)

if __name__ == '__main__':
    
    app.run()
