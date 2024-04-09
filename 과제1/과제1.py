def print_menu():
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구추가")
    print("3. 친구삭제")
    print("4. 이름변경")
    print("9. 종료")

def print_friends(friends):
    print('[', end=' ')
    for friend in friends:
        print(friend, end=' ')
    print(']')

def add_friend(friends):
    friend = input("이름을 입력하시오: ")
    friends.append(friend)

def delete_friend(friends):
    friend = input("삭제할 친구의 이름을 입력하시오: ")
    if friend in friends:
        friends.remove(friend)

def change_friend_name(friends):
    old_name = input("변경할 친구의 현재 이름을 입력하시오: ")
    if old_name in friends:
        new_name = input("변경할 친구의 새 이름을 입력하시오: ")
        index = friends.index(old_name)
        friends[index] = new_name
    else:
        print("이름이 발견되지 않았음")

def main():
    friends = []
    while True:
        print_menu()
        menu = input("메뉴를 선택하시오: ")
        if menu == '1':
            print_friends(friends)
        elif menu == '2':
            add_friend(friends)
        elif menu == '3':
            delete_friend(friends)
        elif menu == '4':
            change_friend_name(friends)
        elif menu == '9':
            break

main()