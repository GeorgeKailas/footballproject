import random 

class User:
    time = 1800
    user_score = 0
    computer_score = 0
    Touchdown = False
    def __init__(self, yardline, possession = 'defense', down = 1, distance = 10):
        self.yardline = yardline
        self.possession = possession
        self.down = down
        self.distance = distance 
    def game_score(self):
        return f"The user score is {User.user_score}, and the computer score is {User.computer_score}"
    def end_play(self, play_type, result):
        if play_type == 'r':
            if self.distance - result / 3:
                self.distance -= result / 3
                self.down += 1
                self.yardline += result / 3
                User.time -= result / 3 - 15
            else:
                self.down = 1
                self.distance = 10
                self.yardline += result / 3
                User.time - result / 3 - 15
        if play_type == 'p':
            self.distance -= result * .75
            self.down += 1
            self.yardline += result * .75
    def kickoff(self):
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
                User.time - 30
                User.Touchdown = True
            else:
                self.yardline += result / 2 
                self.possession = 'defense'
                User.time - 15
        else:
            result = random.randint(1,100)
            print(result)
            if result <= 70:
                self.yardline = 20
                self.possession = 'offense'
                User.time - 5
            elif result >= 99:
                print("Touchdown!")
                User.user_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True
            else:
                self.yardline += result / 2 
                self.possession = 'offense'
                User.time - 15
    def offense(self, play):
        result = random.randint(1,50)
        print(result)
        if play == 'r':
            if result <= 5:
                print("Fumble!")
                User.time - 10
                self.possession == 'defense'
            elif result > 5 and result < 28:
                if result / 3 < self.distance:
                    self.end_play(play, result)
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                    if self.down == 5:
                        print("Turnover on downs!")
                        User.time - 30
                        self.possession == 'defense'
                else: 
                    if result / 3 + self.yardline >= 100:
                        print("Touchdown!")
                        User.user_score += 7
                        print(self.game_score())
                        User.time - 30
                        User.Touchdown = True
                    else:
                        self.distance = 10
                        self.down = 1
                        self.yardline += result / 3 
                        User.time - 30
            elif result >= 28 and result < 45:
                if result / 2 < self.distance:
                    self.distance - result
                    self.down += 1
                    self.yardline += result / 2 
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                    if self.down == 5:
                        print("Turnover on downs!")
                        self.possession == 'defense'
                        User.time - 30
                if result + self.yardline >= 100:
                    print("Touchdown!")
                    User.user_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.distance = 10
                    self.down = 1
                    self.yardline += result / 2
                    User.time - 4
            else: 
                print("Touchdown!")
                User.user_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True
        if play == 'p':
            if result <= 10:
                print("Interception!")
                User.time - 20
                self.possession == 'defense'
            elif result > 10 and result <= 30:
                if result < self.distance:
                    self.distance - result * .75
                    self.down += 1
                    self.yardline + result  * .75
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                    if self.down == 5:
                        print("Turnover on downs!")
                        User.time - 15
                        self.possession == 'defense'
                else: 
                    if result + self.yardline >= 100:
                        print("Touchdown!")
                        User.user_score += 7
                        print(self.game_score())
                        User.time - 30
                        User.Touchdown = True
                    else:
                        self.distance = 10
                        self.down = 1
                        self.yardline + result * .75
                        User.time - 45
            elif result > 30 and result <= 40:
                self.down += 1
                print("Incomplete Pass")
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                User.time - 10
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession == 'defense'
                    User.time - 10
            elif result > 40 and result <= 45:
                sack = random.randint(-15,-.5)
                print("QB SACK!")
                self.distance - sack
                self.down += 1
                self.yardline + sack  
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession == 'defense'
                    User.time - 30
            else: 
                print("Touchdown!")
                User.user_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True
    def defense(self):
        r_or_p = random.randint(1,50)
        if r_or_p <= 25:
            result = random.randint(1,50)
            if result <= 5:
                print("Fumble!")
                User.time - 10
                self.possession == 'defense'
            elif result > 5 and result < 28:
                if result / 3 < self.distance:
                    self.end_play('r', result)
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                    if self.down == 5:
                        print("Turnover on downs!")
                        User.time - 30
                        self.possession == 'defense'
                else: 
                    if result / 3 + self.yardline >= 100:
                        print("Touchdown!")
                        User.computer_score += 7
                        print(self.game_score())
                        User.time - 30
                        User.Touchdown = True
                    else:
                        self.distance = 10
                        self.down = 1
                        self.yardline += result / 3 
                        User.time - 30
            elif result >= 28 and result < 45:
                if result / 2 < self.distance:
                    self.distance - result
                    self.down += 1
                    self.yardline += result / 2 
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                    if self.down == 5:
                        print("Turnover on downs!")
                        self.possession == 'defense'
                        User.time - 30
                if result + self.yardline >= 100:
                    print("Touchdown!")
                    User.computer_score += 7
                    print(self.game_score())
                    User.time - 30
                    User.Touchdown = True
                else:
                    self.distance = 10
                    self.down = 1
                    self.yardline += result / 2
                    User.time - 4
            else: 
                print("Touchdown!")
                User.computer_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True
        else:
            result = random.randint(1,50)
            if result <= 10:
                print("Interception!")
                User.time - 20
                self.possession == 'defense'
            elif result > 10 and result <= 30:
                if result < self.distance:
                    self.distance - result * .75
                    self.down += 1
                    self.yardline + result  * .75
                    print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                    if self.down == 5:
                        print("Turnover on downs!")
                        User.time - 15
                        self.possession == 'defense'
                else: 
                    if result + self.yardline >= 100:
                        print("Touchdown!")
                        User.computer_score += 7
                        print(self.game_score())
                        User.time - 30
                        User.Touchdown = True
                    else:
                        self.distance = 10
                        self.down = 1
                        self.yardline + result * .75
                        User.time - 45
            elif result > 30 and result <= 40:
                self.down += 1
                print("Incomplete Pass")
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                User.time - 10
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession == 'defense'
                    User.time - 10
            elif result > 40 and result <= 45:
                sack = random.randint(-15,-.5)
                print("QB SACK!")
                self.distance - sack
                self.down += 1
                self.yardline + sack  
                print(f"It's {self.down} and {self.distance} at the {self.yardline} yardline and {self.possession}")
                if self.down == 5:
                    print("Turnover on downs!")
                    self.possession == 'defense'
                    User.time - 30
            else: 
                print("Touchdown!")
                User.computer_score += 7
                print(self.game_score())
                User.time - 30
                User.Touchdown = True