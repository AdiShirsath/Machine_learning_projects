# Intent Predictor

This is Natural Language Processing project. We are classifying intent of input sentence into two categories `Departure Time` or `Finding Connection`.

## Data:-
Data contains 209 sentences with their respective intent. Now we have nearly 80 sentences with Departure Time intent and 120+ Finding Connection.

## Training 

### Training LSTM models:-
Code for this is in Training_LSTM.ipynb notebook.

| Models  |Model Description                                           |Validation Score|   
|---------|------------------------------------------------------------|----------------| 
| Model1  | Embedding(50) + LSTM(50) +1 Dense(64)                      |    88.09%      |
| Model2  | Embedding(50) + LSTM(50) +1 Dense(64)                      |    92.86%      |       
| Model3  | Embedding(50) + LSTM(50) +2 Dense(64)                      |    95.23%      |    
| Model4  | Embedding(50) + LSTM(100) +2 Dense(64)                     |    95.24%      |     
| Model5  | Embedding(50) + 2 LSTM(50) +2 Dense(64)                    |    90.48%      |    
|***Model6***  | Embedding(500) + Bi-LSTM(100)+ LSTM(100) +2 Dense(128 & 64)|    97.62%      |       
| Model7  | Embedding(500) + Bi-LSTM(100) +2 Dense(256 & 128)          |    95.38%      |    
| Model8  | Embedding(500) + Bi-LSTM(100)+2 Dense(512 & 128)           |    97.48%      |       
| Model9  | Embedding(500) + Bi-LSTM(500) +1 Dense(512 & 128)          |    96.50%      |    

***Model 6 was the bestt model which is also used in API***.

### Training Bert:-
I have used Tensorflow Hub for training Bert. Code for this is present in Training_Bert File.

| Models  |Model Description                                           |Validation Score|   
|---------|------------------------------------------------------------|----------------| 
| Bert1   | bert_Processor +  Bert Encoder                             |    64.28%      |
| Bert2   | bert_Processor +  Bert Encoder + Dense(128)                |    92.85%      |
| Bert2   | bert_Processor +  Bert Encoder + 2 Dense(128 & 64)         |    95.24%      |
| Bert4   | Fintune Bert + Dense(128)                                  |    61.90%      |
