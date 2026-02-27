import random
from drawingletters import DrawingLetters

# =============================================
# 🎣 Fish Hunter - 물고기 크기 맞추기 게임
# drawingletters 모듈을 활용한 텍스트 기반 게임
# =============================================

def get_difficulty():
    """난이도를 선택하는 함수"""
    print("난이도를 선택하세요:")
    print("  1) 쉬움  - 힌트 있음, 범위: 3~6")
    print("  2) 보통  - 힌트 없음, 범위: 3~10")
    print("  3) 어려움 - 힌트 없음, 범위: 1~15")
    
    while True:
        choice = input("선택 (1/2/3): ").strip()
        if choice == '1':
            return '쉬움', 3, 6, True
        elif choice == '2':
            return '보통', 3, 10, False
        elif choice == '3':
            return '어려움', 1, 15, False
        else:
            print("1, 2, 3 중에 선택하세요!\n")

def give_hint(guess, answer):
    """힌트를 제공하는 함수 (쉬움 난이도 전용)"""
    if guess < answer:
        print("💡 힌트: 더 크게!")
    else:
        print("💡 힌트: 더 작게!")

def show_result(score, total):
    """최종 결과를 출력하는 함수"""
    print("\n" + "=" * 35)
    print("🏆 게임 종료! 최종 결과")
    print("=" * 35)
    print(f"  총 도전 횟수 : {total}번")
    print(f"  획득한 물고기: {score}마리")
    if total > 0:
        rate = score / total * 100
        print(f"  정답률       : {rate:.1f}%")
    print("=" * 35)

    # 점수에 따라 다른 메시지 출력
    if score == 0:
        print("😢 아쉽네요! 다음엔 꼭 물고기를 잡아봐요!")
    elif score <= 3:
        print("🐟 물고기를 조금 잡았네요! 더 연습해봐요!")
    elif score <= 7:
        print("🎣 꽤 능숙한 낚시꾼이에요!")
    else:
        print("🏅 최고의 낚시왕입니다!!")

# =============================================
# 메인 게임 루프
# =============================================

print("🎣 Welcome to Fish Hunter!")
print("물고기 크기를 맞혀보세요!\n")

# 난이도 선택
difficulty, min_size, max_size, hint_mode = get_difficulty()
print(f"\n[{difficulty} 모드] 시작! 물고기 크기 범위: {min_size} ~ {max_size}\n")

score = 0   # 획득한 물고기 수
total = 0   # 총 도전 횟수

while True:
    # 랜덤으로 물고기 크기 결정
    fish_size = random.randint(min_size, max_size)
    print("🌊 물고기가 나타났다!")

    guess = input(f"물고기 크기를 맞혀보세요 ({min_size}~{max_size}, 그만하려면 q): ").strip()

    # 종료 조건
    if guess.lower() == 'q':
        show_result(score, total)
        break

    # 숫자 유효성 검사
    if not guess.isdigit():
        print("숫자를 입력하세요!\n")
        continue

    guess = int(guess)
    total += 1

    # 정답 판정
    if guess == fish_size:
        print("✅ 정답!! 물고기 획득!")
        print(DrawingLetters.fish(fish_size))  # ASCII 아트 물고기 출력
        score += 1
    else:
        print("❌ 틀렸습니다! 물고기가 도망갔어요!")
        print(f"(정답은 {fish_size} 였습니다)  {DrawingLetters.fish(fish_size)}")
        # 쉬움 난이도일 경우 힌트 제공
        if hint_mode:
            give_hint(guess, fish_size)

    print(f"현재 점수: {score} / {total}")
    print("-" * 35)
    print()
