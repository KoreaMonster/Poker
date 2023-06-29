import random as r

deck = ["♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "◆A", "◆2", "◆3", "◆4", "◆5", "◆6", "◆7", "◆8", "◆9", "◆10", "◆J", "◆Q", "◆K", "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K"]
tu_deck = ("♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "◆A", "◆2", "◆3", "◆4", "◆5", "◆6", "◆7", "◆8", "◆9", "◆10", "◆J", "◆Q", "◆K", "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K")

def bet (user1_money, user2_money):
    #user1이 먼저 배팅한다고 하자
    print("Min Bet is 1000")
    min_bet = 1000
    
    while(True):  #user1 배팅하기
        user1_bet = int(input("user1 Bet Amount : "))
        if user1_bet >= 1000 and user1_bet <= user1_money:
            break
        else:
            print("Bet Again")
    user1_money -= user1_bet
    
    while(True):  #user2 배팅하기
        user2_bet = int(input("user2 Bet Amount : "))
        if user2_bet == 0:
            print("You Fold")
            user1_money = user1_money + user1_bet + min_bet
            user2_money = user2_money - min_bet
            break
        elif user1_bet > user2_bet and user2_bet > user2_money:
            print("Bet Again")
        elif user1_bet <= user2_bet:
            break
    user2_money -= user2_bet

    if user2_bet > user1_bet: #user1의 마지막 배팅
        u = int(input(f"{user2_bet - user1_bet} 더 배팅하시겠습니까? [Yes(1) / Fold(0)] "))
        if u == 1:
            user1_money = user1_money - (user2_bet - user1_bet)
            user1_bet = user2_bet
        elif u == 0:
            print("You Fold")
            user2_money = user2_money + user1_bet + user2_bet
        else:
            print("다시 고르시오")


    print(f"user1_mon : {user1_money}, user2_mon : {user2_money}, user1_bet : {user1_bet}, user2_bet : {user2_bet}")




# The number of players is fixed at 2 for now

user1 = []
user2 = []

j = 52

for i in range(0, 4):
    user1.append(deck.pop(r.randint(0, j)))
    j -= 1
    user2.append(deck.pop(r.randint(0, j)))
    j -= 1 

print(user1)
print(user2)
print(deck)

user1_money = 10000
user2_money = 10000
bet(user1_money, user2_money)
