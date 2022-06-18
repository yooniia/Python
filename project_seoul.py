from tkinter import*
import tkinter.ttk as ttk

root = Tk()

#노원구 맛집 리스트 정보1
def Nowon1():
    global new1
    new1 = Toplevel()
    new1.geometry("500x500")
    new1.title("백소정")
    nowon1 = Label(new1, text = "백소정", font = 20, fg = "blue")
    add1 = Label(new1, text = "서울 노원구 동일로 1024")
    menu1 = Label(new1, text = "추천메뉴: 마제소바+돈카츠")
    photo1 = PhotoImage(master = new1, file = "seoul/백소정.gif", width=300, height=400)
    label1 = Label(new1, image = photo1)
    label1.image = photo1
    nowon1.pack()
    add1.pack()
    menu1.pack()
    label1.pack()

#노원구 맛집 리스트 정보2
def Nowon2():
    global new2
    new2 = Toplevel()
    new2.geometry("500x500")
    new2.title("네코정")
    nowon2 = Label(new2, text = "네코정", font = 20, fg = "blue")
    add2 = Label(new2, text = "서울 노원구 동일로192길 77 2층201호")
    menu2 = Label(new2, text = "추천메뉴: 텐동")
    photo2 = PhotoImage(master = new2, file = "seoul/네코정.gif", width=300, height=400)
    label2 = Label(new2, image = photo2)
    label2.image = photo2
    nowon2.pack()
    add2.pack()
    menu2.pack()
    label2.pack()

#노원구 맛집 리스트 정보3
def Nowon3():
    global new3
    new3 = Toplevel()
    new3.geometry("500x500")
    new3.title("라라브레드")
    nowon3 = Label(new3, text = "라라브레드", font = 20, fg = "blue")
    add3 = Label(new3, text = "서울 노원구 공릉로41길 32")
    menu3 = Label(new3, text = "추천메뉴: 아보카도 새우의 역습")
    photo3 = PhotoImage(master = new3, file = "seoul/라라브레드.gif", width=300, height=400)
    label3 = Label(new3, image = photo3)
    label3.image = photo3
    nowon3.pack()
    add3.pack()
    menu3.pack()
    label3.pack()

#강남구 맛집 리스트 정보1
def Gangnam1():
    global new4
    new4 = Toplevel()
    new4.geometry("500x500")
    new4.title("아부라소바")
    Gangnam1 = Label(new4, text = "아부라소바", font = 20, fg = "blue")
    add1 = Label(new4, text = "서울 강남구 학동로43길 8 B동 1층")
    menu1 = Label(new4, text = "추천메뉴: 아부라소바")
    photo4 = PhotoImage(master = new4, file = "seoul/아부라소바.gif",width=300, height=400)
    label1 = Label(new4, image = photo4)
    label1.image = photo4
    Gangnam1.pack()
    add1.pack()
    menu1.pack()
    label1.pack()

#강남구 맛집 리스트 정보2
def Gangnam2():
    global new5
    new5 = Toplevel()
    new5.geometry("500x500")
    new5.title("패티앤베지스")
    Gangnam2 = Label(new5, text = "패티앤베지스", font = 20, fg = "blue")
    add2 = Label(new5, text = "서울 강남구 압구정로4길 11 1층")
    menu2 = Label(new5, text = "추천메뉴: 칠리치즈프라이즈, 클래식베이컨")
    photo5 = PhotoImage(master = new5, file = "seoul/패티앤베지스.gif",width=300, height=400)
    label2 = Label(new5, image = photo5)
    label2.image = photo5
    Gangnam2.pack()
    add2.pack()
    menu2.pack()
    label2.pack()

#강남구 맛집 리스트 정보3
def Gangnam3():
    global new6
    new6 = Toplevel()
    new6.geometry("500x500")
    new6.title("리틀넥 청담")
    Gangnam3 = Label(new6, text = "리틀넥 청담", font = 20, fg = "blue")
    add3 = Label(new6, text = "서울 강남구 도산대로51길 17")
    menu3 = Label(new6, text = "추천메뉴: 아메리칸 오믈렛")
    photo6 = PhotoImage(master = new6, file = "seoul/리틀넥 청담.gif",width=300, height=400)
    label3 = Label(new6, image = photo6)
    label3.image = photo6
    Gangnam3.pack()
    add3.pack()
    menu3.pack()
    label3.pack()
    
