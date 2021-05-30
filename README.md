# CarftHack_Mocktance

## Partition of Problem Statement
> We have devided the probelm statement into two parts
>   1. A Feature extraction 
>   2. Trainin Model for stock price prediction.
>   3. Representation of the output 

## 1. A Feature extraction
> A model to work well on such a complicated data and to fit highly volatile fuction proper feature selction is important. The feature need to proivide an insight about the magnitude as well as direction of a particular data instance.
>   1.Collection of posts regarding NVIDIA from various subreddits are collected along with their score, number of comments and other feature.
>   2.The features like post score,number of comments would tell the magnitude of the post. We also need the direction that is sentiment of the post.
>   3.Even though the feaeture upvote ratio tell us about the sentiment of the post, we may also need other features that depict the sentiment.
>   4.So, We have used VADER pretrained sentiment analyser, to get the sentiment of the post.
>   5.We have also added the corresponding stock prices value for the feature set. In total we have collected 11 features.

## 2. Trainin Model for stock price prediction
> We need an model that mimcs the function the stocks based on the previous behavious. This is called time series prediction , where data is time dependent and we need to capture the underlying cylic and direction of the time series i.e. stock price values.
>   1. The initial model we have tried on VAR (Vector Auto regressor) which is a statistical model for multivariate time series prediction.
>   2. The second model is LSTM based encoder decoder. LSTM is a specialized ANN architecture for ssequential data.
>   3. The model has given 23.9 huber loss of the testing data. The training curves can be seen in the notebooks.

## 3.Representation of the output
> Repressenting the output is also important when it comes to machine learning and deeplearning models.
>   1. To make our model more user iteracting adding the model to a website would help.
>   2. The website can be of interactive plots and links guiding the user about investment and started guide for the same.
