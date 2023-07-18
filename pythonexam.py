import random

def main():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    game_images = [rock, paper, scissors]
    choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
    print(game_images[choose])
    com_choose = random.randint(0, 2)
    print("Computer chose :")
    print(game_images[com_choose])
    print(choose)
    print(com_choose)

    if choose >= 3 or choose < 0:
        print("fuck you")
    elif choose == 0 and com_choose == 2:
        print("you Win")
    elif com_choose == 0 and choose == 2:
        print("Computer wins!")
    elif com_choose > choose:
        print("Computer wins!")
    elif choose > com_choose:
        print("you Win")
    elif choose == com_choose:
        print("Draw")
    else:
        print(" ")

    # if choose == 0:
    #     print(rock)
    # elif choose == 1:
    #     print(paper)
    # elif choose == 2:
    #     print(scissors)



if __name__ == '__main__':
    main()
