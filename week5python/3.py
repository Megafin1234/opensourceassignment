coffee=0 #전역 변수 coffee

def coffee_machine(button) : #지역 변수 button
    print()
    print("#1. (자동으로)뜨거운 물을 준비한다.")
    print("#2. (자동으로)종이컵을 준비한다.")
    if button==1 :
        print("#3. 카페라떼를 탄다")
    elif button==2 :
        print("#3. 카푸치노를 탄다")
    elif button==3 :
        print("#3. 에스프레소를 탄다")
    elif button==4 :
        print("#4. 아메리카노를 탄다")
    else :
        print("#3. 아무거나 탄다. \n")
    print("#4. 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")
    print()

coffee=int(input("로제, 어떤 커피를 드릴까요?(1.카페라떼 2.카푸치노 3.에스프레소 4. 아메리카노:)"))
coffee_machine(coffee)
print("로제~여기 커피 있습니다.")

coffee=int(input("리사, 어떤 커피를 드릴까요?(1.카페라떼 2.카푸치노 3.에스프레소 4.아메리카노:)"))
coffee_machine(coffee)
print("리사~여기 커피 있습니다.")

coffee=int(input("지수, 어떤 커피를 드릴까요?(1.카페라떼 2.카푸치노 3.에스프레소 4.아메리카노:)"))
coffee_machine(coffee)
print("지수~여기 커피 있습니다.")

coffee=int(input("제니, 어떤 커피를 드릴까요?(1.카페라떼 2.카푸치노 3.에스프레소 4.아메리카노:)"))
coffee_machine(coffee)
print("제니~여기 커피 있습니다.")