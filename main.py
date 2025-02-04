import os
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk

# <editor-fold desc="Main window and tabs initial setup">
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

levelup_image = Image.open('UI Resources/Level up tab/Plains.png')
levelup_ui = Image.open('UI Resources/Level up tab/levelup_template.png')
levelup_image.paste(levelup_ui, (0,0), mask=levelup_ui)
levelup_image_resize = ImageTk.PhotoImage(levelup_image.resize([480,320]))
levelup_image_label = Label(tab_levelup, image=levelup_image_resize)
levelup_image_label.pack(side=BOTTOM)
# </editor-fold>

# <editor-fold desc="Levelup tab - unit update functions">
def levelup_name(levelup_var):
    levelup_str = name_levelup_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/name_bg.png')
    levelup_image.paste(levelup_word_background, (736, 20), mask=levelup_word_background)
    word_x_coord = 0
    word_size_px = 4
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Dark font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Dark font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Dark font/' + letter + '.png')
        word_size_px += letter_image.size[0] - 4
    word_x_coord = 864 - int(word_size_px / 2)
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Dark font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Dark font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Dark font/' + letter + '.png')
        levelup_image.paste(letter_image, (word_x_coord, 44), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_class(levelup_var):
    levelup_str = class_levelup_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/class_bg.png')
    levelup_image.paste(levelup_word_background, (32, 180), mask=levelup_word_background)
    word_x_coord = 0
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/White font/' + letter + '.png')
        levelup_image.paste(letter_image, (68 + word_x_coord, 204), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_lvl(levelup_var):
    levelup_num = lvl_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/level_bg.png')
    levelup_image.paste(lvlup_stat_background, (340, 180), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (448, 208), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (416, 208), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (448, 208), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_portrait(levelup_var):
    return
# </editor-fold>
# <editor-fold desc="Levelup tab - stat update functions">
def levelup_vit_bg():
    levelup_vit_num(VIT_levelup_input)
def levelup_vit_num(levelup_var):
    levelup_num = VIT_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/VIT_neutral.png')
    levelup_image.paste(lvlup_stat_background, (68, 316), mask=lvlup_stat_background)
    if VIT_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/VIT_levelup1.png')
        levelup_image.paste(background, (68, 316), mask=background)
    if VIT_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/VIT_levelup2.png')
        levelup_image.paste(background, (68, 316), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (192, 336), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (160, 336), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (192, 336), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_mgt_bg():
    levelup_mgt_num(MGT_levelup_input)
def levelup_mgt_num(levelup_var):
    levelup_num = MGT_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/MGT_neutral.png')
    levelup_image.paste(lvlup_stat_background, (68, 380), mask=lvlup_stat_background)
    if MGT_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/MGT_levelup1.png')
        levelup_image.paste(background, (68, 380), mask=background)
    if MGT_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/MGT_levelup2.png')
        levelup_image.paste(background, (68, 380), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (192, 400), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (160, 400), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (192, 400), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_mnd_bg():
    levelup_mnd_num(MND_levelup_input)
def levelup_mnd_num(levelup_var):
    levelup_num = MND_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/MND_neutral.png')
    levelup_image.paste(lvlup_stat_background, (68, 444), mask=lvlup_stat_background)
    if MND_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/MND_levelup1.png')
        levelup_image.paste(background, (68, 444), mask=background)
    if MND_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/MND_levelup2.png')
        levelup_image.paste(background, (68, 444), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (192, 464), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (160, 464), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (192, 464), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_skl_bg():
    levelup_skl_num(SKL_levelup_input)
def levelup_skl_num(levelup_var):
    levelup_num = SKL_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SKL_neutral.png')
    levelup_image.paste(lvlup_stat_background, (68, 508), mask=lvlup_stat_background)
    if SKL_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/SKL_levelup1.png')
        levelup_image.paste(background, (68, 508), mask=background)
    if SKL_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/SKL_levelup2.png')
        levelup_image.paste(background, (68, 508), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (192, 528), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (160, 528), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (192, 528), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_spd_bg():
    levelup_spd_num(SPD_levelup_input)
def levelup_spd_num(levelup_var):
    levelup_num = SPD_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SPD_neutral.png')
    levelup_image.paste(lvlup_stat_background, (324, 316), mask=lvlup_stat_background)
    if SPD_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/SPD_levelup1.png')
        levelup_image.paste(background, (324, 316), mask=background)
    if SPD_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/SPD_levelup2.png')
        levelup_image.paste(background, (324, 316), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (448, 336), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (416, 336), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (448, 336), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_luk_bg():
    levelup_luk_num(LUK_levelup_input)
def levelup_luk_num(levelup_var):
    levelup_num = LUK_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/LUK_neutral.png')
    levelup_image.paste(lvlup_stat_background, (324, 380), mask=lvlup_stat_background)
    if LUK_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/LUK_levelup1.png')
        levelup_image.paste(background, (324, 380), mask=background)
    if LUK_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/LUK_levelup2.png')
        levelup_image.paste(background, (324, 380), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (448, 400), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (416, 400), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (448, 400), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_def_bg():
    levelup_def_num(DEF_levelup_input)
def levelup_def_num(levelup_var):
    levelup_num = DEF_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/DEF_neutral.png')
    levelup_image.paste(lvlup_stat_background, (324, 444), mask=lvlup_stat_background)
    if DEF_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/DEF_levelup1.png')
        levelup_image.paste(background, (324, 444), mask=background)
    if DEF_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/DEF_levelup2.png')
        levelup_image.paste(background, (324, 444), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (448, 464), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (416, 464), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (448, 464), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new

def levelup_spr_bg():
    levelup_spr_num(SPR_levelup_input)
def levelup_spr_num(levelup_var):
    levelup_num = SPR_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SPR_neutral.png')
    levelup_image.paste(lvlup_stat_background, (324, 508), mask=lvlup_stat_background)
    if SPR_levelup1.get() == 1:
        background = Image.open('UI Resources/Level up tab/SPR_levelup1.png')
        levelup_image.paste(background, (324, 508), mask=background)
    if SPR_levelup2.get() == 1:
        background = Image.open('UI Resources/Level up tab/SPR_levelup2.png')
        levelup_image.paste(background, (324, 508), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (448, 528), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_image.paste(num_image1, (416, 528), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_image.paste(num_image2, (448, 528), mask=num_image2)
    levelup_image_new = ImageTk.PhotoImage(levelup_image.resize([480, 320]))
    levelup_image_label.configure(image=levelup_image_new)
    levelup_image_label.image = levelup_image_new
# </editor-fold>
# <editor-fold desc="Levelup tab - UI">
levelup_unit_frame = Frame(tab_levelup)
levelup_unit_frame.place(x=25, y=20)

name_label = Label(levelup_unit_frame, text='Name', padx=25, pady=5)
class_label = Label(levelup_unit_frame, text='Class', pady=5)
level_label = Label(levelup_unit_frame, text='Level', pady=5)
portrait_label = Label(levelup_unit_frame, text='Portrait', pady=5)
name_label.grid(row=0, column=0)
class_label.grid(row=1, column=0)
level_label.grid(row=2, column=0)
portrait_label.grid(row=3, column=0)

name_levelup_input = Entry(levelup_unit_frame, width=15, justify='center')
name_levelup_input.bind('<KeyRelease>', levelup_name)
class_levelup_input = Entry(levelup_unit_frame, width=15, justify='center')
class_levelup_input.bind('<KeyRelease>', levelup_class)
lvl_levelup_input = Entry(levelup_unit_frame, width=5, justify='center')
lvl_levelup_input.bind('<KeyRelease>', levelup_lvl)
name_levelup_input.grid(row=0, column=1)
class_levelup_input.grid(row=1, column=1)
lvl_levelup_input.grid(row=2, column=1)

levelup_stats_frame = Frame(tab_levelup)
levelup_stats_frame.place(x=25, y=300)

STAT_label = Label(levelup_stats_frame, text='STAT', padx=25, pady=10)
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

VIT_levelup1 = IntVar()
VIT_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_vit_bg, variable = VIT_levelup1)
VIT_levelup2 = IntVar()
VIT_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_vit_bg, variable = VIT_levelup2)
MGT_levelup1 = IntVar()
MGT_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_mgt_bg, variable = MGT_levelup1)
MGT_levelup2 = IntVar()
MGT_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_mgt_bg, variable = MGT_levelup2)
MND_levelup1 = IntVar()
MND_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_mnd_bg, variable = MND_levelup1)
MND_levelup2 = IntVar()
MND_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_mnd_bg, variable = MND_levelup2)
SKL_levelup1 = IntVar()
SKL_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_skl_bg, variable = SKL_levelup1)
SKL_levelup2 = IntVar()
SKL_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_skl_bg, variable = SKL_levelup2)
SPD_levelup1 = IntVar()
SPD_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_spd_bg, variable = SPD_levelup1)
SPD_levelup2 = IntVar()
SPD_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_spd_bg, variable = SPD_levelup2)
LUK_levelup1 = IntVar()
LUK_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_luk_bg, variable = LUK_levelup1)
LUK_levelup2 = IntVar()
LUK_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_luk_bg, variable = LUK_levelup2)
DEF_levelup1 = IntVar()
DEF_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_def_bg, variable = DEF_levelup1)
DEF_levelup2 = IntVar()
DEF_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_def_bg, variable = DEF_levelup2)
SPR_levelup1 = IntVar()
SPR_plus1_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_spr_bg, variable = SPR_levelup1)
SPR_levelup2 = IntVar()
SPR_plus2_checkbox = Checkbutton(levelup_stats_frame, onvalue = 1, offvalue = 0,
                                 command = levelup_spr_bg, variable = SPR_levelup2)
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

