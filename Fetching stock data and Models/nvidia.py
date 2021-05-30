import pandas as pd
import numpy as np
import tensorflow as tf

class Nvda:
    def __init__():
        self.data = "NVIDIA_Stock.csv"
        self.model= "nvidia.h5"
        self.n_past = 10
        self.n_future = 5 
        self.n_features = 11
    def split_series(series, n_past, n_future):
      #
      # n_past ==> no of past observations
      #
      # n_future ==> no of future observations 
      #
      X, y = list(), list()
      for window_start in range(len(series)):
        past_end = window_start + n_past
        future_end = past_end + n_future
        if future_end > len(series):
          break
        # slicing the past and future parts of the window
        past, future = series[window_start:past_end, :], series[past_end:future_end, :]
        X.append(past)
        y.append(future)
      return np.array(X), np.array(y)

    def nvda_pred():
        df1=pd.read_csv(self.data)
        df = df1[list(df1)[-11:]]
        df.shape
        X,y=self.split_series(df.values,self.n_past, self.n_future)
        new_model = tf.keras.models.load_model(self.model)
        p=new_model.predict(X)
        con = [df1["date"].iloc[14:],pd.DataFrame(p[:,4,-4:],columns=list(df)[-4:],index=(list(range(14,260))))]
        pred=pd.concat(con,axis=1)
        return pred
