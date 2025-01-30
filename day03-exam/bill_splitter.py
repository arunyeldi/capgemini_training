def main():
    t = int(input())
    n = int(input())
    tip = int(input())
    money_after_tip_percent = t + (t / 100 * tip)
    print(money_after_tip_percent / n)
main()