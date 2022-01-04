from textblob import TextBlob
a=input("Enter the word: ")
b=TextBlob(a)
if a==b.correct():
    print("Text is Correct")
else:
    print(f"Did you mean: {str(b.correct())}")
