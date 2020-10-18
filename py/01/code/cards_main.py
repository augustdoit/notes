#！ /usr/bin/python3.5

import cards_tools
while True:  # 无线循环，由用户主动决定什么时候退出循环，action_str=0 break

    # 显示功能菜单   # TODO注释 标记需要去做的工作
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是%s" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1","2","3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

         # pass  # 不希望立刻编写分支内部的代码，可以使用pass关键字，表示一个占位符，保证程序代码结构正确。

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    # 其他提示输入错误
    else:
        print("输入错误，请重新选择")