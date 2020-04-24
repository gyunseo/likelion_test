#2019311801이균서

import re#refindall 함수를 사용하기 위하여

#Node 클래스
class Node:
    def __init__(self,data):

        self.data=data
        self.next=None #다음을 지목하는 주소 값

#List 클래스
class List:
    def __init__(self):#create 모듈의 역할
        self.head=Node("DUMMY")
        self.cur=self.head#current 노드를 head로 설정
        self.before=None#더미노드의 before노드는 아직 없으므로 None으로 지정
        self.n=0#노드의 개수
        self.pos=-1#더미노드의 position은 -1로 설정
    
    def add(self, data):# addTail과 add 모듈을 add라는 모듈로 통합, '+' 명령어
        new_node=Node(data)#새로운 노드 생성



        if self.cur.next==None:#가장 마지막 노드에서 append하는 거면

            self.cur.next=new_node#가장 최신의 노드의 next가 새로운 노드의 주소를 가리키게 함

            self.before=self.cur#before노드를 cur노드로 update함

            self.cur=new_node#current node의 주소를 새로운 주소로 update함
        
            self.n=self.n+1#노드 개수+1
            self.pos=self.pos+1#position ++

        else:#노드를 중간에 insert하는 거면
            
            new_node.next=self.cur.next#새로운 node의 next를 current node의 next로 업데이트함
            self.cur.next=new_node#current node의 next를 새로운 node로 업데이트함

            self.before=self.cur#before 노드를 current node로 업데이트 함
            self.cur=new_node#current node를 new node로 업데이트

            self.n=self.n+1#노드 개수+1
            self.pos=self.pos+1#position ++
        
    def PRINT(self):#print 모듈, 'L' 명령어
        
        if self.head.next==None:
            print("Error!Add a node!")

        else:
            i=self.head.next

            while True:
                print(i.data,end=' ')

                if i.next==None:
                    print()
                    break
                else:
                    i=i.next#i를 다음 노드로 업데이트
    
    def get_data(self):

        if self.head.next==None:
            print(self.head.data)
        else:
            print(self.cur.data)

    def traverse_front(self):#'<'명령어 구현, 'N'과 'P' 명령어를 따로 구현하기 위해 count 매개변수를 선언하지 않음

        if self.head.next==None:
            print("Error!Current position is dummy node[-1]!")
        else:
            self.cur=self.head.next#더미 노드의 다음 노드를 current node로 업데이트
            self.before=self.head#before node를 더미 노드로 업데이트
            self.pos=0#current position은 0으로 업데이트
    
    def move_next(self):#'N'명령어 구현

        if self.cur.next==None:
            print("Error!Cannot move to next node!")
        else:
            self.before=self.cur#before node를 현재의 current node로 업데이트
            self.cur=self.cur.next#current node를 현재의 current node.next로 업데이트
            self.pos=self.pos+1#pos++

    
    def ShowCurrentState(self):#가장 최신의 상태를 보여주는 함수

        print("Current State:")

        if self.head.next==None:

            print("Position= -1, No element")
        else:

            print("List: ",end='')
            self.PRINT()
            print("Position=",self.pos,"Element=",self.cur.data)
    
    def delete(self):# '-' 명령어 구현

        if self.head.next==None:

            print("Error!Cannot delete a node since there is no node!")

        
        elif self.cur.next==None:#마지막 노드인 경우
            
            if self.cur==self.head.next:#마지막 노드가 첫 번째 노드인 경우
            
                self.cur=self.head#current node가 더미 노드가 됨
                self.before=None#before node는 None
                self.head.next=None#next는 None
                self.pos=-1#position은 -1
                self.n=0#개수는 0개
            
            else:

                self.before.next=None#before node의 next를 None으로 만듦
                self.cur=self.head.next#current node가 첫 번째 노드가 됨
                self.before=self.head#before node는 더미 노드
                self.pos=0#position은 0
                self.n=self.n-1#개수 1개 감소

        else:#일반적인 경우

            self.before.next=self.cur.next#before노드의 next를 cur node의 next로 업데이트
            self.cur=self.cur.next#cur노드를 cur 노드의 next로 업데이트
            #pos는 그대로
            self.n=self.n-1#노드 개수 1개 감소
    
    def traverse_rear(self):#'>' 명령어, 'N', 'P' 명령어를 따로 구현하기 때문에, count 매개변수를 삭제

        if self.head.next==None:
            print("Error!Add a node!")
        else:

            while self.cur.next!=None:
                self.move_next()

    def move_to_head(self):#'<<' 명령어, position을 [-1] head로 가져감, 교안에 있는 '< +x +y +z'를 구현하기 위하여 '<'대신 '<<'새로 구현

        self.cur=self.head#current node를 head로 업데이트
        self.before=None
        self.pos=-1
    
    def replace(self,data):# '='명령어
        self.cur.data=data
    
    def move_to_index(self,index):#'5G'와 같은 명령어 수행하기 위하여 만든 모듈, 특정 index로 이동

        self.move_to_head()

        while self.pos!=index:
            self.move_next()
    
    def data_count(self):# '#'명령어
         
         return self.n
    
    def is_member(self,data):# '?'명령어

        self.move_to_head()

        while True:

            if self.cur.data==data:
                print(self.pos+1,end=':')
                self.PRINT()
            
            if self.cur.next==None:
                break
            else:
                self.move_next()
    
    def clear_list(self): # 'C'명령어
        self.traverse_front()

        while self.head.next!=None:
            self.delete()
    
    def is_empty(self): # "E" 명령어

        if self.head.next==None:

            return True

        else:

            return False
    
    def find_before(self,target): # target node의 before노드를 찾는 모듈

        i=self.head

        while True:

            if i.next==target:
                return i
            else:
                i=i.next

        
    def move_previous(self): #'P'명령어

        if self.cur==self.head:#current node가 더미노드이면
            print("Error!Cannot move back!")

        else:
            tmp=self.find_before(self.before)

            self.cur=self.before#current node를 before node로 업데이트
            self.before=tmp#before 노드를 tmp 노드로 업데이트
            self.pos=self.pos-1#pos -1
    
    def count_member(self,data): #'c'명령어, ex) 'ca'는 a라는 element가 list에 몇개 있는지 알려줌

        cnt=0
        
        self.move_to_head()
        
        while True:

            if self.cur.data==data:
                cnt=cnt+1
            
            if self.cur.next==None:
                break

            self.move_next()
        
        return cnt

        

                
    
        