VIT_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
VIT_levelup_input.bind('<KeyRelease>', levelup_vit_num)
MGT_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
MGT_levelup_input.bind('<KeyRelease>', levelup_mgt_num)
MND_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
MND_levelup_input.bind('<KeyRelease>', levelup_mnd_num)
SKL_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
SKL_levelup_input.bind('<KeyRelease>', levelup_skl_num)
SPD_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
SPD_levelup_input.bind('<KeyRelease>', levelup_spd_num)
LUK_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
LUK_levelup_input.bind('<KeyRelease>', levelup_luk_num)
DEF_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
DEF_levelup_input.bind('<KeyRelease>', levelup_def_num)
SPR_levelup_input = Entry(levelup_stats_frame, width=5, justify='center')
SPR_levelup_input.bind('<KeyRelease>', levelup_spr_num)
VIT_levelup_input.grid(row=1, column=3)
MGT_levelup_input.grid(row=2, column=3)
MND_levelup_input.grid(row=3, column=3)
SKL_levelup_input.grid(row=4, column=3)
SPD_levelup_input.grid(row=5, column=3)
LUK_levelup_input.grid(row=6, column=3)
DEF_levelup_input.grid(row=7, column=3)
SPR_levelup_input.grid(row=8, column=3)
# </editor-fold>

# <editor-fold desc="Statsheet tab UI">
image_statsheet = Image.open('UI Resources/Statsheet tab/statsheet_template.png')
image_resize_statsheet = ImageTk.PhotoImage(image_statsheet.resize([780,240]))
statsheet_image = Label(tab_statsheet, image=image_resize_statsheet)
statsheet_image.pack(side=BOTTOM)
# </editor-fold>

window.mainloop()