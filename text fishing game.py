!pip install drawingletters

import random
from drawingletters import DrawingLetters

print("Welcome to Fish Hunter!")
print("물고기 크기를 맞혀보세요!\n")

score = 0

while True:
    fish_size = random.randint(3, 10)

    print("물고기가 나타났다!")

    guess = input("물고기 크기를 맞혀보세요 (그만하려면 q): ")

    if guess.lower() == 'q':
        print("게임 종료!")
        print(f"최종 점수: {score}")
        break

    if not guess.isdigit():
        print("숫자를 입력하세요!\n")
        continue

    guess = int(guess)

    if guess == fish_size:
        print("정답!! 물고기 획득!")
        print(DrawingLetters.fish(fish_size))
        score += 1
    else:
        print("틀렸습니다! 물고기가 도망갔어요!")
        print(f"(정답은 {fish_size} 였습니다)")

    print(f"현재 점수: {score}")
    print("-" * 30)
