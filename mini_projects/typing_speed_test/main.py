import time  #time related functions
import random
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "I think, therefore I am."
    ]
def accuracy_function(user_input, test_sentence):
    user_words = user_input.split()
    test_words = test_sentence.split()
    correct_words = 0
    for uw, tw in zip(user_words, test_words):
        if uw == tw:
            correct_words += 1
    accuracy = (correct_words / len(test_words)) * 100
    return accuracy
  
def typing_test():
  test_sentence = random.choice(sentences)
  print("Type the following sentence as fast as you can:")
  print(test_sentence)
  input("Press Enter when you are ready...")
  start_time= time.time()
  user_input = input("start typing")
  end_time = time.time()
  time_taken = end_time - start_time
  words_count = len(test_sentence.split())
  wpm = (words_count / time_taken) * 60
  print("Results:")
  print(f"Time taken: {time_taken} seconds")
  print(f"Words typed: {words_count}")
  print(f"Your WPM: {wpm:.2f}")
  accuracy = accuracy_function(user_input, test_sentence)
  print(f"Accuracy: {accuracy:.2f}%")

  
typing_test()