#마포구 맛집 리스트 정보1
def Mapo1():
    global new7
    new7 = Toplevel()
    new7.geometry("500x500")
    new7.title("카츠만개")
    Mapo1 = Label(new7, text = "카츠만개", font = 20, fg = "blue")
    add1 = Label(new7, text = "서울 마포구 동교로38길 23 1층")
    menu1 = Label(new7, text = "추천메뉴: 로제 누룽지 치즈 돈카츠")
    photo7 = PhotoImage(master = new7, file = "seoul/카츠만개.gif",width=300, height=400)
    label1 = Label(new7, image = photo7)
    label1.image = photo7
    Mapo1.pack()
    add1.pack()
    menu1.pack()
    label1.pack()

#마포구 맛집 리스트 정보2
def Mapo2():
    global new8
    new8 = Toplevel()
    new8.geometry("500x500")
    new8.title("랫댓")
    Mapo2 = Label(new8, text = "랫댓", font = 20, fg = "blue")
    add2 = Label(new8, text = "서울 마포구 동교로 243-4 2층")
    menu2 = Label(new8, text = "추천메뉴: 반반피자")
    photo8 = PhotoImage(master = new8, file = "seoul/랫댓.gif",width=400, height=400)
    label2 = Label(new8, image = photo8)
    label2.image = photo8
    Mapo2.pack()
    add2.pack()
    menu2.pack()
    label2.pack()

#마포구 맛집 리스트 정보3
def Mapo3():
    global new9
    new9 = Toplevel()
    new9.geometry("500x500")
    new9.title("스와레")
    Mapo3 = Label(new9, text = "스와레", font = 20, fg = "blue")
    add3 = Label(new9, text = "서울 마포구 연남로 4-1 1층")
    menu3 = Label(new9, text = "추천메뉴: 치킨냉우동")
    photo9 = PhotoImage(master = new9, file = "seoul/스와레.gif",width=300, height=400)
    label3 = Label(new9, image = photo9)
    label3.image = photo9
    Mapo3.pack()
    add3.pack()
    menu3.pack()
    label3.pack()

#노원구 맛집 버튼
def Nowon():
    global new_nw
    new_nw = Toplevel()
    new_nw.title("노원구 맛집")
    new_nw.geometry("250x133")
    button1_nowon = Button(new_nw, text = "백소정", font = 15, width = 10, height = 2, command = Nowon1)
    button2_nowon = Button(new_nw, text = "네코정", font = 15, width = 10, height = 2, command = Nowon2)
    button3_nowon = Button(new_nw, text = "라라브레드", font = 15, width = 10, height = 2, command = Nowon3)
    button1_nowon.pack()
    button2_nowon.pack()
    button3_nowon.pack()

#강남구 맛집 버튼
def Gangnam():
    global new_gn
    new_gn = Toplevel()
    new_gn.title("강남구 맛집")
    new_gn.geometry("250x133")
    button1_gn = Button(new_gn, text = "아부라소바", font = 15, width = 10, height = 2, command = Gangnam1)
    button2_gn = Button(new_gn, text = "패티앤베지스", font = 15, width = 10, height = 2, command = Gangnam2)
    button3_gn = Button(new_gn, text = "리틀넥 청담", font = 15, width = 10, height = 2, command = Gangnam3)
    button1_gn.pack()
    button2_gn.pack()
    button3_gn.pack()

#마포구 맛집 버튼
def Mapo():
    global new_mp
    new_mp = Toplevel()
    new_mp.title("마포구 맛집")
    new_mp.geometry("250x133")
    button1_mapo = Button(new_mp, text = "카츠만개", font = 15, width = 10, height = 2, command = Mapo1)
    button2_mapo = Button(new_mp, text = "랫댓", font = 15, width = 10, height = 2, command = Mapo2)
    button3_mapo = Button(new_mp, text = "스와레", font = 15, width = 10, height = 2, command = Mapo3)
    button1_mapo.pack()
    button2_mapo.pack()
    button3_mapo.pack()

#서울시 지도 띄우기    
root.title("서울시 지도")
bg = PhotoImage(file = "seoul/seoul.gif")
seoul1 = Canvas(root, width = 1500, height = 873)
seoul1.pack(fill = "both", expand = True)
seoul1.create_image(0, 0, image = bg, anchor = "nw") 

#각 구별 버튼 구현
button1 = Button(root, text = "노원구", width = 10, command = Nowon)
button2 = Button(root, text = "강남구", width = 10, command = Gangnam)
button3 = Button(root, text = "마포구", width = 10, command = Mapo)

button1_seoul = seoul1.create_window(940, 238, anchor = "nw", window = button1)
button2_seoul = seoul1.create_window(915, 635, anchor = "nw", window = button2)
button3_seoul = seoul1.create_window(624, 473, anchor = "nw", window = button3)

root.mainloop()
