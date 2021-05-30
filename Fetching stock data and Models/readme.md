## Predictive Model

**Descreption**
> The idea is to add stock values according to the date of NVIDIA and make predictions.

**Work Details**
1. _NvidiaStock_ notebook will fetch the stock values (openning,clossing,high,low,etc.) from Yahoo Finance module.
2. These values are addded to the previous data set that is _NVIDIA_sent1.csv_.
3. _vda (1)_ notebook is implementation of Vector Auto Regression (VAR) on the stocks data set.
4._LSTM_STOCK (1)_ model consists of a 2 layer encoder and 2 layer decoder model.
5. The model takes 10 days as input and predcits the output of next five days.
6. The mode gave 23.9 Huber loss on test data andsaved the model in h5 file format.
7. _nvidia.py_ file is a class containing the function to predict the model ouput and integrate with DJango framework.
