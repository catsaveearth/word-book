from tkinter import *
import random

f = open("word.txt", 'r')  #파일열기
word_list = [] #word instance를 저장할 리스트


#word class 생성
class word():
    def __init__(self, spel, mean):
        self.spel = spel
        self.mean = mean

    def getspel(self):
        return self.spel

    def getmean(self):
        return self.mean

    def getspel_mean(self):
        listt = [self.spel, self.mean]
        return listt


for line in f:
    contents = line.split(',')
    en = contents[0]
    ko = contents[1]
    itc = word(en, ko)  #객체생성
    word_list.append(itc) #리스트에 객체 저장



window = Tk()
window.title("word")
window.geometry("500x400+100+100")
window.resizable(False, False)

logo = PhotoImage(file="logo.png")
logolabel = Label(image=logo)
logolabel.place(x=19, y=45)


start=Entry(window,width=5)
start.place(x=75, y=170)

end=Entry(window,width=5)
end.place(x=195, y=170)

the_number=Entry(window,width=5)
the_number.place(x=310, y=170)

label1= Label(window, text = "번 부터" , width=5, height=1, fg="black")
label1.place(x=123, y=170)

label2= Label(window, text = "번 까지" , width=5, height=1, fg="black")
label2.place(x=240, y=170)

label3= Label(window, text = "개를(최대 7개)" , width=13, height=1, fg="black")
label3.place(x=345, y=170)

label4= Label(window, text = "(1 ~ 530) 사이의 값" , width=20, height=1, fg="black")
label4.place(x=105, y=200)


def studyroom():
    window=Tk()
    window.title("word_study")
    window.geometry("640x700+100+100")
    window.resizable(False, False)

    number = random.sample(range((int(start.get()) - 1), (int(end.get()) - 1)), (int(the_number.get())))
    for i in number:
        spelmean = word_list[i].getspel_mean()
        label= Label(window, text = spelmean[0] , width=30, height=3, fg="black", relief="solid")
        label.pack()
        label1= Label(window, text =  spelmean[1] , width=30, height=3, fg="purple")
        label1.pack()


def testroom():
    window=Tk()
    window.title("word_test")
    window.geometry("640x700+100+100")
    window.resizable(False, False)

    number = random.sample(range((int(start.get()) - 1), (int(end.get()) - 1)), (int(the_number.get())))
    for i in number:
        label= Label(window, text = word_list[i].getspel(), width=30, height=3, fg="black")
        label.pack()

        answer=Entry(window,width=10)
        answer.pack()

    def real_answer():
        a = 0
        for i in number:
            real_ans = Label(window, text = word_list[i].getmean(),  width=30, height=3, fg="blue")
            real_ans.place(x=400, y=40+ 70*a)
            a = a+1

    label= Label(window, text = " ", width=30, height=3, fg="black")
    label.pack()

    button = Button(window, overrelief="solid", width=5, height=1, text="뜻 보기", command = real_answer, repeatdelay=1000, repeatinterval=100)
    button.pack()


studylogo = PhotoImage(file="study.png")
button1 = Button(window, image=studylogo, command=studyroom, repeatdelay=1000, repeatinterval=100)
button1.place(x=70, y=265)

examlogo = PhotoImage(file="exam.png")
button2 = Button(window, image=examlogo, command=testroom, repeatdelay=1000, repeatinterval=100)
button2.place(x=270, y=265)


window.mainloop()
