#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Mar 07, 2018 09:14:17 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import Pompa_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    Pompa_support.set_Tk_var()
    top = POMPA (root)
    Pompa_support.init(root, top)
    root.mainloop()

w = None
def create_POMPA(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    Pompa_support.set_Tk_var()
    top = POMPA (w)
    Pompa_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_POMPA():
    global w
    w.destroy()
    w = None


class POMPA:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font11 = "-family ISOCPEUR -size 16 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"
        font9 = "-family Tahoma -size 8 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1024x780+186+5")
        top.title("POMPA")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.FrameLogo = Frame(top)
        self.FrameLogo.place(relx=0.01, rely=0.03, relheight=0.22, relwidth=0.98)

        self.FrameLogo.configure(relief=GROOVE)
        self.FrameLogo.configure(borderwidth="2")
        self.FrameLogo.configure(relief=GROOVE)
        self.FrameLogo.configure(background="#d9d9d9")
        self.FrameLogo.configure(highlightbackground="#d9d9d9")
        self.FrameLogo.configure(highlightcolor="black")
        self.FrameLogo.configure(width=1000)

        self.FrameAdv = Frame(top)
        self.FrameAdv.place(relx=0.74, rely=0.28, relheight=0.45, relwidth=0.24)
        self.FrameAdv.configure(relief=GROOVE)
        self.FrameAdv.configure(borderwidth="2")
        self.FrameAdv.configure(relief=GROOVE)
        self.FrameAdv.configure(background="#d9d9d9")
        self.FrameAdv.configure(highlightbackground="#d9d9d9")
        self.FrameAdv.configure(highlightcolor="black")
        self.FrameAdv.configure(width=250)

        self.LabelAdv = Label(self.FrameAdv)
        self.LabelAdv.place(relx=0.04, rely=0.06, height=289, width=211)
        self.LabelAdv.configure(activebackground="#f9f9f9")
        self.LabelAdv.configure(activeforeground="black")
        self.LabelAdv.configure(background="#d9d9d9")
        self.LabelAdv.configure(disabledforeground="#a3a3a3")
        self.LabelAdv.configure(foreground="#000000")
        self.LabelAdv.configure(highlightbackground="#d9d9d9")
        self.LabelAdv.configure(highlightcolor="black")
        self.LabelAdv.configure(text="Wskazowki")

        self.ButtonRun = Button(top)
        self.ButtonRun.place(relx=0.74, rely=0.86, height=111, width=251)
        self.ButtonRun.configure(activebackground="#d9d9d9")
        self.ButtonRun.configure(activeforeground="#000000")
        self.ButtonRun.configure(background="#d9d9d9")
        self.ButtonRun.configure(disabledforeground="#a3a3a3")
        self.ButtonRun.configure(font=font11)
        self.ButtonRun.configure(foreground="#000000")
        self.ButtonRun.configure(highlightbackground="#d9d9d9")
        self.ButtonRun.configure(highlightcolor="black")
        self.ButtonRun.configure(pady="0")
        self.ButtonRun.configure(text='''PPPPrzzzrzelicz''')

        self.RadioMode1 = Radiobutton(top)
        self.RadioMode1.place(relx=0.75, rely=0.74, relheight=0.03
                , relwidth=0.21)
        self.RadioMode1.configure(activebackground="#d9d9d9")
        self.RadioMode1.configure(activeforeground="#000000")
        self.RadioMode1.configure(anchor=W)
        self.RadioMode1.configure(background="#d9d9d9")
        self.RadioMode1.configure(disabledforeground="#a3a3a3")
        self.RadioMode1.configure(foreground="#000000")
        self.RadioMode1.configure(highlightbackground="#d9d9d9")
        self.RadioMode1.configure(highlightcolor="black")
        self.RadioMode1.configure(justify=LEFT)
        self.RadioMode1.configure(text='''Sprawdzenie istniejacej pompowni''')
        self.RadioMode1.configure(variable=Pompa_support.tryb)

        self.RadioMode2 = Radiobutton(top)
        self.RadioMode2.place(relx=0.75, rely=0.78, relheight=0.03
                , relwidth=0.21)
        self.RadioMode2.configure(activebackground="#d9d9d9")
        self.RadioMode2.configure(activeforeground="#000000")
        self.RadioMode2.configure(anchor=W)
        self.RadioMode2.configure(background="#d9d9d9")
        self.RadioMode2.configure(disabledforeground="#a3a3a3")
        self.RadioMode2.configure(foreground="#000000")
        self.RadioMode2.configure(highlightbackground="#d9d9d9")
        self.RadioMode2.configure(highlightcolor="black")
        self.RadioMode2.configure(justify=LEFT)
        self.RadioMode2.configure(text='''Minimalizacja nakladow inwestycyjnych''')
        self.RadioMode2.configure(variable=Pompa_support.tryb)

        self.RadioMode3 = Radiobutton(top)
        self.RadioMode3.place(relx=0.75, rely=0.82, relheight=0.03
                , relwidth=0.22)
        self.RadioMode3.configure(activebackground="#d9d9d9")
        self.RadioMode3.configure(activeforeground="#000000")
        self.RadioMode3.configure(anchor=W)
        self.RadioMode3.configure(background="#d9d9d9")
        self.RadioMode3.configure(disabledforeground="#a3a3a3")
        self.RadioMode3.configure(foreground="#000000")
        self.RadioMode3.configure(highlightbackground="#d9d9d9")
        self.RadioMode3.configure(highlightcolor="black")
        self.RadioMode3.configure(justify=LEFT)
        self.RadioMode3.configure(text='''Optymalizacja nakladow inwestycyjnych''')
        self.RadioMode3.configure(variable=Pompa_support.tryb)


        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNBOptions = ttk.Notebook(top)
        self.TNBOptions.place(relx=0.01, rely=0.26, relheight=0.76
                , relwidth=0.71)
        self.TNBOptions.configure(width=731)
        self.TNBOptions.configure(takefocus="")
        self.TNBOptions_t1 = ttk.Frame(self.TNBOptions)
        self.TNBOptions.add(self.TNBOptions_t1, padding=3)
        self.TNBOptions.tab(0, text="Geometria ",underline="-1",)
        self.TNBOptions_t2 = ttk.Frame(self.TNBOptions)
        self.TNBOptions.add(self.TNBOptions_t2, padding=3)
        self.TNBOptions.tab(1, text="Charakterystyka pomp",underline="-1",)

        self.LOption1 = Label(self.TNBOptions_t1)
        self.LOption1.place(relx=0.01, rely=0.04, height=19, width=171)
        self.LOption1.configure(activebackground="#f9f9f9")
        self.LOption1.configure(activeforeground="black")
        self.LOption1.configure(anchor=W)
        self.LOption1.configure(background="#d9d9d9")
        self.LOption1.configure(disabledforeground="#a3a3a3")
        self.LOption1.configure(foreground="#000000")
        self.LOption1.configure(highlightbackground="#d9d9d9")
        self.LOption1.configure(highlightcolor="black")
        self.LOption1.configure(text='''Ksztalt pompowni:''')

        self.RadioLO1A = Radiobutton(self.TNBOptions_t1)
        self.RadioLO1A.place(relx=0.67, rely=0.04, relheight=0.04, relwidth=0.12)

        self.RadioLO1A.configure(activebackground="#d9d9d9")
        self.RadioLO1A.configure(activeforeground="#000000")
        self.RadioLO1A.configure(anchor=W)
        self.RadioLO1A.configure(background="#d9d9d9")
        self.RadioLO1A.configure(disabledforeground="#a3a3a3")
        self.RadioLO1A.configure(foreground="#000000")
        self.RadioLO1A.configure(highlightbackground="#d9d9d9")
        self.RadioLO1A.configure(highlightcolor="black")
        self.RadioLO1A.configure(justify=LEFT)
        self.RadioLO1A.configure(text='''Prostokatny''')

        self.RadioLO1B = Radiobutton(self.TNBOptions_t1)
        self.RadioLO1B.place(relx=0.81, rely=0.04, relheight=0.04, relwidth=0.18)

        self.RadioLO1B.configure(activebackground="#d9d9d9")
        self.RadioLO1B.configure(activeforeground="#000000")
        self.RadioLO1B.configure(anchor=W)
        self.RadioLO1B.configure(background="#d9d9d9")
        self.RadioLO1B.configure(disabledforeground="#a3a3a3")
        self.RadioLO1B.configure(foreground="#000000")
        self.RadioLO1B.configure(highlightbackground="#d9d9d9")
        self.RadioLO1B.configure(highlightcolor="black")
        self.RadioLO1B.configure(justify=LEFT)
        self.RadioLO1B.configure(text='''Kolowy''')

        self.RadioLO2A = Radiobutton(self.TNBOptions_t1)
        self.RadioLO2A.place(relx=0.67, rely=0.09, relheight=0.04, relwidth=0.13)

        self.RadioLO2A.configure(activebackground="#d9d9d9")
        self.RadioLO2A.configure(activeforeground="#000000")
        self.RadioLO2A.configure(anchor=W)
        self.RadioLO2A.configure(background="#d9d9d9")
        self.RadioLO2A.configure(disabledforeground="#a3a3a3")
        self.RadioLO2A.configure(foreground="#000000")
        self.RadioLO2A.configure(highlightbackground="#d9d9d9")
        self.RadioLO2A.configure(highlightcolor="black")
        self.RadioLO2A.configure(justify=LEFT)
        self.RadioLO2A.configure(text='''Rzedowe''')
        self.RadioLO2A.configure(variable=Pompa_support.ustawienie_pomp)

        self.RadioLO2B = Radiobutton(self.TNBOptions_t1)
        self.RadioLO2B.place(relx=0.81, rely=0.09, relheight=0.04, relwidth=0.17)

        self.RadioLO2B.configure(activebackground="#d9d9d9")
        self.RadioLO2B.configure(activeforeground="#000000")
        self.RadioLO2B.configure(anchor=W)
        self.RadioLO2B.configure(background="#d9d9d9")
        self.RadioLO2B.configure(disabledforeground="#a3a3a3")
        self.RadioLO2B.configure(foreground="#000000")
        self.RadioLO2B.configure(highlightbackground="#d9d9d9")
        self.RadioLO2B.configure(highlightcolor="black")
        self.RadioLO2B.configure(justify=LEFT)
        self.RadioLO2B.configure(text='''Optymalne''')
        self.RadioLO2B.configure(variable=Pompa_support.ustawienie_pomp)

        self.LOption2 = Label(self.TNBOptions_t1)
        self.LOption2.place(relx=0.01, rely=0.09, height=19, width=171)
        self.LOption2.configure(activebackground="#f9f9f9")
        self.LOption2.configure(activeforeground="black")
        self.LOption2.configure(anchor=W)
        self.LOption2.configure(background="#d9d9d9")
        self.LOption2.configure(disabledforeground="#a3a3a3")
        self.LOption2.configure(foreground="#000000")
        self.LOption2.configure(highlightbackground="#d9d9d9")
        self.LOption2.configure(highlightcolor="black")
        self.LOption2.configure(text='''Ustawienie pomp:''')

        self.LOption3 = Label(self.TNBOptions_t1)
        self.LOption3.place(relx=0.01, rely=0.15, height=19, width=281)
        self.LOption3.configure(activebackground="#f9f9f9")
        self.LOption3.configure(activeforeground="black")
        self.LOption3.configure(anchor=W)
        self.LOption3.configure(background="#d9d9d9")
        self.LOption3.configure(disabledforeground="#a3a3a3")
        self.LOption3.configure(foreground="#000000")
        self.LOption3.configure(highlightbackground="#d9d9d9")
        self.LOption3.configure(highlightcolor="black")
        self.LOption3.configure(text='''Wariant okreslajacy liczbe pomp rezerwowych:''')

        self.RadioLO3A = Radiobutton(self.TNBOptions_t1)
        self.RadioLO3A.place(relx=0.55, rely=0.15, relheight=0.04, relwidth=0.17)

        self.RadioLO3A.configure(activebackground="#d9d9d9")
        self.RadioLO3A.configure(activeforeground="#000000")
        self.RadioLO3A.configure(anchor=W)
        self.RadioLO3A.configure(background="#d9d9d9")
        self.RadioLO3A.configure(disabledforeground="#a3a3a3")
        self.RadioLO3A.configure(foreground="#000000")
        self.RadioLO3A.configure(highlightbackground="#d9d9d9")
        self.RadioLO3A.configure(highlightcolor="black")
        self.RadioLO3A.configure(justify=LEFT)
        self.RadioLO3A.configure(text='''Minimalny''')

        self.RadioLO3B = Radiobutton(self.TNBOptions_t1)
        self.RadioLO3B.place(relx=0.67, rely=0.15, relheight=0.04, relwidth=0.14)

        self.RadioLO3B.configure(activebackground="#d9d9d9")
        self.RadioLO3B.configure(activeforeground="#000000")
        self.RadioLO3B.configure(anchor=W)
        self.RadioLO3B.configure(background="#d9d9d9")
        self.RadioLO3B.configure(disabledforeground="#a3a3a3")
        self.RadioLO3B.configure(foreground="#000000")
        self.RadioLO3B.configure(highlightbackground="#d9d9d9")
        self.RadioLO3B.configure(highlightcolor="black")
        self.RadioLO3B.configure(justify=LEFT)
        self.RadioLO3B.configure(text='''Optymalny''')

        self.RadioLO3C = Radiobutton(self.TNBOptions_t1)
        self.RadioLO3C.place(relx=0.81, rely=0.15, relheight=0.04, relwidth=0.14)

        self.RadioLO3C.configure(activebackground="#d9d9d9")
        self.RadioLO3C.configure(activeforeground="#000000")
        self.RadioLO3C.configure(anchor=W)
        self.RadioLO3C.configure(background="#d9d9d9")
        self.RadioLO3C.configure(disabledforeground="#a3a3a3")
        self.RadioLO3C.configure(foreground="#000000")
        self.RadioLO3C.configure(highlightbackground="#d9d9d9")
        self.RadioLO3C.configure(highlightcolor="black")
        self.RadioLO3C.configure(justify=LEFT)
        self.RadioLO3C.configure(text='''Bezpieczny''')

        self.LOption4 = Label(self.TNBOptions_t1)
        self.LOption4.place(relx=0.01, rely=0.2, height=19, width=331)
        self.LOption4.configure(activebackground="#f9f9f9")
        self.LOption4.configure(activeforeground="black")
        self.LOption4.configure(anchor=W)
        self.LOption4.configure(background="#d9d9d9")
        self.LOption4.configure(disabledforeground="#a3a3a3")
        self.LOption4.configure(foreground="#000000")
        self.LOption4.configure(highlightbackground="#d9d9d9")
        self.LOption4.configure(highlightcolor="black")
        self.LOption4.configure(text='''Srednica kola, niezbedna do fizycznego zainstalowania pompy [m]''')

        self.EntryLO4 = Entry(self.TNBOptions_t1)
        self.EntryLO4.place(relx=0.61, rely=0.2, relheight=0.04, relwidth=0.27)
        self.EntryLO4.configure(background="white")
        self.EntryLO4.configure(disabledbackground="#d4d4d0d0c8c8")
        self.EntryLO4.configure(disabledforeground="#a3a3a3")
        self.EntryLO4.configure(font=font10)
        self.EntryLO4.configure(foreground="#000000")
        self.EntryLO4.configure(highlightbackground="#d9d9d9")
        self.EntryLO4.configure(highlightcolor="black")
        self.EntryLO4.configure(insertbackground="black")
        self.EntryLO4.configure(selectbackground="#c4c4c4")
        self.EntryLO4.configure(selectforeground="black")

        self.LOption5 = Label(self.TNBOptions_t1)
        self.LOption5.place(relx=0.01, rely=0.26, height=19, width=331)
        self.LOption5.configure(activebackground="#f9f9f9")
        self.LOption5.configure(activeforeground="black")
        self.LOption5.configure(anchor=W)
        self.LOption5.configure(background="#d9d9d9")
        self.LOption5.configure(disabledforeground="#a3a3a3")
        self.LOption5.configure(foreground="#000000")
        self.LOption5.configure(highlightbackground="#d9d9d9")
        self.LOption5.configure(highlightcolor="black")
        self.LOption5.configure(text='''Srednica wewnetrzna pompowni [m]''')

        self.EntryLO5 = Entry(self.TNBOptions_t1)
        self.EntryLO5.place(relx=0.61, rely=0.26, relheight=0.04, relwidth=0.27)
        self.EntryLO5.configure(background="white")
        self.EntryLO5.configure(disabledforeground="#a3a3a3")
        self.EntryLO5.configure(font=font10)
        self.EntryLO5.configure(foreground="#000000")
        self.EntryLO5.configure(highlightbackground="#d9d9d9")
        self.EntryLO5.configure(highlightcolor="black")
        self.EntryLO5.configure(insertbackground="black")
        self.EntryLO5.configure(selectbackground="#c4c4c4")
        self.EntryLO5.configure(selectforeground="black")

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.plik = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.plik,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Plik")
        self.plik.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=Pompa_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Otworz")
        self.plik.add_separator(
                background="#d9d9d9")
        self.plik.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=Pompa_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Importuj Dane")
        self.plik.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=Pompa_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Eksportuj Dane")
        self.plik.add_separator(
                background="#d9d9d9")
        self.plik.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=Pompa_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Zamknij Program")
        self.pomoc = Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.pomoc,
                activebackground="#d9d9d9",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Pomoc")
        self.pomoc.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=Pompa_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="O Programie")
        self.pomoc.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                #command=Pompa_support.# TODO,
                font="TkMenuFont",
                foreground="#000000",
                label="Pomoc")







if __name__ == '__main__':
    vp_start_gui()



