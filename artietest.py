import random

affirm = ["good", "Good", "great", "Great", "Yes", "yes"]
deny = ["bad", "Bad", "Not Good", "not good", "No", "no"]
list_check = ["check", "Check", "Debug", "debug"]

# Initialize word lists
known_words = ["dog", "apple", "cat", "I", "am", "is", "eat", "breathe", "pet", "an", "a", "me", "for", "you", "alive"]
subjects = ["dog", "cat"]  # Initial subjects
indefinite_articles = ["a", "an"]  # Initial indefinite articles
verbs = ["chases", "eats"]  # Initial verbs

def generate_phrase():
  """Generates a random phrase based on the word lists."""
  subject1 = random.choice(subjects)
  indefinite_article = random.choice(indefinite_articles)
  verb = random.choice(verbs)
  subject2 = random.choice(subjects)
  return f"{subject1} {indefinite_article} {verb} {subject2}"

def learning():
  """Main learning loop."""
  while True:
    phrase = generate_phrase()
    print(phrase)
    guide = input()

    if guide in affirm:
      phrases.append(phrase)
      new_word = input("Enter a new word: ")
      word_type = input("Enter word type (subject, indefinite_article, verb): ")
      if word_type == "subject":
        subjects.append(new_word)
      elif word_type == "indefinite_article":
        indefinite_articles.append(new_word)
      elif word_type == "verb":
        verbs.append(new_word)
      else:
        print("Invalid word type.")
    elif guide in deny:
      continue
    elif guide in list_check:
      print(known_words)
      print(phrases)
      print(subjects)
      print(indefinite_articles)
      print(verbs)
    else:
      print("Invalid input.")

learning()