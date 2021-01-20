import random 

class User:
    time = 1800
    user_score = 0
    computer_score = 0
    Touchdown = False
    def __init__(self, yardline, possession = 'defense', down = 1, distance = 10, sack = 0):
        self.yardline = yardline
        self.possession = possession
        self.down = down
        self.distance = distance 
        self.sack = sack
    def update_usertime(self,time):
        User.time += time
    def game_score(self):
        return f"The user score is {User.user_score}, and the computer score is {User.computer_score}"
    def end_play(self, play_type, result):
        if play_type == 'r':
            if result / 3 < self.distance:
                self.distance -= result / 3
                self.down += 1
                self.yardline += result / 3
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession = 'defense'
                    self.update_usertime(-20)
                else:
                    User.time -= result / 3 - 15
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            else:
                self.down = 1
                self.distance = 10
                self.yardline += result / 3
                User.time -= result / 3 - 15
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
        if play_type == 'p':
            if  result *.75 < self.distance:
                self.distance -= result * .75
                self.down += 1
                self.yardline += result * .75
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession = 'defense'
                    User.time -= 10
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                else:  
                    User.time -= result * .75
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            elif self.sack < 0:
                self.distance -= self.sack
                self.down += 1
                self.yardline += self.sack  
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            else:
                self.down = 1
                self.distance = 10
                self.yardline += result * .75
                User.time -= result * .75
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
    def kickoff(self):
        User.Touchdown = False
        if self.possession == 'offense':
            result = random.randint(1,100)
            print(result)
            if result <= 70:
                self.yardline = 20
                self.possession = 'defense'
                User.time -= 5
            elif result >= 99:
                print("Touchdown!")
                User.computer_score += 7
                print(self.game_score())
                User.time -= 30
                User.Touchdown = True
            else:
                self.yardline += result / 2 
                self.possession = 'defense'
                User.time -= 15
        else:
            result = random.randint(1,100)
            print(result)
            if result <= 70:
                self.yardline = 20
                self.possession = 'offense'
                User.time -= 5
            elif result >= 99:
                print("Touchdown!")
                User.user_score += 7
                print(self.game_score())
                User.time -= 30
                User.Touchdown = True
            else:
                self.yardline += result / 2 
                self.possession = 'offense'
                User.time -= 15
    def offense(self, play):
        result = random.randint(1,50)
        print(result)
        if play == 'r':
            if result <= 5:
                print("Fumble!")
                User.time -= 10
                self.possession = 'defense'
                self.down = 1
                self.distance = 10
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            elif result > 5 and result < 28:
                if result / 3 + self.yardline >= 100:
                    print("Touchdown!")
                    User.user_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.end_play(play, result) 
            elif result >= 28 and result < 45:
                if result + self.yardline >= 100:
                    print("Touchdown!")
                    User.user_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.end_play(play, result)
            else: 
                print("Touchdown!")
                User.user_score += 7
                print(self.game_score())
                User.time -= 30
                User.Touchdown = True
        if play == 'p':
            if result <= 10:
                print("Interception!")
                User.time -= 20
                self.possession = 'defense'
                self.down = 1
                self.distance = 10
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            elif result > 10 and result <= 30:
                if result + self.yardline >= 100:
                    print("Touchdown!")
                    User.user_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.end_play(play, result)
            elif result > 30 and result <= 40:
                self.down += 1
                print("Incomplete Pass")
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                User.time -= 10
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession = 'defense'
                    User.time -= 10
            elif result > 40 and result <= 45:
                self.sack = random.randint(-15,-1)
                print("QB SACK!")
                self.end_play(play, result)
                
            else: 
                print("Touchdown!")
                User.user_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True
    def defense(self):
        r_or_p = random.randint(1,50)
        if r_or_p <= 25:
            play = 'r'
            result = random.randint(1,50)
            if result <= 5:
                print("Fumble!")
                User.time -= 10
                self.possession = 'offense'
                self.down = 1
                self.distance = 10
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            elif result > 5 and result < 28:
                    if result / 3 + self.yardline >= 100:
                        print("Touchdown!")
                        User.computer_score += 7
                        print(self.game_score())
                        User.time - 30
                        User.Touchdown = True
                    else:
                       self.end_play(play, result)
            elif result >= 28 and result < 45:
                if result + self.yardline >= 100:
                    print("Touchdown!")
                    User.computer_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.end_play(play, result)
            else: 
                print("Touchdown!")
                User.computer_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True
        else:
            result = random.randint(1,50)
            play = 'p'
            if result <= 10:
                print("Interception!")
                User.time -= 20
                self.possession = 'offense'
                self.down = 1
                self.distance = 10
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
            elif result > 10 and result <= 30:
                if result + self.yardline >= 100:
                    print("Touchdown!")
                    User.computer_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.end_play(play, result)
            elif result > 30 and result <= 40:
                self.down += 1
                print("Incomplete Pass")
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                User.time -= 10
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession = 'defense'
                    User.time -= 10
            elif result > 40 and result <= 45:
                self.sack = random.randint(-15,-1)
                print("QB SACK!")
                self.end_play(play, result)
            else: 
                print("Touchdown!")
                User.computer_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True