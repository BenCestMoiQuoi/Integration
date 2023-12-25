import tkinter as t
from tkinter import messagebox
from tkinter import ttk


import matplotlib as plt

plt.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg#, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from Integration.Fonction import *


class Fen(t.Tk):
    def __init__(self, *args, **kwargs):
        self.page=0

        t.Tk.__init__(self, *args, **kwargs)
        t.Tk.wm_title(self, Nom_projet)

        self.bind('<KeyPress-Escape>', self.keypress_enter)
        self.bind('<KeyPress-Return>', self.keypress_enter)
        self.bind('<KeyPress-Up>', self.print_size)


        self.iconbitmap(f"{path}{Nom_icon}")

        container = t.Frame(self)

        container.pack(side="top")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Page1, Page2):
            frame = F(container, self)
            frame.grid(row=0, column=0, sticky='nsew')
            self.frames[F] = frame

        self.change_page1()
        self.mainloop()

    def keypress_enter(self, key):
        if self.page == 1 and key.keysym == 'Return':
            self.change_page2()
        elif self.page == 1 and key.keysym == 'Escape':
            self.quit()
        elif self.page == 2 and key.keysym == 'Escape':
            self.change_page1()

    def change_page1(self):
        frame = self.frames[Page1]
        frame.tkraise()
        self.geometry("468x423")
        self.page = 1

    def change_page2(self):
        if self.frames[Page1].validation():
            frame = self.frames[Page2]
            frame.tkraise()
            self.geometry("575x569")
            frame.calcul_graph(self.frames[Page1])
            self.page = 2

    def quit(self):
        self.destroy()

    def print_size(self, key):
        print(f'Largeur : {self.winfo_width()}\tHauteur : {self.winfo_height()}')


class Button(t.Button):
    def __init__(self, *args, **kwargs):
        t.Button.__init__(self, font=("Times New Roman", 16), *args, **kwargs)
class Entry(t.Button):
    def __init__(self, *args, **kwargs):
        t.Entry.__init__(self, font=("Times New Roman", 16), *args, **kwargs)
class Label(t.Label):
    def __init__(self, *args, **kwargs):
        t.Label.__init__(self, font=("Times New Roman", 16), *args, **kwargs)


class Page1(t.Frame):
    def __init__(self, parent, controlleur):
        t.Frame.__init__(self, parent)

        self.xmin = t.StringVar()
        self.xmax = t.StringVar()
        self.t_func = t.StringVar()

        self.func = ""
        self.t_t_func = ""
        self.t_func.set('')
        self.xmin.set('')
        self.xmax.set('')

        Label_ = Label(self, text="Give the fonction and all parameters")
        Label_exem = Label(self, text="ex : 2*sin(x)+exp(x**(2))-(ln(x**(17)))/(2.13)", fg='gray')

        Label_fonc = Label(self, textvariable=self.t_func, borderwidth=2, relief="groove")

        mat_frame = Matrice(self)

        cmd = self.register(lambda s: not s or is_float(s))

        Label_xmin = Label(self, text="x_min")
        Label_xmax = Label(self, text="x_max")
        Entry_xmin = Entry(self, textvariable=self.xmin, validate="key", vcmd=(cmd, "%P"))
        Entry_xmax = Entry(self, textvariable=self.xmax, validate="key", vcmd=(cmd, "%P"))

        Bu_reset = Button(self, text='Reset', command=self.reset)
        Bu_valid = Button(self, text='Calcul', command=lambda: controlleur.change_page2())
        Bu_quit = Button(self, text="Quit", command=lambda: controlleur.destroy())

        Label_.grid(row=0, column=0, columnspan=3)
        Label_exem.grid(row=1, column=0, columnspan=3)
        Label_fonc.grid(row=2, column=0, columnspan=3)

        mat_frame.grid(row=3, column=1, columnspan=2)

        Label_xmin.grid(row=4, column=1)
        Label_xmax.grid(row=5, column=1)
        Entry_xmin.grid(row=4, column=2)
        Entry_xmax.grid(row=5, column=2)

        Bu_reset.grid(row=6, column=3)
        Bu_valid.grid(row=7, column=3)
        Bu_quit.grid(row=8, column=3)


    def reset(self):
        self.t_t_func=""
        self.func=""
        self.t_func.set(self.t_t_func)
        self.xmin.set('')
        self.xmax.set('')

    def bu_f(self, text):
        self.t_t_func += text
        if text in CHANGE_FONCTION.keys():
            text = CHANGE_FONCTION[text]
        self.func += text
        self.t_func.set(self.t_t_func)
    
    def validation(self):
        if verif_fonction(self):
            messagebox.showinfo(title = "Veuillez réessayer !", message = "La fonction est mal remplie")
            return False
        if self.t_t_func == '' or self.xmin.get() == '' or self.xmax.get() == '':
            messagebox.showinfo(title = "Veuillez réessayer !", message = "Une ou plusieur(s) cases ne sont pas rempli(s)")
            return False
        if float(self.xmin.get()) >= float(self.xmax.get()):
            messagebox.showinfo(title = "Veuillez réessayer !" ,message = "La tranche de valeur n'est pas corecte")
            return False
        return True