#일반적인 모듈 선언부



def CommandLineInput(pList):

    bIterationTrigger=True

    while bIterationTrigger:

        strInput=input("Type Command Line('Q' to quit) >> ")

        command=strInput.split()#띄어쓰기 단위로 문자열 쪼개기
        
        for i in command:
            if i[0]=="+":
                pList.add(i[1])

            elif i=="Q" or i=="q":
                bIterationTrigger=False

            elif i=="L":
                pList.PRINT()

            elif i=="G":
                pList.get_data()

            elif i=="<":
                pList.traverse_front()

            elif i=="N":
                pList.move_next()

            elif i=="-":
                pList.delete()
            
            elif i==">":
                pList.traverse_rear()

            elif i=="<<":#추가한 기능
                pList.move_to_head()

            elif i[0]=="=":
                pList.replace(i[1])
            
            elif i[0]>="0" and i[0]<="9":

                num=int(re.findall("\d+",i)[0])#숫자만 추출
                string=re.findall("\D+",i)[0]#문자열만 추출

                if string[0]=="=":
                    pList.move_to_index(num-1)
                    pList.replace(string[1])
                else:
                    pList.move_to_index(num-1)
                    pList.get_data()

            elif i=="#":
                print("The number of elements in the list: ",pList.data_count())

            elif i[0]=="?":
                pList.is_member(i[1])
            
            elif i=="C":
                pList.clear_list()
            
            elif i=="E":

                if pList.is_empty():
                    print("The list is empty!")
                else:
                    print("The lis is not empty!")
            
            elif i=="P":#추가한 기능
                pList.move_previous()

            elif i[0]=="c":#추가한 기능
                print("The number of element '",i[1],"' in the list: ",pList.count_member(i[1]))

        pList.ShowCurrentState()
        





def main():
    
    my_list=List()#linkedlist 선언
    CommandLineInput(my_list)
    
    



if __name__=="__main__":
    main()


    