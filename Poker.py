import random as r

deck = ["♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "◆A", "◆2", "◆3", "◆4", "◆5", "◆6", "◆7", "◆8", "◆9", "◆10", "◆J", "◆Q", "◆K", "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K"]
tu_deck = ("♠A", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠J", "♠Q", "♠K", "◆A", "◆2", "◆3", "◆4", "◆5", "◆6", "◆7", "◆8", "◆9", "◆10", "◆J", "◆Q", "◆K", "♥A", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥J", "♥Q", "♥K", "♣A", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣J", "♣Q", "♣K")

j = 52

user1_money = 10000  #사용자의 초기 금액
user2_money = 10000

def bet():
    global user1_money, user2_money
    #user1이 먼저 배팅한다고 하자
    print("Min Bet is 1000")
    min_bet = 1000
    
    while(True):  #user1 배팅하기
        user1_bet = int(input("user1 Bet Amount : "))
        if user1_bet >= 1000 and user1_bet <= user1_money:
            break
        elif user1_bet == 0:
            print("You Fold")
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

    total_bet = user1_bet #fold가 안나왔을 때의 경우 / fold가 나오면 게임을 끝내야함 or fold한 사람만 끝내야함


    print(f"user1_mon : {user1_money}, user2_mon : {user2_money}, user1_bet : {user1_bet}, user2_bet : {user2_bet}, total_bet : {total_bet}")


def hand(turn):
    global j
    if turn == 1:
        for i in range(0, 4):  #첫번째 턴에 4장을 공개한다. 
            user1.append(deck.pop(r.randint(0, j)))
            j -= 1
            user2.append(deck.pop(r.randint(0, j)))
            j -= 1
    else:  #카드 한장씩을 추가한다. 
        user1.append(deck.pop(r.randint(0, j)))
        j -= 1
        user2.append(deck.pop(r.randint(0, j)))
        j -= 1
    print(f"user1 : {user1}") #사용자의 패 공개
    print(f"user2 : {user2}")
        

def result(user):
    user.sort() #오름차순 정렬
    for i in range(0, 52, 13): #로얄 스트레이트 플러쉬
        if i in user and i + 9 in user and i + 10 in user and i + 11 in user and i + 12 in user:
            if i == 0:
                return 0
            elif i == 13:
                return 1
            elif i == 26:
                return 2
            elif i == 39:
                return 3
    '''
    if 0 in user and 9 in user and 10 in user and 11 in user and 12 in user:
        #스페이드 로얄 스트레이트 플러쉬
        return 0
    elif 13 in user and 21 in user and 22 in user and 23 in user and 24 in user:
        #다이아 로얄 스트레이트 플러쉬
        return 1
    elif 26 in user and 35 in user and 36 in user and 37 in user and 38 in user:
        #하트 로얄 스트레이트 플러쉬
        return 2
    elif 39 in user and 48 in user and 19 in user and 50 in user and 51 in user:
        #클로버 로얄 스트레이트 플러쉬
        return 3
    '''
    for i in range (0, 52, 13): #백스트레이트 플러쉬
        if i in user and i + 1 in user and i + 2 in user and i + 3 in user and i + 4 in user:
            if i == 0:
                return 4
            elif i == 13:
                return 5
            elif i == 26:
                return 6
            elif i == 39:
                return 7

    for i in range(1, 10): #스트레이트 플러쉬
        for k in range (0, 52, 13):
            if (i - 1) + k in user and i + k in user and (i + 1) + k in user and (i + 2) + k in user and (i + 3) + k in user:
                if k == 0:
                    return 8
                elif k == 13:
                    return 9
                elif k == 26:
                    return 10
                elif k == 39:
                    return 11


    for i in range(0, 13): #포카드
        if i in user and i + 13 in user and i + 26 in user and i + 39 in user:
            return 12

    for i in range(5, 0, -1):
        for k in range (0, 6):
            if i > k:
                if user[i] - user[k] == 13 or user[i] - user[k] == 26 or user[i] - user[k] == 39: #원페어
                    for l in range(0, 6):
                        if l != k:
                            if user[i] - user[l] == 13 or user[i] - user[l] == 26 or user[i] - user[l] == 39: #3장 같음
                                print("3장이 같다")
                            

                
    
    


# The number of players is fixed at 2

user1 = []
user2 = []

hand(1) #첫번째 패 분배 후 공개

n = int(input("user1 버릴 카드의 위치를 고르시오. ")) #사용자의 패 중 한장을 버림
print(f"버리는 user1: {user1.pop(n - 1)}")
n = int(input("user2 버릴 카드의 위치를 고르시오. "))
print(f"버리는 user2 : {user2.pop(n - 1)}")

print(f"user1 : {user1}") #한장을 버리고 남아있는 사용자의 패
print(f"user2 : {user2}")

bet()  #1차 배팅

hand(2)
hand(2) #2번째 패 분배, 오픈두장씩 추가하기

bet() #2차 배팅

hand(3) #3번째 패 분배, 히든한장씩 추가하기

bet() #3차 배팅

print(user1)
print(user2)

user1_result = []  
user2_result = []
for i in range(0, 6):
    user1_result.append(tu_deck.index(user1[i]))
    user2_result.append(tu_deck.index(user2[i]))
'''
print(f"user1 : {result(user1_result)}")
print(f"user2 : {result(user2_result)}")
'''



















