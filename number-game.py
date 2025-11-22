import random

print("乱数当てゲームを始めます！")

number_min = int(input("最小値を入力してね\n"))
print("最小値は " + str(number_min) + " です")
number_max = int(input("最大値を入力してね\n"))

if number_max <= number_min :
    print("最大値は最小値よりも大きい数字である必要があります")
    number_max = int(input("最大値を入力してね\n"))
else:
    print("最大値は " + str(number_max) + " です")


random_number = random.randint(number_min, number_max)


for index in range(3):
    num = int(input("乱数を予想して入力してね\n"))
   
    if num == random_number:
        print("正解です！")
        break

    if index == 2:
        print("残念！また挑戦してみてね")
    else:
        print("もう１度予想してみよう")


    

    
