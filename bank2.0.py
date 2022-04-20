# 1.계좌생성(아이디,비밀번호,이름,나이)
# 2.로그인
# 3.입금,출금,잔액조회,*계좌이체

from database import DB
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
    # db.get(fields,userid)

    if os.path.isfile("customerlist.data"):
        with open("customerlist.data", "rb") as f:
            idcu = pickle.load(f)
            # customer_str = f.read()
            # customer_str_list = customer_str.split('\n')
            # for customer_str in customer_str_list:
            #     if customer_str == '':
            #         continue
            #     tmp_pi_object = PI()
            #
            #     customer = customer_str.split(',')
            #
            #     tmp_pi_object.userid = customer[0]
            #     tmp_pi_object.password = customer[1]
            #     tmp_pi_object.username = customer[2]
            #     tmp_pi_object.userage = int(customer[3])
            #     tmp_pi_object.usergender = int(customer[4])
            #     tmp_pi_object.credit = int(customer[5])
            #
            #     idcu[customer[0]] = tmp_pi_object

    while True:
        os.system('cls')  # 터미널에서 페이지 클리어

        print('백모은행에 오신것을 환영합니다.')
        a = input('1.계좌생성\n2.로그인\n원하는메뉴를 선택해주세요:')
        # 계정생성
        if a == '1':
            pi_object = PI()

            while True:
                pi_object.userid = input('사용할 아이디를 입력해주세요:')

                if pi_object.userid in idcu:

                    print('아이디가 중복됩니다')

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
            # db.post()

            with open("customerlist.data", "wb") as f:
                pickle.dump(idcu, f)
                # save_pi_str = pi_object.userid + ',' + pi_object.password + ',' + pi_object.username + ',' + \
                #               pi_object.userage + ',' + pi_object.usergender + ',' + str(pi_object.credit) + '\n'
                # f.write(save_pi_str)

        # print(customerlist)
        # if username.isalpha():
        # if len(username) == 1:
        # print('이름이 너무 짧습니다.')
        # print('이름,주민번호,아이디,비밀번호입력')
        # 이름에 숫자 혹은 특수문자가 포함되어있을경우 '정확히 입력하시오' isalpha 로 true일때 ok, false일때 '정확히 입력해주세요.' 프린트...
        # 로그인
        elif a == '2':
            while True:
                userid = input('ID:')
                if userid in idcu.keys():
                    break

                else:
                    print('없는 아이디입니다')

            while True:
                password = input('PASSWORD:')
                pass_code = 0
                key_code = 0
                for key_s in key:
                    key_code += ord(key_s)
                for pass_s in password:
                    pass_code += ord(pass_s)

                if pass_code ^ key_code == idcu[userid].password:
                    break
                else:
                    print('비밀번호가 맞지않습니다')

            customer = idcu[userid]  # idcu[userid] = tmp_pi_object

            while True:
                ft = input('1.입금\n2.출금\n3.계좌이체\n4.잔액조회\n5.이전으로\n:')

                if ft == '1':

                    deposit = input('입금할 금액을 입력해주세요:')
                    if deposit.isalpha():
                        print('숫자만 입력할수있습니다')

                    else:
                        customer.credit += int(deposit)
                        with open("customerlist.data", "wb") as f:
                            pickle.dump(idcu, f)
                            # for save_object in idcu.values():
                            #     save_pi_str = save_object.userid + ',' + \
                            #                   save_object.password + ',' + \
                            #                   save_object.username + ',' + \
                            #                   str(save_object.userage) + ',' + \
                            #                   str(save_object.usergender) + ',' + \
                            #                   str(save_object.credit) + '\n'
                            #     f.write(save_pi_str)

                        # id에 맞는 credit에 새로 입력받게..
                        # id에 credit을 묶어?
                        # if 로그인때 입력받은 id 리스트의 마지막번째(credit)
                        # pop ?

                elif ft == '2':

                    withdraw = input('출금할 금액을 입력해주세요:')
                    if withdraw.isalpha():
                        print('숫자만 입력할수있습니다')

                    elif int(withdraw) > customer.credit:
                        print('잔액이 부족합니다')

                    else:
                        customer.credit -= int(withdraw)
                        with open("customerlist.data", "wb") as f:
                            pickle.dump(idcu, f)
                            # for save_object in idcu.values():
                            #     save_pi_str = save_object.userid + ',' + \
                            #                   save_object.password + ',' + \
                            #                   save_object.username + ',' + \
                            #                   str(save_object.userage) + ',' + \
                            #                   str(save_object.usergender) + ',' + \
                            #                   str(save_object.credit) + '\n'
                            #     f.write(save_pi_str)

                elif ft == '3':

                    transfer_id = input('입금받으실 분의 아이디를 입력해주세요:')
                    if transfer_id in idcu.keys():

                        while True:

                            transfer_credit = input('입금할 금액을 입력해주세요:')

                            if customer.credit < int(transfer_credit):
                                print('잔액이 부족합니다')

                            else:
                                customer.credit -= int(transfer_credit)
                                idcu[transfer_id].credit += int(transfer_credit)
                                with open("customerlist.data", "wb") as f:
                                    pickle.dump(idcu, f)
                                    # for save_object in idcu.values():
                                    #     save_pi_str = save_object.userid + ',' + \
                                    #                   save_object.password + ',' + \
                                    #                   save_object.username + ',' + \
                                    #                   str(save_object.userage) + ',' + \
                                    #                   str(save_object.usergender) + ',' + \
                                    #                   str(save_object.credit) + '\n'
                                    #     f.write(save_pi_str)
                                break

                    else:
                        print('없는 아이디 입니다')

                elif ft == '4':
                    print(customer.credit)

                elif ft == '5':
                    break

                else:
                    print('없는기능입니다')

            # if userid in customerlist: 로그인 id 를 인풋 받아서 리스트에 포함되어있나 확인..
        else:
            print('없는기능 입니다')
            break