class Matrice(t.Frame):
    def __init__(self, parent):
        t.Frame.__init__(self, parent)
        frame_num = t.Frame(self)
        frame_sim = t.Frame(self)
        frame_com = t.Frame(self)

        Bu_1 = Button(frame_num, text='1', command=lambda: parent.bu_f('1'))
        Bu_2 = Button(frame_num, text='2', command=lambda: parent.bu_f('2'))
        Bu_3 = Button(frame_num, text='3', command=lambda: parent.bu_f('3'))
        Bu_4 = Button(frame_num, text='4', command=lambda: parent.bu_f('4'))
        Bu_5 = Button(frame_num, text='5', command=lambda: parent.bu_f('5'))
        Bu_6 = Button(frame_num, text='6', command=lambda: parent.bu_f('6'))
        Bu_7 = Button(frame_num, text='7', command=lambda: parent.bu_f('7'))
        Bu_8 = Button(frame_num, text='8', command=lambda: parent.bu_f('8'))
        Bu_9 = Button(frame_num, text='9', command=lambda: parent.bu_f('9'))
        Bu_0 = Button(frame_num, text='0', command=lambda: parent.bu_f('0'))
        Bu_p = Button(frame_sim, text='+', command=lambda: parent.bu_f('+'))
        Bu_m = Button(frame_sim, text='-', command=lambda: parent.bu_f('-'))
        Bu_f = Button(frame_sim, text='*', command=lambda: parent.bu_f('*'))
        Bu_d = Button(frame_sim, text='/', command=lambda: parent.bu_f('/'))
        Bu_sin = Button(frame_com, text='sin(', command=lambda: parent.bu_f('sin('))
        Bu_cos = Button(frame_com, text='cos(', command=lambda: parent.bu_f('cos('))
        Bu_tan = Button(frame_com, text='tan(', command=lambda: parent.bu_f('tan('))
        Bu_asin = Button(frame_com, text='arcsin(', command=lambda: parent.bu_f('asin('))
        Bu_acos = Button(frame_com, text='arccos(', command=lambda: parent.bu_f('acos('))
        Bu_atan = Button(frame_com, text='arctan(', command=lambda: parent.bu_f('atan('))
        Bu_pi = Button(frame_com, text='pi', command=lambda: parent.bu_f('pi'))
        Bu_ln = Button(frame_com, text='log(', command=lambda: parent.bu_f('log('))
        Bu_exp = Button(frame_com, text='exp(', command=lambda: parent.bu_f('exp('))
        Bu_pui = Button(frame_com, text='**(', command=lambda: parent.bu_f('**('))
        Bu_par1 = Button(frame_com, text='(', command=lambda: parent.bu_f('('))
        Bu_par2 = Button(frame_com, text=')', command=lambda: parent.bu_f(')'))
        Bu_x = Button(frame_com, text='x', command=lambda: parent.bu_f('x'))

        Bu_1.grid(row=0, column=0)
        Bu_2.grid(row=0, column=1)
        Bu_3.grid(row=0, column=2)
        Bu_4.grid(row=1, column=0)
        Bu_5.grid(row=1, column=1)
        Bu_6.grid(row=1, column=2)
        Bu_7.grid(row=2, column=0)
        Bu_8.grid(row=2, column=1)
        Bu_9.grid(row=2, column=2)
        Bu_0.grid(row=3, column=0, columnspan=3)
        Bu_p.grid(row=0, column=0)
        Bu_m.grid(row=1, column=0)
        Bu_f.grid(row=2, column=0)
        Bu_d.grid(row=3, column=0)

        Bu_sin.grid(row=0, column=0, columnspan=2)
        Bu_cos.grid(row=1, column=0, columnspan=2)
        Bu_tan.grid(row=2, column=0, columnspan=2)
        Bu_asin.grid(row=0, column=2)
        Bu_acos.grid(row=1, column=2)
        Bu_atan.grid(row=2, column=2)
        Bu_ln.grid(row=0, column=3)
        Bu_exp.grid(row=1, column=3)
        Bu_pui.grid(row=2, column=3)
        Bu_par1.grid(row=3, column=0)
        Bu_par2.grid(row=3, column=1)
        Bu_pi.grid(row=3, column=2)
        Bu_x.grid(row=3, column=3)

        frame_num.grid(row=0, column=0, padx=(10, 0))
        frame_sim.grid(row=0, column=1, padx=(5, 0))
        frame_com.grid(row=0, column=2, padx=(5, 0))



