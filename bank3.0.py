# 1.계좌생성(아이디,비밀번호,이름,나이)
# 2.로그인
# 3.입금,출금,잔액조회,*계좌이체

from database2 import DB
import os
import pickle
import getpass  # 비밀번호 안보이게 받기


key = "asdfqwerdry3489ruh3q89wefuhasdiuf923`u42389fhesdklf"


class PI:
    def __init__(self):
        self.userid = ''
        self.password = ''
        self.username = ''
        self.userage = 0
        self.usergender = 0
        self.credit = 0


customerlist = list()
idcu = dict()

if __name__ == '__main__':

    # 프로그램 초기화 부분
    db = DB()
    # db.get()  # 데이터를 먼저 읽어올 필요가 있나? - id 중복검사 때문에 먼저 읽을필요 있음

    while True:
        os.system('cls')  # 터미널에서 페이지 클리어

        print('은행에 오신것을 환영합니다.')
        a = input('1.계좌생성\n2.로그인\n원하는메뉴를 선택해주세요:')
        # 계정생성
        if a == '1':
            pi_object = PI()

            while True:
                pi_object.userid = input('사용할 아이디를 입력해주세요:')

                # values.append = input  /values리스트 생성..?

                if pi_object.userid in db.get(fields=['userid'], userid=None):

                    print('아이디가 중복됩니다')

                    # values[0] in /select 'userid' from 'PI'/

                elif pi_object.userid.isalnum():
                    break

                else:
                    print('아이디에 특수문자는 사용이 불가능합니다')

            while True:
                pi_object.password = getpass.getpass('비밀번호를 입력해주세요(특수문자 및 숫자 포함 8자리이상):')
                if len(pi_object.password) <= 7:
                    print('8자리 이상 입력하지않으셨습니다')
                else:
                    pass_code = 0
                    key_code = 0
                    for key_s in key:
                        key_code += ord(key_s)
                    for pass_s in pi_object.password:
                        pass_code += ord(pass_s)

                    pi_object.password = pass_code ^ key_code
                    break
            while True:
                pi_object.username = input('이름을 입력해주세요:')
                pi_object.username.isalpha()
                if not pi_object.username.isalpha():
                    print('이름을 정확히 입력해주세요')
                elif len(pi_object.username) == 1:
                    print('이름이 너무 짧습니다')
                else:
                    break
            while True:
                pi_object.userage = input('주민번호 앞7자리를 입력해주세요:')
                if len(pi_object.userage) == 7:
                    break
                else:
                    print('7자리를 입력받지 못했습니다')
            pi_object.usergender = pi_object.userage[-1]

            idcu[pi_object.userid] = pi_object

        # print(customerlist)
        # if username.isalpha():
        # if len(username) == 1:
        # print('이름이 너무 짧습니다.')
        # print('이름,주민번호,아이디,비밀번호입력')
        # 이름에 숫자 혹은 특수문자가 포함되어있을경우 '정확히 입력하시오' isalpha 로 true일때 ok, false일때 '정확히 입력해주세요.' 프린트...

        # 로그인
        elif a == '2':
            while True:
                login_userid = input('ID:')
                login_password = input('PASSWORD:')

                db_data = db.get(fields=['password', 'name', 'credit'], userid=login_userid)

                if len(db_data) <= 0:
                    print('없는 아이이디 입니다.')

                else:
                    if db_data[0]['password'] != login_password:
                        print('잘못된 패스워드 입니다.')

                    else:
                        break

            while True:
                tf = input('1.입금\n2.출금\n3.계좌이체\n4.잔액조회\n5.이전으로\n:')

                if tf == '1':

                    deposit = input('입금할 금액을 입력해주세요:')
                    if deposit.isalpha():
                        print('숫자만 입력할수있습니다.')

                    else:
                        user_credit = db.get(fields=['credit'], userid=login_userid)
                        credit = int(user_credit[0]["credit"]) + int(deposit)
                        db.put(field='credit', value=credit, userid=login_userid)

                        print(f'입금이 완료되었습니다.\n현재잔액:{int(credit)}원')

                elif tf == '2':

                    withdraw = input('출금할 금액을 입력해주세요:')
                    if withdraw.isalpha():
                        print('숫자만 입력할수있습니다.')

                    else:
                        user_credit = db.get(fields=['credit'], userid=login_userid)
                        if int(user_credit[0]['credit']) < int(withdraw):
                            print('잔액이 부족합니다.')

                        else:
                            credit = int(user_credit[0]['credit']) - int(withdraw)
                            db.put(field='credit', value=credit, userid=login_userid)
                            print(f'출금이 완료되었습니다.\n현재잔액:{int(credit)}원')

                elif tf == '3':

                    transfer_id = input('입금받으실 분의 아이디를 입력해주세요:')

                    sender = db.get(fields=['credit'], userid=login_userid)
                    receiver = db.get(fields=['credit'], userid=transfer_id)

                    if len(receiver) <= 0:
                        print('없는 아이디입니다.')

                    else:
                        transfer_credit = input("입금할 금액을 입력해주세요:")

                        if int(sender[0]['credit']) < int(transfer_credit):
                            print('잔액이 부족합니다.')

                        else:
                            sender_credit = int(sender[0]['credit']) - int(transfer_credit)
                            receiver_credit = int(receiver[0]['credit']) + int(transfer_credit)

                            db.put(field='credit', value=sender_credit, userid=login_userid)
                            db.put(field='credit', value=receiver_credit, userid=transfer_id)
                            print(f'입금이 완료되었습니다.\n현재잔액:{int(sender_credit)}원')

                    # if transfer_id in idcu.keys():
                    #
                    #     while True:
                    #
                    #         transfer_credit = input('입금할 금액을 입력해주세요:')
                    #
                    #         if customer.credit < int(transfer_credit):
                    #             print('잔액이 부족합니다')
                    #
                    #         else:
                    #             customer.credit -= int(transfer_credit)
                    #             idcu[transfer_id].credit += int(transfer_credit)
                    #             with open("customerlist.data", "wb") as f:
                    #                 pickle.dump(idcu, f)
                    #                 # for save_object in idcu.values():
                    #                 #     save_pi_str = save_object.userid + ',' + \
                    #                 #                   save_object.password + ',' + \
                    #                 #                   save_object.username + ',' + \
                    #                 #                   str(save_object.userage) + ',' + \
                    #                 #                   str(save_object.usergender) + ',' + \
                    #                 #                   str(save_object.credit) + '\n'
                    #                 #     f.write(save_pi_str)
                    #             break
                    #
                    # else:
                    #     print('없는 아이디 입니다')

                elif tf == '4':
                    credit = db.get(fields=['credit'], userid=login_userid)
                    print(f'잔액: {credit[0]["credit"]}원')

                elif tf == '5':
                    break

                else:
                    print('없는 기능 입니다.')

            # if userid in customerlist: 로그인 id 를 인풋 받아서 리스트에 포함되어있나 확인..
        else:
            print('없는 기능 입니다.')
            break


