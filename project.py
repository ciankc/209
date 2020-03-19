from ml.random_forest import RoomRF
from ml.markov import RoomMarkov 

rf = RoomRF()
markov = RoomMarkov()

room_to_int = {
    'officeCarp': 0,
    'hallwayCarp': 1,
    'livingCarp': 2,
    'kitchenCarp': 3,
    'bedroomCarp': 4, 
    'bathroomCarp': 5
}

int_to_room = {
    0: 'officeCarp',
    1: 'hallwayCarp',
    2: 'livingCarp',
    3: 'kitchenCarp',
    4: 'bedroomCarp',
    5: 'bathroomCarp'
}

# 1583383222
pred, prob, i = rf.get_room(1583383222, ['officeCarp', 'kitchenCarp'])

print((pred, prob, i))

print("============ LOADING MARKOV ==============")


aProb, roomA, bProb, roomB = markov.get_top_two(i)

print((int_to_room[roomA], int_to_room[roomB]))

print("============ LOADING MARKOV ==============")

# train all the random forests
# train the morkov model

# get the initial room by querying all the random forests
# get request from user and get potential rooms from markov models
# query potential rooms random forests and pick the highest probability (confidence)
