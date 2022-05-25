from cProfile import label
from email import message
from fileinput import filename
import sqlite3
from lib2to3.pgen2.token import NAME
from tkinter import *
import tkinter.messagebox
import random


def page_start():

    def users():

        Canvas(z,height=200,width=200).place(x=0,y=0)
        Atsumi_label =Label(z,image=pic_four)
        Atsumi_label.place(x=0,y=0)

        username1 = StringVar()
        user_one = Entry(z,textvariable=username1,font=('Arail',35))
        user_one.place(x=500,y=520)

        
        def page_menu():

            global user_show

            # รูปหน้าเมนู
            Canvas(z,height=200,width=200).place(x=0,y=0)
            Hiyori_label =Label(z,image=pic_two)
            Hiyori_label.place(x=0,y=0)

            user_show = username1.get()
            username_show = Label(z,text=user_show,font=('Arail',30))
            username_show2 = Label(z,text='USERNAME : ',font=('Arail',30))
            username_show.place(x=1170,y=0)
            username_show2.place(x=900,y=0)

            def enter_name():

                Hiyori_label.destroy()

                Canvas(z,height=200,width=200).place(x=0,y=-1)
                Aru_label =Label(z,image=pic_three)
                Aru_label.place(x=0,y=0)

                def delete_db():

                    x = sqlite3.connect(r"C:\Users\Clinic iT\Desktop\PYTHON WORK\project_db\RANDOM_gui_one.db")
                    X=x.cursor()

                    z=tkinter.messagebox.askquestion("DELETE","ARE YOU SURE ?")
                    if z == 'yes':
                        X.execute('DELETE FROM save_name WHERE username = ?',(user_show,))
                        x.commit()

        
                def show_name():

                    x = sqlite3.connect(r"C:\Users\Clinic iT\Desktop\PYTHON WORK\project_db\RANDOM_gui_one.db")
                    X=x.cursor()

                    list_number = []

                    s=X.execute('SELECT NAME FROM save_name WHERE username = ?',(user_show,))
                    
                    for i in s: 
                        list_number.append(i[0])

                    number_of_name = Label(z,text=len(list_number),fg='red',bg='white',font=('Arail',45)).place(x=150,y=600)

                def delete_all():# ถามตอนจะลบ

                    z= tkinter.messagebox.askquestion("DELETE","ARE YOU SURE ?")
                    if z == 'yes':

                        massage_one.delete(0,END)
                        massage_two.delete(0,END)
                        massage_three.delete(0,END)
                        massage_four.delete(0,END)
                        massage_five.delete(0,END)
                        massage_six.delete(0,END)
                        massage_seven.delete(0,END)
                        massage_eight.delete(0,END)
                        massage_nine.delete(0,END)
                        massage_ten.delete(0,END)
                        massage_elevent.delete(0,END)
                        massage_twelth.delete(0,END)
                        massage_thridteen.delete(0,END)
                        massage_fourteen.delete(0,END)
                        massage_fifteen.delete(0,END)
                        massage_sixteen.delete(0,END)
                        massage_seventeen.delete(0,END)
                        massage_eightteen.delete(0,END)
                        massage_nineteen.delete(0,END)
                        massage_twenty.delete(0,END)
                        
                        z= tkinter.messagebox.showinfo("DELETE","YOU DELETED")

                    



                txt1 =StringVar()
                massage_one = Entry(z,textvariable=txt1,font=('Arail',20))
                massage_one.place(x=80,y=50)
                label_1 = Label(z,text='1.',font=('Arail',20)).place(x=45,y=50)
                def delete():
                    massage_one.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=50)

                txt2 =StringVar()
                massage_two = Entry(z,textvariable=txt2,font=('Arail',20))
                massage_two.place(x=80,y=100)
                label_2 = Label(z,text='2.',font=('Arail',20)).place(x=45,y=100)
                def delete():
                    massage_two.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=100)

                txt3 =StringVar()
                massage_three = Entry(z,textvariable=txt3,font=('Arail',20))
                massage_three.place(x=80,y=150)
                label_3 = Label(z,text='3.',font=('Arail',20)).place(x=45,y=150)
                def delete():
                    massage_three.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=150)

                txt4 =StringVar()
                massage_four = Entry(z,textvariable=txt4,font=('Arail',20))
                massage_four.place(x=80,y=200)
                label_4 = Label(z,text='4.',font=('Arail',20)).place(x=45,y=200)
                def delete():
                    massage_four.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=200)

                txt5 =StringVar()
                massage_five = Entry(z,textvariable=txt5,font=('Arail',20))
                massage_five.place(x=80,y=250)
                label_5 = Label(z,text='5.',font=('Arail',20)).place(x=45,y=250)
                def delete():
                    massage_five.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=250)

                txt6 =StringVar()
                massage_six = Entry(z,textvariable=txt6,font=('Arail',20))
                massage_six.place(x=80,y=300)
                label_6 = Label(z,text='6.',font=('Arail',20)).place(x=45,y=300)
                def delete():
                    massage_six.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=300)

                txt7 =StringVar()
                massage_seven = Entry(z,textvariable=txt7,font=('Arail',20))
                massage_seven.place(x=80,y=350)
                label_7 = Label(z,text='7.',font=('Arail',20)).place(x=45,y=350)
                def delete():
                    massage_seven.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=350)

                txt8 =StringVar()
                massage_eight = Entry(z,textvariable=txt8,font=('Arail',20))
                massage_eight.place(x=80,y=400)
                label_8 = Label(z,text='8.',font=('Arail',20)).place(x=45,y=400)
                def delete():
                    massage_eight.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=400)

                txt9 =StringVar()
                massage_nine = Entry(z,textvariable=txt9,font=('Arail',20))
                massage_nine.place(x=80,y=450)
                label_9 = Label(z,text='9.',font=('Arail',20)).place(x=45,y=450)
                def delete():
                    massage_nine.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=450)

                txt10 =StringVar()
                massage_ten = Entry(z,textvariable=txt10,font=('Arail',20))
                massage_ten.place(x=80,y=500)
                label_10 = Label(z,text='10.',font=('Arail',20)).place(x=30,y=500)
                def delete():
                    massage_ten.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=400,y=500)

                txt11 =StringVar()
                massage_elevent = Entry(z,textvariable=txt11,font=('Arail',20))
                massage_elevent.place(x=520,y=50)
                label_11 = Label(z,text='11.',font=('Arail',20)).place(x=465,y=50)
                def delete():
                    massage_elevent.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=50)

                txt12 =StringVar()
                massage_twelth = Entry(z,textvariable=txt12,font=('Arail',20))
                massage_twelth.place(x=520,y=100)
                label_12 = Label(z,text='12.',font=('Arail',20)).place(x=465,y=100)
                def delete():
                    massage_twelth.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=100)

                txt13 =StringVar()
                massage_thridteen = Entry(z,textvariable=txt13,font=('Arail',20))
                massage_thridteen.place(x=520,y=150)
                label_13 = Label(z,text='13.',font=('Arail',20)).place(x=465,y=150)
                def delete():
                    massage_thridteen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=150)

                txt14 =StringVar()
                massage_fourteen = Entry(z,textvariable=txt14,font=('Arail',20))
                massage_fourteen.place(x=520,y=200)
                label_14 = Label(z,text='14.',font=('Arail',20)).place(x=465,y=200)
                def delete():
                    massage_fourteen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=200)

                txt15 =StringVar()
                massage_fifteen = Entry(z,textvariable=txt15,font=('Arail',20))
                massage_fifteen.place(x=520,y=250)
                label_15 = Label(z,text='15.',font=('Arail',20)).place(x=465,y=250)
                def delete():
                    massage_fifteen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=250)

                txt16 =StringVar()
                massage_sixteen = Entry(z,textvariable=txt16,font=('Arail',20))
                massage_sixteen.place(x=520,y=300)
                label_16 = Label(z,text='16.',font=('Arail',20)).place(x=465,y=300)
                def delete():
                    massage_sixteen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=300)

                txt17 =StringVar()
                massage_seventeen = Entry(z,textvariable=txt17,font=('Arail',20))
                massage_seventeen.place(x=520,y=350)
                label_17 = Label(z,text='17.',font=('Arail',20)).place(x=465,y=350)
                def delete():
                    massage_seventeen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=350)

                txt18 =StringVar()
                massage_eightteen = Entry(z,textvariable=txt18,font=('Arail',20))
                massage_eightteen.place(x=520,y=400)
                label_18 = Label(z,text='18.',font=('Arail',20)).place(x=465,y=400)
                def delete():
                    massage_eightteen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=400)

                txt19 =StringVar()
                massage_nineteen = Entry(z,textvariable=txt19,font=('Arail',20))
                massage_nineteen.place(x=520,y=450)
                label_19 = Label(z,text='19.',font=('Arail',20)).place(x=465,y=450)
                def delete():
                    massage_nineteen.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=450)

                txt20 =StringVar()
                massage_twenty = Entry(z,textvariable=txt20,font=('Arail',20))
                massage_twenty.place(x=520,y=500)
                label_20 = Label(z,text='20.',font=('Arail',20)).place(x=465,y=500)
                def delete():
                    massage_twenty.delete(0,END)
                button_delete= Button(z,text='X',bg='red',font=('Arail',15),command=delete).place(x=840,y=500)


                def Check_name():

                    
                    x = sqlite3.connect(r"C:\Users\Clinic iT\Desktop\PYTHON WORK\project_db\RANDOM_gui_one.db")
                    X=x.cursor()

                    list_name=[]

                    Save_name1 = txt1.get()
                    if len(Save_name1) == 0 :
                        list_name.append(0)
                    elif len(Save_name1) != 0 :
                        list_name.append(1)
                        txt1_save = Save_name1
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt1_save,user_show))
                        x.commit()            


                    Save_name2 = txt2.get()
                    if len(Save_name2) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt2_save = Save_name2
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt2_save,user_show))
                        x.commit()


                    Save_name3 = txt3.get()
                    if len(Save_name3) == 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt3_save = Save_name3
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt3_save,user_show))
                        x.commit()


                    Save_name4 = txt4.get()
                    if len(Save_name4)== 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt4_save = Save_name4
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt4_save,user_show))
                        x.commit()



                    Save_name5 = txt5.get()
                    if len(Save_name5) == 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt5_save = Save_name5
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt5_save,user_show))
                        x.commit()


                    Save_name6 = txt6.get()
                    if len(Save_name6) == 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt6_save = Save_name6
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt6_save,user_show))
                        x.commit()


                    Save_name7 = txt7.get()
                    if len(Save_name7) == 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt7_save = Save_name7
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt7_save,user_show))
                        x.commit()


                    Save_name8 = txt8.get()
                    if len(Save_name8) == 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt8_save = Save_name8
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt8_save,user_show))
                        x.commit()


                    Save_name9 = txt9.get()
                    if len(Save_name9) == 0:
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt9_save = Save_name9
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt9_save,user_show))
                        x.commit()


                    Save_name10 = txt10.get()
                    if len(Save_name10) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt10_save = Save_name10
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt10_save,user_show))
                        x.commit()

                    Save_name11 = txt11.get()
                    if len(Save_name11) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt11_save = Save_name11
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt11_save,user_show))
                        x.commit()

                    Save_name12 = txt12.get()
                    if len(Save_name12) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt12_save = Save_name12
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt12_save,user_show))
                        x.commit()

                    Save_name13 = txt13.get()
                    if len(Save_name13) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt13_save = Save_name13
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt13_save,user_show))
                        x.commit()

                    Save_name14 = txt14.get()
                    if len(Save_name14) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt14_save = Save_name14
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt14_save,user_show))
                        x.commit()

                    Save_name15 = txt15.get()
                    if len(Save_name15) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt15_save = Save_name15
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt15_save,user_show))
                        x.commit()

                    Save_name16 = txt16.get()
                    if len(Save_name16) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt16_save = Save_name16
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt16_save,user_show))
                        x.commit()

                    Save_name17 = txt17.get()
                    if len(Save_name17) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt17_save = Save_name17
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt17_save,user_show))
                        x.commit()

                    Save_name18 = txt18.get()
                    if len(Save_name18) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt18_save = Save_name18
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt18_save,user_show))
                        x.commit()

                    Save_name19 = txt19.get()
                    if len(Save_name19) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt19_save = Save_name19
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt19_save,user_show))
                        x.commit()

                    Save_name20 = txt20.get()
                    if len(Save_name20) == 0 :
                        list_name.append(0)
                    else:
                        list_name.append(1)
                        txt20_save = Save_name20
                        X.execute(f'INSERT INTO save_name(NAME,username) VALUES(?,?)',(txt20_save,user_show))
                        x.commit()

                    print('\n\n\n')
                
                    
                    print(list_name)

                    list_name1 = []
                    list_name2 = []

                    def check_list():
                        for i in list_name:
                            if i ==  1 :
                                list_name1.append(1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                            else:
                                list_name2.append(0)
                    
                        print(list_name1)
                        print(list_name2)
                
                    check_list()
                    

                    if len(list_name1) == 1 or len(list_name1) == 0:
                        box_error=tkinter.messagebox.showerror("ERROR","Please enter name more than 1 names")
                    elif len(list_name1) > 1: 
                        box_info=tkinter.messagebox.showinfo("SAVE","YOU SAVED")
                    
                    

                # ปุ่มหน้า enert_name
                buttom_delete_name_db = Button(z,text='DELETET_DB',fg='white',bg='purple',font=('Arail',30),command=delete_db).place(x=400,y=600)
                buttom_show_name = Button(z,text='NAMES',fg='cyan',bg='purple',font=('Arail',30),command=show_name).place(x=200,y=600)
                buttom_back_menu = Button(z,text='BACK',fg='cyan',bg='purple',font=('Arail',50),command=page_menu).place(x=1200,y=250)
                buttom_save_name = Button(z,text='SAVE',fg='cyan',bg='purple',font=('Arail',50),command=Check_name).place(x=1200,y=400)
                buttom_delete_all = Button(z,text='DELETE ALL',fg='cyan',bg='purple',font=('Arail',50),command=delete_all).place(x=1000,y=550)


            def before_press_sprandom():
                x = sqlite3.connect(r"C:\\Users\\Clinic iT\Desktop\\PYTHON WORK\\project_db\\RANDOM_gui_one.db")
                X=x.cursor()
                box_check=[]
                username = user_show
                for i in X.execute('SELECT NAME FROM save_name WHERE username = ?',(username,)):
                    print(i[0])
                    box_check.append(i[0])
                print(box_check)

                if len(box_check) == 1 or len(box_check) == 0:
                    box_error=tkinter.messagebox.showerror("ERROR","Please enter name more than 1 names")
                elif len(box_check) > 1: 
                    spacial_random()
            
            def before_press_nmrandom():
                x = sqlite3.connect(r"C:\\Users\\Clinic iT\Desktop\\PYTHON WORK\\project_db\\RANDOM_gui_one.db")
                X=x.cursor()
                box_check=[]
                username = user_show
                for i in X.execute('SELECT NAME FROM save_name WHERE username = ?',(username,)):
                    print(i[0])
                    box_check.append(i[0])
                print(box_check)

                if len(box_check) == 1 or len(box_check) == 0:
                    box_error=tkinter.messagebox.showerror("ERROR","Please enter name more than 1 names")
                elif len(box_check) > 1: 
                    normal_random()


            def spacial_random():

                Karin_bunny_label = Label(z,image=pic_six)
                Karin_bunny_label.place(x=0,y=0)
                box_name1=[]

                def enter_name_to_box():
                    x = sqlite3.connect(r"C:\\Users\\Clinic iT\Desktop\\PYTHON WORK\\project_db\\RANDOM_gui_one.db")
                    X=x.cursor()
                    username = user_show
                    for i in X.execute('SELECT NAME FROM save_name WHERE username = ?',(username,)):
                        print(i[0])
                        box_name1.append(i[0])
                    print(box_name1)
                enter_name_to_box()

                def start_random():
                    akari_label =Label(z,image=pic_eight)
                    akari_label.place(x=0,y=0)
                    while len(box_name1)!=0:
                        student=random.choice(box_name1)
                        if len(box_name1) != '0':
                            Label(z,text=student,fg="blue",font=("Arail",70),bg="white").place(x=1200,y=300)
                            box_name1.remove(student)
                            print(box_name1)
                            print(len(box_name1))
                            print(student,'\n\t')
                            break
                        else:
                            Label(z,text='STOP',fg="purple",font=("Arail",50),bg="white").place(x=500,y=200)
                
                    def back_menu():
                        z= tkinter.messagebox.askquestion("WARNING SYSTEM","AER YOU SURE ? : if you exit, system will reset")
                        if z =="yes":
                            page_menu()

                            
                    # ปุ่มหน้า random
                    back_to_menu = Button(z,text="BACK",command=back_menu,fg="black",font=("Arail",30),bg="white").place(x=0,y=0)
                    button_random = Button(z,text="RANDOM",command=start_random,fg="red",font=("Arail",80),bg="white").place(x=50,y=470)
                    
                # ปุ่มหน้า start random
                button_back_menu = Button(z,text="BACK",command=page_menu,fg="black",font=("Arail",30),bg="white").place(x=0,y=0)
                buttom_start_random = Button(z,text="START",command=start_random,fg="red",font=("Arail",70),bg="white").place(x=50,y=490)
            
            def normal_random():

                shun_label =Label(z,image=pic_nine)
                shun_label.place(x=0,y=0)
                box_name2 = []

                def enter_name_to_box():
                    x = sqlite3.connect(r"C:\\Users\\Clinic iT\Desktop\\PYTHON WORK\\project_db\\RANDOM_gui_one.db")
                    X=x.cursor()
                    username = user_show
                    for i in X.execute('SELECT NAME FROM save_name WHERE username = ?',(username,)):
                        print(i[0])
                        box_name2.append(i[0])
                    print(box_name2)
                enter_name_to_box()

                def start_random():
                    Hina_label = Label(z,image=pic_seven)
                    Hina_label.place(x=0,y=0)
                    student1 =random.choice(box_name2)
                    Label(z,text=student1,fg="red",font=("Arail",100),bg="white").place(x=250,y=250)

                    def back_menu():
                            z= tkinter.messagebox.askquestion("WARNING SYSTEM","AER YOU SURE ? : if you exit, system will reset")
                            if z =="yes":
                                page_menu()

                    # ปุ่มหน้า random
                    back_to_menu = Button(z,text="BACK",command=back_menu,fg="black",font=("Arail",30),bg="white").place(x=0,y=0)
                    button_random = Button(z,text="RANDOM",command=start_random,fg="purple",font=("Arail",70),bg="white").place(x=1050,y=350)
                
                # ปุ่มหน้า start random
                button_back_menu = Button(z,text="BACK",command=page_menu,fg="black",font=("Arail",30),bg="white").place(x=0,y=0)
                button_start_random = Button(z,text="START",command=start_random,fg="purple",font=("Arail",70),bg="white").place(x=50,y=490)


            # ปุ่มหน้าเมนู
            button_enter_name = Button(z,text='ENTER NAME',fg='red',bg='white',font=('Arail',50),command=enter_name).place(x=200,y=300)
            button_random_one = Button(z,text='SPACIAL RANDOM',fg='orange',bg='purple',font=('Arail',50),command=before_press_sprandom).place(x=200,y=500)
            button_random_two = Button(z,text='NOMAL RANDOM',fg='cyan',bg='purple',font=('Arail',50),command=before_press_nmrandom).place(x=900,y=500)

        def save_user():

            x = sqlite3.connect(r"C:\Users\Clinic iT\Desktop\PYTHON WORK\project_db\RANDOM_gui_one.db")
            X=x.cursor()

            save_username = username1.get()
            if len(save_username) == 0 :
                box_error=tkinter.messagebox.showerror("ERROR","Please enter name ")
            elif len(save_username) > 10 :
                box_error=tkinter.messagebox.showerror("ERROR","Please enter name no more than 10 charactors")
            elif len(save_username) <= 10 :
                box_info=tkinter.messagebox.showinfo("SYSTEM","YOUR WELCOME TO MY PROGRAM")
                txt1_saveuser1 = save_username 
                X.execute(f'INSERT INTO users(username) VALUES(?)',(txt1_saveuser1,))
                x.commit()
                page_menu()        
        
        # ปุ่มหน้าป้อน username
        button_page_menu = Button(z,text='ENTER',fg='red',bg='white',font=('Arail',35),command=save_user).place(x=1100,y=500)

    def restart(): # จบโปรเเกรม
        x= tkinter.messagebox.askquestion("EXIT","ARE YOU SURE ?")
        if x == 'yes':
            x = sqlite3.connect(r"C:\Users\Clinic iT\Desktop\PYTHON WORK\project_db\RANDOM_gui_one.db")
            X=x.cursor()
            X.execute('DELETE FROM save_name WHERE username = ?',(user_show,))
            X.execute('DELETE FROM users')
            x.commit()
            page_start()

    def destroy(): # จบโปรเเกรม
        x= tkinter.messagebox.askquestion("EXIT","ARE YOU SURE ?")
        if x == 'yes':
            x = sqlite3.connect(r"C:\Users\Clinic iT\Desktop\PYTHON WORK\project_db\RANDOM_gui_one.db")
            X=x.cursor()
            X.execute('DELETE FROM save_name WHERE username = ?',(user_show,))
            X.execute('DELETE FROM users')
            x.commit()
            z.destroy()

    
    # ส่วนเมนู บนขอบ
    MY_menu = Menu()
    z.config(menu=MY_menu)
    mymemu = Menu()
    mymemu.add_command(label='RESTART',command=restart)
    mymemu.add_command(label='EXIT',command=destroy)
    MY_menu.add_cascade(label='menu',menu=mymemu)

    # ปุ่มหน้าเเรก 
    Mashiro_buttom = Button(z,image=pic_one,command=users).place(x=0,y=0)

# com.nexon.bluearchive_Screenshot_2021.11.26_23.37.33
# com.nexon.bluearchive_Screenshot_2021.12.16_20.18.24

# box_error=tkinter.messagebox.showerror("ERROR","Please enter name at No.2 more than 0 charactors")
# box_info=tkinter.messagebox.showinfo("SAVE","YOU SAVED")

z = Tk()
z.title('MY PROJECT')
z.geometry('1550x700+20+50')
z.resizable(0,0)

pic_one=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\MASHIRO.png')
pic_two=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\HIYORI.png')
pic_three=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\ARU.png')
pic_four=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\AZUMI2.png')
pic_five=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\Shun2.png')
pic_six=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\karinbunny4.png')
pic_seven=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\Hina_swim2.png')
pic_eight=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\Akari3.png')
pic_nine=PhotoImage(file='\\Users\\Clinic iT\\Desktop\\PIC.EXE\\Shun2.png')


page_start()
z.mainloop()







