import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk

def vit_background():
    return
def mgt_background():
    return
def mnd_background():
    return
def skl_background():
    return
def spd_background():
    return
def luk_background():
    return
def def_background():
    return
def spr_background():
    return


# ----------- Main window and tabs creation ----------
window = Tk()
window.title("Fire Emblem Akkadia")
window.geometry("1000x600+150+100")
window.iconbitmap('UI Resources/fe_akkadia.ico')

tabControl = ttk.Notebook(window)
tab_levelup = Frame(tabControl)
tab_statsheet = Frame(tabControl)
tab_map = Frame(tabControl)

tabControl.add(tab_levelup, text = '  Level up  ')
tabControl.add(tab_statsheet, text = '  Statsheet  ')
tabControl.add(tab_map, text = '  Map  ')
tabControl.pack(expand = 1, fill = 'both')
# ----------------------------------------------------

# ------------------ Level up tab UI -----------------
image_level = Image.open('UI Resources/levelup_template.png')
image_resize_level = ImageTk.PhotoImage(image_level.resize([480,320]))
levelup_image = Label(tab_levelup, image=image_resize_level)
levelup_image.pack(side=BOTTOM)

levelup_stats_frame = Frame()
levelup_stats_frame.place(x=25, y=300)

STAT_label = Label(levelup_stats_frame, text='STAT', padx=25, pady=10, font=('bold'))
plus1_label = Label(levelup_stats_frame, text='+1', padx=2, pady=10, width=3, anchor='w')
plus2_label = Label(levelup_stats_frame, text='+2', padx=2, pady=10, width=3, anchor='w')
stat_value_label = Label(levelup_stats_frame, text='Value', padx=10, pady=10)
STAT_label.grid(row=0, column=0)
plus1_label.grid(row=0, column=1)
plus2_label.grid(row=0, column=2)
stat_value_label.grid(row=0, column=3)

VIT_label = Label(levelup_stats_frame, text = 'Vitality', width=6)
MGT_label = Label(levelup_stats_frame, text = 'Might', width=6)
MND_label = Label(levelup_stats_frame, text = 'Mind', width=6)
SKL_label = Label(levelup_stats_frame, text = 'Skill', width=6)
SPD_label = Label(levelup_stats_frame, text = 'Speed', width=6)
LUK_label = Label(levelup_stats_frame, text = 'Luck', width=6)
DEF_label = Label(levelup_stats_frame, text = 'Defense', width=6)
SPR_label = Label(levelup_stats_frame, text = 'Spirit', width=6)
VIT_label.grid(row=1, column=0)
MGT_label.grid(row=2, column=0)
MND_label.grid(row=3, column=0)
SKL_label.grid(row=4, column=0)
SPD_label.grid(row=5, column=0)
LUK_label.grid(row=6, column=0)
DEF_label.grid(row=7, column=0)
SPR_label.grid(row=8, column=0)

VIT_up1 = IntVar()
VIT_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = vit_background, variable = VIT_up1)
VIT_up2 = IntVar()
VIT_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = vit_background, variable = VIT_up2)
MGT_up1 = IntVar()
MGT_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = mgt_background, variable = MGT_up1)
MGT_up2 = IntVar()
MGT_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = mgt_background, variable = MGT_up2)
MND_up1 = IntVar()
MND_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = mnd_background, variable = MND_up1)
MND_up2 = IntVar()
MND_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = mnd_background, variable = MND_up2)
SKL_up1 = IntVar()
SKL_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = skl_background, variable = SKL_up1)
SKL_up2 = IntVar()
SKL_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = skl_background, variable = SKL_up2)
SPD_up1 = IntVar()
SPD_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = spd_background, variable = SPD_up1)
SPD_up2 = IntVar()
SPD_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = spd_background, variable = SPD_up2)
LUK_up1 = IntVar()
LUK_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = luk_background, variable = LUK_up1)
LUK_up2 = IntVar()
LUK_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = luk_background, variable = LUK_up2)
DEF_up1 = IntVar()
DEF_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = def_background, variable = DEF_up1)
DEF_up2 = IntVar()
DEF_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = def_background, variable = DEF_up2)
SPR_up1 = IntVar()
SPR_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = spr_background, variable = SPR_up1)
SPR_up2 = IntVar()
SPR_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = spr_background, variable = SPR_up2)
VIT_plus1_checkbox.grid(row=1, column=1)
MGT_plus1_checkbox.grid(row=2, column=1)
MND_plus1_checkbox.grid(row=3, column=1)
SKL_plus1_checkbox.grid(row=4, column=1)
SPD_plus1_checkbox.grid(row=5, column=1)
LUK_plus1_checkbox.grid(row=6, column=1)
DEF_plus1_checkbox.grid(row=7, column=1)
SPR_plus1_checkbox.grid(row=8, column=1)
VIT_plus2_checkbox.grid(row=1, column=2)
MGT_plus2_checkbox.grid(row=2, column=2)
MND_plus2_checkbox.grid(row=3, column=2)
SKL_plus2_checkbox.grid(row=4, column=2)
SPD_plus2_checkbox.grid(row=5, column=2)
LUK_plus2_checkbox.grid(row=6, column=2)
DEF_plus2_checkbox.grid(row=7, column=2)
SPR_plus2_checkbox.grid(row=8, column=2)

VIT_input = Entry(levelup_stats_frame, width=5, justify='center')
MGT_input = Entry(levelup_stats_frame, width=5, justify='center')
MND_input = Entry(levelup_stats_frame, width=5, justify='center')
SKL_input = Entry(levelup_stats_frame, width=5, justify='center')
SPD_input = Entry(levelup_stats_frame, width=5, justify='center')
LUK_input = Entry(levelup_stats_frame, width=5, justify='center')
DEF_input = Entry(levelup_stats_frame, width=5, justify='center')
SPR_input = Entry(levelup_stats_frame, width=5, justify='center')
VIT_input.grid(row=1, column=3)
MGT_input.grid(row=2, column=3)
MND_input.grid(row=3, column=3)
SKL_input.grid(row=4, column=3)
SPD_input.grid(row=5, column=3)
LUK_input.grid(row=6, column=3)
DEF_input.grid(row=7, column=3)
SPR_input.grid(row=8, column=3)
# ----------------------------------------------------

# ------------ Statsheet generator tab UI ------------
image_statsheet = Image.open('UI Resources/statsheet_template.png')
image_resize_statsheet = ImageTk.PhotoImage(image_statsheet.resize([780,240]))
statsheet_image = Label(tab_statsheet, image=image_resize_statsheet)
statsheet_image.pack(side=BOTTOM)
# ----------------------------------------------------

window.mainloop()