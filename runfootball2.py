class testvariables:
    user_score = 0
    computer_score = 0
    # game_score = f"The user score is {testvariables.user_score}, and the computer score is {testvariables.computer_score}"
    globe = 1 
    def __init__(self, var=1):
        self.var = var
    def __str__(self):
        return f"The user score is {testvariables.user_score}, and the computer score is {testvariables.computer_score}"
    def increase(self):
        testvariables.user_score += 3
t1 = testvariables(2)
# print(t1.globe)
# print(testvariables.globe)
# t1.globe += 2
# print(t1.globe)
# print(testvariables.globe)
# testvariables.globe += 5
# print(t1.globe)
# print(testvariables.globe)
t1.increase()
print(t1.globe)
print(testvariables.globe)
print(t1.user_score)
print(t1)