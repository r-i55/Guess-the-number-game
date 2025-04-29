import random

print('ゲームスタート！')
n = int(input('最小値を入力してください: '))
m = int(input('最大値を入力してください: '))

while n > m:
    n = int(input('もう１度最小値を入力してください'))
    m = int(input('もう１度最大値を入力してください'))

number = random.randint(n, m)
count = 0

while(count <= 4):
    temp = int(input(f'{n}から{m}までの数字を入力してください')) 
    if number == temp :
        print('おめでとう！正解です！')
        break
    else:
        print('残念！もう１回入力してみてね')
        count += 1
else:
    print('ゲーム終了です!正解は', number, 'でした')