class Page2(t.Frame):
    def __init__(self, parent, controlleur):
        self.n=1000
        self.xmin=0
        self.xmax=0
        self.pas = 0
        self.area = t.StringVar()
        self.area.set('Area : ')
        self.x=[]
        self.y=[]
        

        t.Frame.__init__(self, parent)

        self.f = Fonction()

        fig = Figure(figsize=(5, 5), dpi=100) 
        a = fig.add_subplot(111)
        a.plot(self.x, self.y)

        canvas = FigureCanvasTkAgg(fig, self)
        Bu_retu = Button(self, text="Return", command=lambda: controlleur.change_page1())
        Label_ = Label(self, textvariable=self.area)

        canvas._tkcanvas.grid(row=0, column=0, columnspan=2)
        Label_.grid(row=1, column=0)
        Bu_retu.grid(row=2, column=2)

    def calcul_graph(self, p1):
        self.xmin = float(p1.xmin.get())
        self.xmax = float(p1.xmax.get())
        self.pas = (self.xmax-self.xmin)/self.n
        val = 0

        self.f.new_fonc(p1.func)
        x1 = self.xmin
        x2 = x1+self.pas
        y1 = self.f.calcul_val(x1)
        self.x = [x1]
        self.y = [y1]
        while x2 <= self.xmax:
            y2 = self.f.calcul_val(x2)
            self.x.append(x2)
            self.y.append(y2)
            val += 0.5*(y1+y2)*self.pas

            y1 = y2
            x1 = x2
            x2 += self.pas
        self.area.set(f'{self.area.get()}{round_str(val)}')

        fig = Figure(figsize=(5, 5), dpi=100)
        a = fig.add_subplot(111)
        a.plot(self.x, self.y)
        
        canvas = FigureCanvasTkAgg(fig, self)
        canvas._tkcanvas.grid(row=0, column=0, columnspan=2)
        canvas.draw()

        

class Fonction:
    def __init__(self):
        self.t_solve = ""
        self.solve = ""

    def new_fonc(self, text):
        self.t_solve = text

    def calcul_val(self, x):
        return eval(self.t_solve)


