from ml.random_forest import RoomRF
from ml.markov import RoomMarkov 

rf = RoomRF()
markov = RoomMarkov()
rf.evaluate_model()

room_to_int = {
    'officeCarp': 0,
    'livingCarp': 1,
    'kitchenCarp': 2,
    'bedroomCarp': 3, 
    'bathroomCarp': 4
}

int_to_room = {
    0: 'officeCarp',
    1: 'livingCarp',
    2: 'kitchenCarp',
    3: 'bedroomCarp',
    4: 'bathroomCarp'
}

# 1583383222
t = 1583383222 % 86400
# pred, prob, i = rf.get_room(t, ['officeCarp', 'kitchenCarp'])
pred, prob, i = rf.get_room(t)

print((pred, prob, int_to_room[i]))

print("============ LOADING MARKOV ==============")


aProb, roomA, bProb, roomB = markov.get_top_two(i)

print((int_to_room[roomA], aProb, int_to_room[roomB], bProb))

print("============ LOADING MARKOV ==============")

# train all the random forests
# train the morkov model

# get the initial room by querying all the random forests
# get request from user and get potential rooms from markov models
# query potential rooms random forests and pick the highest probability (confidence)
