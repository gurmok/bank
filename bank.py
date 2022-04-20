# 1.계좌생성(아이디,비밀번호,이름,나이)
# 2.로그인
# 3.입금,출금,잔액조회,*계좌이체


class PI:

    def __init__(self):
        self.userid = ''
        self.password = ''
        self.username = ''
        self.userage = 0
        self.usergender = 0


pi_object = PI()

f = open("C:\stock\customerlist.txt", "w")

customerlist = []
while True:
    print('은행에 오신것을 환영합니다.')

    a = input('1.계좌생성\n2.로그인\n원하는메뉴를 선택해주세요:')

    # 계정생성
    if a == '1':
        while True:

            pi_object.userid = input('사용할 아이디를 입력해주세요:')

            if pi_object.userid.isalnum():
                customerlist.append(pi_object.userid)
                break
            else:
                print('아이디에 특수문자는 사용이 불가능합니다.')

        while True:

            pi_object.password = input('비밀번호를 입력해주세요.(특수문자 및 숫자 포함 8자리이상):')
            if len(pi_object.password) <= 7:
                print('8자리 이상 입력하지않으셨습니다.')

            else:
                customerlist.append(pi_object.password)
                break

        while True:

            pi_object.username = input('이름을 입력해주세요:')
            pi_object.username.isalpha()

            if not pi_object.username.isalpha():
                print('이름을 정확히 입력해주세요.')

            elif len(pi_object.username) == 1:
                print('이름이 너무 짧습니다.')

            else:
                customerlist.append(pi_object.username)
                break

        while True:
            pi_object.userage = input('주민번호 앞7자리를 입력해주세요:')
            if len(pi_object.userage) == 7:
                customerlist.append(pi_object.userage)
                break
            else:
                print('7자리를 입력받지 못했습니다.')

        pi_object.usergender = pi_object.userage[-1]

        f.write(','.join(customerlist))

    # print(customerlist)

    # if username.isalpha():
    # if len(username) == 1:
    # print('이름이 너무 짧습니다.')

    # print('이름,주민번호,아이디,비밀번호입력')
    # 이름에 숫자 혹은 특수문자가 포함되어있을경우 '정확히 입력하시오' isalpha 로 true일때 ok, false일때 '정확히 입력해주세요.' 프린트...

    # 로그인
    elif a == '2':
        userid = input('ID:')
        # if userid in customerlist: 로그인 id 를 인풋 받아서 리스트에 포함되어있나 확인..
    else:
        print('없는기능 입니다.')
        break
