import random
import numpy as np



def create_stack():

    stack=np.arange(1, 105)
    l_stack=list(stack)

    return l_stack

l_stack = create_stack()

def create_players():
    nb_players= input("How many players are there?")
    nb_players=int(nb_players)

    return nb_players

nb_players=create_players()

def enter_username(nb_players):

    l_users = []
    for i in range(nb_players):
        print("Name of the player %s"%format(i+1))
        l_users.append(input())

    return l_users

l_users=enter_username(nb_players)

def create_hand():

    l_hand = []

    for i in range(1, 11):
        temp = random.choice(l_stack)
        l_stack.remove(temp)
        l_hand.append(temp)

    return l_hand


def hand_for_each_player(l_users):

    d_all_hands = {}

    for i in range(len(l_users)):
        d_all_hands.update({l_users[i] : create_hand()})

    return d_all_hands

d_all_hands = hand_for_each_player(l_users)


def create_table():

    temp = []
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []

    col = []
    for i in range(4):
        rand=random.choice(l_stack)
        l_stack.remove(rand)
        temp.append(rand)

    col_1.append(temp[0])
    col_2.append(temp[1])
    col_3.append(temp[2])
    col_4.append(temp[3])

    col.append(col_1)
    col.append(col_2)
    col.append(col_3)
    col.append(col_4)

    return temp, col

visible_table, table = create_table()
print(table)
print("visible table : ", visible_table)


done = 0
while done == 0:

    print(d_all_hands)

    def choose_card():
        # test_bool = True
        #
        # while test_bool == True:

        for i in range(len(l_users)):
            print("It is %s's turn \n"%format(l_users[i]),"What card do you want to put ?")

            card_put = input()
            card_put = int(card_put)

            if card_put in d_all_hands[l_users[i]]:
                res = card_put
                d_all_hands[l_users[i]].remove(res)
                i+=1

            else:
                res = "You don't have this card"

            return res

    chosen_card = choose_card()



    def min_dist(chosen_card):

        matdist = []

        for i in visible_table:

            if i != 0:
                dist = chosen_card - i
                if dist > 0:
                    matdist.append(dist)
                else:
                    matdist.append(1000)

        min_dist = min(matdist)

        print("matdist :", matdist)

        if min_dist < 800:
            min_ind = matdist.index(min_dist)

            return min_ind

        else:
            chosen_pile=input("Choose a pile")
            chosen_pile=int(chosen_pile)

            l_temp = []
            l_temp.append(chosen_card)

            table[chosen_pile] = l_temp
            visible_table[chosen_pile] = chosen_card



    min_ind = min_dist(chosen_card)


    print("min_ind : ", min_ind)

    def add_card_to_pile(min_ind):

        if len(table[min_ind]) < 5:
            table[min_ind].append(chosen_card)
            visible_table[min_ind]=chosen_card
        else:
            l_temp = []
            l_temp.append(chosen_card)
            table[min_ind]=l_temp
            visible_table[min_ind]=chosen_card



        return table, visible_table

    table, visible_table= add_card_to_pile(min_ind)
    print("visible table :", visible_table)
    print("table :", table)




