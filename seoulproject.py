from tkinter import*
import tkinter.ttk as ttk

root = Tk()

def Nowon1():
    global new1
    new1 = Toplevel()
    new1.geometry("500x300")
    new1.title("백소정")
    nowon1 = Label(new1, text = "백소정", font = 20, fg = "blue")
    add1 = Label(new1, text = "서울 노원구 동일로 1024")
    menu1 = Label(new1, text = "추천메뉴: 마제소바+돈카츠")
    photo1 = PhotoImage(master = new1, file = "gif/baek.gif", width=20, height=10)
    label1 = Label(new1, image = photo1)
    nowon1.pack()
    add1.pack()
    menu1.pack()
    label1.pack(anchor=CENTER)

def Nowon2():
    global new2
    new2 = Toplevel()
    new2.geometry("500x300")
    new2.title("네코정")
    nowon2 = Label(new2, text = "네코정", font = 20, fg = "blue")
    add2 = Label(new2, text = "서울 노원구 동일로192길 77 2층201호")
    menu2 = Label(new2, text = "추천메뉴: 텐동")
    photo2 = PhotoImage(master = new2, file = "gif/네코정.gif")
    label2 = Label(new2, image = photo2)
    nowon2.pack()
    add2.pack()
    menu2.pack()
    label2.pack()

def Nowon3():
    global new3
    new3 = Toplevel()
    new3.geometry("500x300")
    new3.title("라라브레드")
    nowon3 = Label(new3, text = "라라브레드", font = 20, fg = "blue")
    add3 = Label(new3, text = "서울 노원구 공릉로41길 32")
    menu3 = Label(new3, text = "추천메뉴: 아보카도 새우의 역습")
    photo3 = PhotoImage(master = new3, file = "gif/라라브레드.gif")
    label3 = Label(new3, image = photo3)
    nowon3.pack()
    add3.pack()
    menu3.pack()
    label3.pack()

def Gangnam1():
    global new4
    new4 = Toplevel()
    new4.geometry("500x300")
    new4.title("아부라소바")
    mapo1 = Label(new4, text = "아부라소바", font = 20, fg = "blue")
    add1 = Label(new4, text = "서울 강남구 학동로43길 8 B동 1층")
    menu1 = Label(new4, text = "추천메뉴: 아부라소바")
    mapo1.pack()
    add1.pack()
    menu1.pack()

def Gangnam2():
    global new5
    new5 = Toplevel()
    new5.geometry("500x300")
    new5.title("노티드")
    mapo2 = Label(new5, text = "노티드", font = 20, fg = "blue")
    add2 = Label(new5, text = "서울 강남구 도산대로53길 15 1층")
    menu2 = Label(new5, text = "추천메뉴: 딸기도넛")
    mapo2.pack()
    add2.pack()
    menu2.pack()

def Gangnam3():
    global new6
    new6 = Tk()
    new6.geometry("500x300")
    new6.title("그랑씨엘")
    mapo3 = Label(new6, text = "그랑씨엘", font = 20, fg = "blue")
    add3 = Label(new6, text = "서울 강남구 도산대로45길 16-6 1층")
    menu3 = Label(new6, text = "추천메뉴: 버섯 크림 리조또")
    mapo3.pack()
    add3.pack()
    menu3.pack()

def Mapo1():
    global new7
    new7 = Toplevel()
    new7.geometry("500x300")
    new7.title("카츠만개")
    gangnam1 = Label(new7, text = "카츠만개", font = 20, fg = "blue")
    add1 = Label(new7, text = "서울 마포구 동교로38길 23 1층")
    menu1 = Label(new7, text = "추천메뉴: 로제 누룽지 치즈 돈카츠")
    gangnam1.pack()
    add1.pack()
    menu1.pack()

def Mapo2():
    global new8
    new8 = Toplevel()
    new8.geometry("500x300")
    new8.title("랫댓")
    gangnam2 = Label(new8, text = "랫댓", font = 20, fg = "blue")
    add2 = Label(new8, text = "서울 마포구 동교로 243-4 2층")
    menu2 = Label(new8, text = "추천메뉴: 반반피자")
    gangnam2.pack()
    add2.pack()
    menu2.pack()

def Mapo3():
    global new9
    new9 = Toplevel()
    new9.geometry("500x300")
    new9.title("스와레")
    gangnam3 = Label(new9, text = "스와레", font = 20, fg = "blue")
    add3 = Label(new9, text = "서울 마포구 연남로 4-1 1층")
    menu3 = Label(new9, text = "추천메뉴: 치킨냉우동")
    gangnam3.pack()
    add3.pack()
    menu3.pack()

def Nowon():
    global new_nw
    new_nw = Toplevel()
    new_nw.title("노원구 맛집")
    new_nw.geometry("250x130")
    button1_nowon = Button(new_nw, text = "백소정", font = 15, width = 10, height = 2, command = Nowon1)
    button2_nowon = Button(new_nw, text = "네코정", font = 15, width = 10, height = 2, command = Nowon2)
    button3_nowon = Button(new_nw, text = "라라브레드", font = 15, width = 10, height = 2, command = Nowon3)
    button1_nowon.pack()
    button2_nowon.pack()
    button3_nowon.pack()

def Gangnam():
    global new_gn
    new_gn = Toplevel()
    new_gn.title("강남구 맛집")
    new_gn.geometry("250x130")
    button1_gn = Button(new_gn, text = "아부라소바", font = 15, width = 10, height = 2, command = Gangnam1)
    button2_gn = Button(new_gn, text = "노티드", font = 15, width = 10, height = 2, command = Gangnam2)
    button3_gn = Button(new_gn, text = "그랑씨엘", font = 15, width = 10, height = 2, command = Gangnam3)
    button1_gn.pack()
    button2_gn.pack()
    button3_gn.pack()

def Mapo():
    global new_mp
    new_mp = Toplevel()
    new_mp.title("마포구 맛집")
    new_mp.geometry("250x130")
    button1_mapo = Button(new_mp, text = "카츠만개", font = 15, width = 10, height = 2, command = Mapo1)
    button2_mapo = Button(new_mp, text = "랫댓", font = 15, width = 10, height = 2, command = Mapo2)
    button3_mapo = Button(new_mp, text = "스와레", font = 15, width = 10, height = 2, command = Mapo3)
    button1_mapo.pack()
    button2_mapo.pack()
    button3_mapo.pack()
    
root.title("서울시 지도")
bg = PhotoImage(file = "gif/seoul.gif")
seoul1 = Canvas(root, width = 1500, height = 873)
seoul1.pack(fill = "both", expand = True)
seoul1.create_image(0, 0, image = bg, anchor = "nw") 

button1 = Button(root, text = "노원구", width = 10, command = Nowon)
button2 = Button(root, text = "강남구", width = 10, command = Gangnam)
button3 = Button(root, text = "마포구", width = 10, command = Mapo)

button1_seoul = seoul1.create_window(940, 238, anchor = "nw", window = button1)
button2_seoul = seoul1.create_window(915, 635, anchor = "nw", window = button2)
button3_seoul = seoul1.create_window(624, 473, anchor = "nw", window = button3)

root.mainloop()
