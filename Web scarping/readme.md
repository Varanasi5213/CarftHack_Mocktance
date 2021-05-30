## Web Scarping

**Descreption**
> The idea is to find reddit posts related to NVIDIA using Praw library and use pretrained sentinment analysis on the same.

**Work Details**
1. _Web_scraping (1)_ notebook consists the reddit posts and the date time of the posts along with other attirbutes like score, upvote ratio and some essential inputs.
2. The posts are sorted interms of date and stored in a csv file called _NVIDIA.csv_
3. All he features except upvote ratio tell the magniture towards the post but the direction i.e. whethear it is negative or positive is not determined. 
4.This direction is very important interms of stock preditions which can help tell the movement of stock is upwards or downwords.
5.So in _Sentiment_Analysis_ notebook the sentiment analysis of the posts has been done using pretrained model VADER.
6.VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media
7.The prdictions of VADER has been added to the original feature set and the date have been sorted.
8.The final result is stored in _NVIDIA_sent1.csv_ file.
