# made by Om Kumar 

def game():
    rock = 1
    paper = 2
    scissor = 3
    user = ""
    computer = 0
    show = 4
    win = 0 
    draw = 0
    lose = 0
    import random
    while True: 
        user = input("Enter rock, paper, scissor, show or break: ")
        computer = random.randint(1,3)

        if user.upper() == "ROCK":
            if computer == 1:
                print("Draw both are rock.")
                draw += 1
            elif computer == 2:
                print("You lose computer was paper.")
                lose += 1
            elif computer == 3:
                print("You win computer throw scissors and you smased them.")
                win += 1
            else:
                pass
        elif user.upper() == "PAPER":
            if computer == 2:
                print("Draw both are paper.")
                draw += 1
            elif computer == 3:
                print("You lose computer was scissor.")
                lose += 1
            elif computer == 1:
                print("You win computer throw rock and covered it.")
                win += 1
            else:
                pass   
        elif user.lower() == "scissor":
            if computer == 3:
                print("Draw both are scissor.")
                draw += 1
            elif computer == 1:
                print("You lose computer was rock.")
                lose += 1
            elif computer == 2:
                print("You win computer had paper and you cut it up.")
                win += 1
            else:
                pass
        elif user.lower() == "show":
            print("win:", win, "lose:", lose, "draws:", draw)
        elif user.upper() == "BREAK":
            print("Ok Byeeeeee!!!")
            print("win:", win, "lose:", lose, "draws:", draw)
            break
        else:
            print("Try again!!!")

if __name__ == '__main__':
    game()
