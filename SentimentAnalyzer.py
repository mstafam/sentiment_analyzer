from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw()

SIA = SentimentIntensityAnalyzer()

print("\nThis application determines the sentiment of text ranging from very negative to very positve. You can upload a .txt for longer form texts.\n")

def get_textfile():
    try:
        open_file = askopenfilename(title= "Select file")
        f = open(open_file, "r")
        file_text = f.read()
        return file_text
    except:
        print("Invalid file! Choose only .txt files!", end="")
    
def sentiment(text):
    try:
        sentiment_list = SIA.polarity_scores(text)
        neg_sentiment = sentiment_list["neg"]
        neu_sentiment = sentiment_list["neu"]
        pos_sentiment = sentiment_list["pos"]
        comp_sentiment = sentiment_list["compound"]

        if (comp_sentiment > 0.5):
            overall_sentiment = "Very Positive."
        elif (0.5 >= comp_sentiment > 0.1):
            overall_sentiment = "Positive."
        elif (0.1 >=comp_sentiment > -0.1):
            overall_sentiment = "Neutral."
        elif (0.1 >= comp_sentiment > -0.5):
            overall_sentiment = "Negative."
        else:
            overall_sentiment = "Very Negative."

        print(f"Overall Sentiment: {overall_sentiment}")
        details = input("For more detail, type 1: ")
        if (details == "1"):
            print(f"Negative Sentiment: {round(neg_sentiment * 100)}%\nNeutral Sentiment: {round(neu_sentiment * 100)}%\nPositive Sentiment: {round(pos_sentiment * 100)}%")

        print("Thank you for using this application!")
    except:
        pass
def main():
    text_input = input("Would you like to input text(type 1), or use a text file(type 2): ")
    if (text_input != "1" and text_input != "2"):
        while (text_input != "1" and text_input != "2"):
            text_input = input("Invalid Response! Would you like to input text(type 1), or use a text file(type 2): ")
    if (text_input == "1"):
        sentiment_input = input("Write some text to recieve a sentiment: ")
        sentiment(sentiment_input)
    elif (text_input == "2"):
        sentiment(get_textfile())
    

if __name__ == "__main__":
    main()