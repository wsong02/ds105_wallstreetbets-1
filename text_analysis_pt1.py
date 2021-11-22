import pickle
import nltk
import csv
from nltk.corpus import stopwords
import pandas as pd
from nltk.tokenize import word_tokenize

comments = pickle.load(open('WSB_Comments.pickle', 'rb'))
comments
stop_words=set(stopwords.words("english"))
custom_stop_words =["!",":",".",",","'","..."]
stop_words.update(custom_stop_words)


ticker_dict = {"Ticker_ID":[], "Comment_Frequency":[], "Upvotes":[]}
for i in range(2,len(comments)): ##len(comments)
    the_comment = str(comments[i:i+1].body)
    upvotes = int(comments[i:i+1].score)
    
    tokenized_word = word_tokenize(the_comment)
    
    for w in tokenized_word:
        for char in w:
            if not char.isalpha() or char in custom_stop_words:
                w.replace(char,"")
        if (len(w)== 3 or len(w) == 4) and w.isupper():

            if len(ticker_dict["Ticker_ID"]) != 0:
                if w in ticker_dict["Ticker_ID"]:
                    id_index = ticker_dict["Ticker_ID"].index(w)
                    ticker_dict["Comment_Frequency"][id_index] += 1
                    ticker_dict["Upvotes"][id_index] += upvotes
                else:
                    ticker_dict["Ticker_ID"].append(w)
                    ticker_dict["Comment_Frequency"].append(1)
                    ticker_dict["Upvotes"].append(upvotes)
            else:
                   ticker_dict["Ticker_ID"].append(w)
                   ticker_dict["Comment_Frequency"].append(1)
                   ticker_dict["Upvotes"].append(upvotes)
            
    if (i-1) % 1000 == 0:
        print("on comment: ", i-1)


all_tickers_df = pd.read_csv("nasdaq_screener_1637600752040.csv", usecols=["Symbol"])
tickers_list = all_tickers_df["Symbol"].tolist()

false_positives_dict = {"Ticker_ID":[], "Comment_Frequency":[], "Upvotes":[]}

for ticker in ticker_dict["Ticker_ID"]:
    if ticker not in tickers_list:
        ticker_index = ticker_dict["Ticker_ID"].index(ticker)
        false_positives_dict["Ticker_ID"].append(ticker_dict["Ticker_ID"][ticker_index])
        false_positives_dict["Comment_Frequency"].append(ticker_dict["Comment_Frequency"][ticker_index])
        false_positives_dict["Upvotes"].append(ticker_dict["Upvotes"][ticker_index])
        del ticker_dict["Ticker_ID"][ticker_index]
        del ticker_dict["Comment_Frequency"][ticker_index]
        del ticker_dict["Upvotes"][ticker_index]
        
tickers_df = pd.DataFrame(ticker_dict)
tickers_df.sort_values(by=['Upvotes'], inplace=True, ascending=False)
false_positives_df = pd.DataFrame(false_positives_dict)
false_positives_df.sort_values(by=['Upvotes'], inplace=True, ascending=False)

tickers_df.to_pickle('WSB_tickers.pickle')
tickers_df.to_csv(r'tickers.csv', mode = 'w')
false_positives_df.to_pickle('false_positives.pickle')
false_positives_df.to_csv(r'false_positives.csv', mode = 'w')
