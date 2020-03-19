from ml.random_forest import RoomRF
from ml.markov import RoomMarkov 

rf = RoomRF()

print("============ LOADING MARKOV ==============")

markov = RoomMarkov()

markov.get_top_two(0)

# train all the random forests
# train the morkov model

# get the initial room by querying all the random forests
# get request from user and get potential rooms from markov models
# query potential rooms random forests and pick the highest probability (confidence)
