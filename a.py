#피로그래밍 17기 코딩테스트 연습

import string
import random

class Player:
    def __init__(self,name,hp,damage,conrrect_alp):
        self.name=name #이름
        self.hp=hp #생명력
        self.damage=damage #데미지
        self.correct_alp=0 #알파벳 맞춘 횟수

class Game:
    def __init__(self):
        self.player=[] #캐릭터의 목록 /start_game()에서 생성
        self.user_character="" #사용자가 선택한 캐릭터
        self.remain_alp=list(string.ascii_uppercase) #남은 알파벳
        self.cur_string=['_']*10 #현재까지의 글자상태 저장
        self.answer_string="" #랜덤 10글자

    def start_game(self):
        '''
        게임 시작 전 부분 담당 함수
        캐릭터 초기화/사용자가 플레이할 캐릭터 선택
        랜덤 알파벳 10글자로 이루어진 answer_string 생성
        동일 클래스의 game()에서 호출됨
        '''

        self.player.append(Player("오세은",50,20,0))
        self.player.append(Player("이효은",70,25,0))
        self.player.append(Player("노서연",80,30,0))
        self.player.append(Player("조은비",90,35,0))

        #사용자로부터 캐릭터를 입력받아 user_character에 저장
        #1~4 중 정수 입력 받아 if문 사용해서 user_character에 이름 저장하기
        global user_num
        while True:
            user_num=int(input("당신의 캐릭터 번호를 선택해주세요 (1,2,3,4) : "))
            if user_num==1:
                self.user_character="오세은"
                break
            elif user_num==2:
                self.user_character="이효은"
                break
            elif user_num==3:
                self.user_character="노서연"
                break
            elif user_num==4:
                self.user_character="조은비"
                break
            elif user_num<=0 or user_num>=5:
                print("잘못된 캐릭터 번호입니다. 1/2/3/4 중 하나를 다시 선택해주세요.")
            
        

        #랜덤 알파벳 10글자로 이루어진 단어를 만들어 answer_string에 저장
        random_list=random.sample(string.ascii_uppercase,10)
        self.answer_string=''.join(random_list)


    def sort_data(self,i):
        
        #게임진행을 위한 data를 재정렬
        #sort와 lambda 함수 사용
        if i==1:
            self.player.sort(key=lambda player:player.name)
        else:
            self.player.sort(key=lambda player:-player.hp)

    def play_game(self):
        print(f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        for i in range(4):
            if self.player[i].name==self.user_character:
                print("***** 내 캐릭터 *****")

            else:
                print(f"***** {i+1} 캐릭터 *****")

            print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")

            #플레이어와 컴퓨터의 차례에서는 랜덤의 알파벳 한글자를 선택하게 해주세요
            #단 앞에 나왔던 알파벳과 중복되면 안됩니다
            
            while True:   
                user_letter=input("선택 알파벳 : ")
                if user_letter in self.remain_alp:
                        if user_letter in self.remain_alp:
                            #단어 안에서 알파벳 유무 판별
                            #정답 시, 현재 맞춘 단어의 상태를 출력
                            if user_letter in self.answer_string:
                                self.player[i].correct_alp+=1
                                print("***** 맞았습니다 ᵔεᵔ  *****")
                                #print(' '.join(self.cur_string)) //확인 위한 임시 코드
                                k=0
                                for k in range(10):
                                    if user_letter==self.answer_string[k]:
                                        self.cur_string[k]=self.answer_string[k]
                                    #else 조건은 필요 없음
                                    #else:
                                    #   self.cur_string[k]="_ "

                                    k+=1
                                print(' '.join(self.cur_string))
                                print()
                            #오답 시, 생명력을 데미지만큼 감소 후 출력
                            else:
                                print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                                self.player[i].hp-=self.player[i].damage
                                print(f"{self.player[i].name}님은 틀렸기 때문에 HP가 {self.player[i].hp} 남았습니다.\n")
                                
                                
                            self.remain_alp.remove(user_letter)
                            break
                else:
                    print("잘못된 입력입니다. 확인 후 다시 입력해주세요.\n")

    def game_result(self):

        print("\n\n******************* 게임이 끝났습니다 *******************")

        #todo 4-1 생명력 순으로 결과값 출력
        #내가 선택한 캐릭터 이름 앞뒤에는 *를 붙여주세요
        #sort 와 lambda함수 사용
        for i in range(1,5,1):

            if i==user_num:
                self.player[i].name='*'+self.player[i].name+'*'

        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        #생명력 순으로 재정렬
        self.player.sort(key=lambda player:player.hp, reverse=True)
        for i in range(4):
            if self.player[i].hp<=0:
                self.player[i].hp=str(self.player[i].hp)+" >>> 사망"
        print(f"1등: {self.player[0].name} (HP: {self.player[0].hp})\n")
        print(f"2등: {self.player[1].name} (HP: {self.player[1].hp})\n")
        print(f"3등: {self.player[2].name} (HP: {self.player[2].hp})\n")
        print(f"4등: {self.player[3].name} (HP: {self.player[3].hp})\n")
        

        #todo 4-2 알파벳 맞춘 횟수 순으로 결과값 출력
        #내가 선택한 캐릭터 이름 앞뒤에는 *를 붙여주세요
        #sort 와 lambda함수 사용
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        #맞춘 횟수 순으로 재정렬
        self.player.sort(key=lambda player:player.correct_alp, reverse=True)
        print(f"1등: {self.player[0].name} {self.player[0].correct_alp}회")
        print(f"2등: {self.player[1].name} {self.player[1].correct_alp}회")
        print(f"3등: {self.player[2].name} {self.player[2].correct_alp}회")
        print(f"4등: {self.player[3].name} {self.player[3].correct_alp}회")


    def game(self):
        '''
        게임 운영을 위한 함수
        '''
        self.start_game()
        print("\n******************* 게임 시작 *******************\n")

        for i in range(1,4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")

            self.sort_data(i)
            self.play_game()

            print("===========================")
            print(f"     ROUND {i} - END")
            print("===========================")

        self.game_result()
if __name__=="__main__":
    '''
    코드를 실행하는 부분
    '''
    game = Game()
    game.game()
    result=input("게임을 다시 진행하시겠습니까?")
    #게임 진행 여부 확인 후 반복
