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

rooms = ['officeCarp', 'hallwayCarp','livingCarp','kitchenCarp','bedroomCarp','bathroomCarp']

print('\n\n')

while True:
    tin = input("Please enter a unix time stamp (eg. 1583383222): ")
    t = int(tin)
    pred, prob, i = rf.get_room(t, rooms)
    print("=========== RF result =============")
    print((pred, prob, int_to_room[i]))
    print("========== MARKOV result ==========")
    aProb, roomA, bProb, roomB = markov.get_top_two(i)
    print((int_to_room[roomA], aProb, int_to_room[roomB], bProb))
    rooms = [int_to_room[roomA], int_to_room[roomB]]


# get the initial room by querying all the random forests
# get request from user and get potential rooms from markov models
# query potential rooms random forests and pick the highest probability (confidence)
