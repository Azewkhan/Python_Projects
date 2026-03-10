from textblob import TextBlob
Initial_sentence = input('Enter your sentence here\n').split()

Correct_sentence= []

for words in Initial_sentence:
   Txt_blob= TextBlob(words)
   Correct_sentence.append(Txt_blob.correct())
print("----------------------------------------------------")
print("Your correct sentence should be")
for i in Correct_sentence:
  print(i, end= ' ')