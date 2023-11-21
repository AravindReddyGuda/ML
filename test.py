import numpy as np
import scipy.misc as sc
from sklearn import datasets 
from sklearn import metrics 
from sklearn.tree import DecisionTreeClassifier 
# import theano 
# import theano.tensor as T 
# import tensorflow as tf
# import keras as ke
# import pytorch as pt
import pandas as pd
import matplotlib as mp











def fibonacci(n, num1, num2, next_number, count):
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()


n = 10
num1 = 0
num2 = 1
next_number = num2 
count = 1

fibonacci(n, num1, num2, next_number, count)