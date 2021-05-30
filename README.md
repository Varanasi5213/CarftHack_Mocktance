# CarftHack_Mocktance

## Partition of Problem Statement
> We have divided the problem statement into two parts
>   1.  A Feature extraction 
>   2.  Training Model for stock price prediction.
>   3.  Representation of the output 



## 1.  A Feature extraction

> A model to work well on such complicated data and to fit highly volatile functions, proper feature selection is important. The feature needs to provide an insight into the magnitude as well as the direction of a particular data instance.

>   1. Collection of posts regarding NVIDIA from various subreddits are collected along with their score, a number of comments, and other feature.

>   2. The features like post score, the number of comments would tell the magnitude of the post. We also need the direction that is the sentiment of the post.

>   3. Even though the feature upvote ratio tells us about the sentiment of the post, we may also need other features that depict the sentiment.

>   4. So, We have used VADER pre-trained sentiment analyzer, to get the sentiment of the post.

>   5. We have also added the corresponding stock price value for the feature set. In total, we have collected 11 features.



## 2. Training Model for stock price prediction

> We need a model that mimics the function of the stocks based on the previous behavior. This is called time series prediction, where data is time-dependent and we need to capture the underlying cyclic and direction of the time series i.e. stock price values.

>   1. The initial model we have tried on VAR (Vector Auto regressor) is a statistical model for multivariate time series prediction.

>   2. The second model is LSTM based encoder-decoder. LSTM is a specialized ANN architecture for sequential data.

>   3. The model has given a 23.9 Huber loss of the testing data. The training curves can be seen in the notebooks.



## 3.Representation of the output

> Representing the output is also important when it comes to machine learning and deep learning models.

>   1. To make our model more user interacting adding the model to a website would help.

>   2. The website can be of interactive plots and links guiding the user about investment and started guide for the same.


## Future Work
>  1.  Here we have used a static company name. The ideal solution would be using knowledge graphs to determine the company name from the post and generalizing the idea provided above.

>  2. The website can be made more responsive.
