from football_wfunctions import User

# user = user(yardline=0,possession='offense')

def game():
    print_welcome()
    play_game()

def print_welcome():
    print("Are you ready for some football??")

def get_play():
    cmd = input("Do you want to [r]un or [p]ass?")
    while cmd not in ['r','p']:
        print("Please enter one of the two letters [r] or [p] to play")
        print("To exit game, type [q] for 'quit'.")
        cmd = input("Do you want to [r]un or [p]ass?")
    return cmd    

def play_game():
    user = User(0)
    while User.time > 0:
        user.kickoff()
        print(f"You are on the {user.yardline}, 1st and 10!")
        cmd = get_play()
        while user.possession == 'offense':
            user.offense(cmd)
            if User.Touchdown == True:
                user.kickoff()
            elif user.possession == 'defense':
                user.defense()
            else:
                cmd = get_play()
        else: 
            user.defense()
            if User.Touchdown == True:
                user.kickoff() 
            elif user.possession == 'offense':
                user.offense(get_play())
            else: 
                user.defense()
game()        

# get yardline, possession, down, distance 