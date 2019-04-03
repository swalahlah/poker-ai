import random
##from pypokerengine.players import BasePokerPlayer
##from time import sleep
##import pprint 

def randomize(winrate):
    p_threshold = 0.4
    threshold = 5
    if (winrate < p_threshold):
        num = random.randint(1,100)
        if (num <= threshold):
            return valid_actions[0]["action"]
    
    return  valid_actions[1]["action"]
    
#If they check at preflop, they may show sign of weakness
def pressure(opponent_action,round_state):
    if(round_state == "preflop"): 
        if(opponent_action = valid_actions[0]["action"]):
           return valid_actions [1]["action"]


