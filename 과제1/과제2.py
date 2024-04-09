def print_seats(seats):
    print("--------------------")
    print("1 2 3 4 5 6 7 8 9 10")
    print("--------------------")
    for row in seats:
        print(' '.join(str(seat) for seat in row))

def reserve_seat():
    seats = [[0]*10 for _ in range(10)]
    while True:
        print_seats(seats)
        row = int(input("원하는 좌석의 행번호를 입력하세요(종료는 –1): "))
        if row == -1:
            break
        col = int(input("원하는 좌석의 열번호를 입력하세요(종료는 –1): "))
        if col == -1:
            break
        if seats[row-1][col-1] == 0:
            seats[row-1][col-1] = 1
            print("예약되었습니다.")
        else:
            print("이미 예약된 좌석입니다.")

reserve_seat()