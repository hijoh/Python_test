print('欢迎来到黑马儿童游乐园，儿童免费，成人收费10元')
age = int(input('请输入你的年龄：'))

if age >= 18:
    print('您已成年，游玩需要购票10元。')
    choice = input('继续游玩吗？(是/否)')
    if choice == '是':
        chance = 3  # 设置3次机会
        while chance > 0:
            payment = int(input('请付款10元：'))
            if payment == 10:
                print('付款成功，祝您游玩愉快！')
                break
            else:
                chance -= 1
                if chance > 0:
                    print(f'付款失败了')
                    retry_choice = input('是否继续？(是/否)')
                    if retry_choice != '是':
                        print('祝您下次游玩愉快！')
                        break
                else:
                    print('很抱歉，设备受限，请联系工作人员。')
                    print('谢谢光临，欢迎下次来玩。')
                    break
    else:
        print('祝您下次游玩愉快！')
else:
    print('欢迎小朋友来玩，结束还送python C++ C语言 java web前端 HTML linux等等编程教学')
    print('祝你游玩和学习编程更加愉快！')
