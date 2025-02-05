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

levelup_ui = Image.open('UI Resources/Level up tab/levelup_tab_ui.png')
levelup_template_image = Image.open('UI Resources/Level up tab/Plains.png')
levelup_preview_image = Image.open('UI Resources/Level up tab/levelup_template.png')
levelup_ui.paste(levelup_template_image, (520,560), mask=levelup_template_image)
levelup_ui.paste(levelup_preview_image, (520,560), mask=levelup_preview_image)
levelup_ui_resize = ImageTk.PhotoImage(levelup_ui.resize([1000,600]))
levelup_ui_label = Label(tab_levelup, image=levelup_ui_resize)
levelup_ui_label.place(x=0, y=0)
# </editor-fold>

# <editor-fold desc="Levelup tab - unit update functions">
def levelup_name(levelup_var):
    levelup_str = name_levelup_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/name_bg.png')
    levelup_ui.paste(levelup_word_background, (736, 20), mask=levelup_word_background)
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
        levelup_ui.paste(letter_image, (word_x_coord, 44), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_class(levelup_var):
    levelup_str = class_levelup_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/class_bg.png')
    levelup_ui.paste(levelup_word_background, (32, 180), mask=levelup_word_background)
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
        levelup_ui.paste(letter_image, (68 + word_x_coord, 204), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_lvl(levelup_var):
    levelup_num = lvl_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/level_bg.png')
    levelup_ui.paste(lvlup_stat_background, (340, 180), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (448, 208), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (416, 208), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (448, 208), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_portrait(levelup_var):
    return
# </editor-fold>

# <editor-fold desc="Levelup tab - stat update functions">
def levelup_vit_bg1():
    levelup_var = 1
    levelup_vit_num(levelup_var)
def levelup_vit_bg2():
    levelup_var = 2
    levelup_vit_num(levelup_var)
def levelup_vit_num(levelup_var):
    levelup_num = VIT_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/VIT_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (68, 316), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/VIT_levelup1.png')
        levelup_ui.paste(background, (68, 316), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/VIT_levelup2.png')
        levelup_ui.paste(background, (68, 316), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (192, 336), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (160, 336), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (192, 336), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_mgt_bg1():
    levelup_var = 1
    levelup_mgt_num(levelup_var)
def levelup_mgt_bg2():
    levelup_var = 2
    levelup_mgt_num(levelup_var)
def levelup_mgt_num(levelup_var):
    levelup_num = MGT_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/MGT_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (68, 380), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/MGT_levelup1.png')
        levelup_ui.paste(background, (68, 380), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/MGT_levelup2.png')
        levelup_ui.paste(background, (68, 380), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (192, 400), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (160, 400), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (192, 400), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_mnd_bg1():
    levelup_var = 1
    levelup_mnd_num(levelup_var)
def levelup_mnd_bg2():
    levelup_var = 2
    levelup_mnd_num(levelup_var)
def levelup_mnd_num(levelup_var):
    levelup_num = MND_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/MND_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (68, 444), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/MND_levelup1.png')
        levelup_ui.paste(background, (68, 444), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/MND_levelup2.png')
        levelup_ui.paste(background, (68, 444), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (192, 464), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (160, 464), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (192, 464), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_skl_bg1():
    levelup_var = 1
    levelup_skl_num(levelup_var)
def levelup_skl_bg2():
    levelup_var = 2
    levelup_skl_num(levelup_var)
def levelup_skl_num(levelup_var):
    levelup_num = SKL_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SKL_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (68, 508), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/SKL_levelup1.png')
        levelup_ui.paste(background, (68, 508), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/SKL_levelup2.png')
        levelup_ui.paste(background, (68, 508), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (192, 528), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (160, 528), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (192, 528), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_spd_bg1():
    levelup_var = 1
    levelup_spd_num(levelup_var)
def levelup_spd_bg2():
    levelup_var = 2
    levelup_spd_num(levelup_var)
def levelup_spd_num(levelup_var):
    levelup_num = SPD_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SPD_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (324, 316), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/SPD_levelup1.png')
        levelup_ui.paste(background, (324, 316), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/SPD_levelup2.png')
        levelup_ui.paste(background, (324, 316), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (448, 336), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (416, 336), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (448, 336), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_luk_bg1():
    levelup_var = 1
    levelup_luk_num(levelup_var)
def levelup_luk_bg2():
    levelup_var = 2
    levelup_luk_num(levelup_var)
def levelup_luk_num(levelup_var):
    levelup_num = LUK_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/LUK_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (324, 380), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/LUK_levelup1.png')
        levelup_ui.paste(background, (324, 380), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/LUK_levelup2.png')
        levelup_ui.paste(background, (324, 380), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (448, 400), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (416, 400), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (448, 400), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_def_bg1():
    levelup_var = 1
    levelup_def_num(levelup_var)
def levelup_def_bg2():
    levelup_var = 2
    levelup_def_num(levelup_var)
def levelup_def_num(levelup_var):
    levelup_num = DEF_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/DEF_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (324, 444), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/DEF_levelup1.png')
        levelup_ui.paste(background, (324, 444), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/DEF_levelup2.png')
        levelup_ui.paste(background, (324, 444), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (448, 464), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (416, 464), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (448, 464), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_spr_bg1():
    levelup_var = 1
    levelup_spr_num(levelup_var)
def levelup_spr_bg2():
    levelup_var = 2
    levelup_spr_num(levelup_var)
def levelup_spr_num(levelup_var):
    levelup_num = SPR_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SPR_neutral.png')
    levelup_ui.paste(lvlup_stat_background, (324, 508), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/SPR_levelup1.png')
        levelup_ui.paste(background, (324, 508), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/SPR_levelup2.png')
        levelup_ui.paste(background, (324, 508), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (448, 528), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (416, 528), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (448, 528), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([480, 320]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new
# </editor-fold>

# <editor-fold desc="Levelup tab - UI">
name_levelup_input = Entry(tab_levelup, width=15, justify='center')
name_levelup_input.bind('<KeyRelease>', levelup_name)
class_levelup_input = Entry(tab_levelup, width=15, justify='center')
class_levelup_input.bind('<KeyRelease>', levelup_class)
lvl_levelup_input = Entry(tab_levelup, width=5, justify='center')
lvl_levelup_input.bind('<KeyRelease>', levelup_lvl)
name_levelup_input.place(x=104, y=112)
class_levelup_input.place(x=104, y=144)
lvl_levelup_input.place(x=124, y=176)

levelup_plus1 = PhotoImage(file = 'UI Resources/Level up tab/plus_1.png')
VIT_plus1_button = Button(tab_levelup, command = levelup_vit_bg1, image = levelup_plus1, bg='#f24f65')
VIT_plus2_button = Button(tab_levelup, command = levelup_vit_bg2, image = levelup_plus1, bg='#f24f65')
MGT_plus1_button = Button(tab_levelup, command = levelup_mgt_bg1, image = levelup_plus1, bg='#f24f65')
MGT_plus2_button = Button(tab_levelup, command = levelup_mgt_bg2, image = levelup_plus1, bg='#f24f65')
MND_plus1_button = Button(tab_levelup, command = levelup_mnd_bg1, image = levelup_plus1, bg='#f24f65')
MND_plus2_button = Button(tab_levelup, command = levelup_mnd_bg2, image = levelup_plus1, bg='#f24f65')
SKL_plus1_button = Button(tab_levelup, command = levelup_skl_bg1, image = levelup_plus1, bg='#f24f65')
SKL_plus2_button = Button(tab_levelup, command = levelup_skl_bg2, image = levelup_plus1, bg='#f24f65')
SPD_plus1_button = Button(tab_levelup, command = levelup_spd_bg1, image = levelup_plus1, bg='#f24f65')
SPD_plus2_button = Button(tab_levelup, command = levelup_spd_bg2, image = levelup_plus1, bg='#f24f65')
LUK_plus1_button = Button(tab_levelup, command = levelup_luk_bg1, image = levelup_plus1, bg='#f24f65')
LUK_plus2_button = Button(tab_levelup, command = levelup_luk_bg2, image = levelup_plus1, bg='#f24f65')
DEF_plus1_button = Button(tab_levelup, command = levelup_def_bg1, image = levelup_plus1, bg='#f24f65')
DEF_plus2_button = Button(tab_levelup, command = levelup_def_bg2, image = levelup_plus1, bg='#f24f65')
SPR_plus1_button = Button(tab_levelup, command = levelup_spr_bg1, image = levelup_plus1, bg='#f24f65')
SPR_plus2_button = Button(tab_levelup, command = levelup_spr_bg2, image = levelup_plus1, bg='#f24f65')
VIT_plus1_button.place(x=98, y=274)
MGT_plus1_button.place(x=98, y=306)
MND_plus1_button.place(x=98, y=338)
SKL_plus1_button.place(x=98, y=370)
SPD_plus1_button.place(x=98, y=402)
LUK_plus1_button.place(x=98, y=434)
DEF_plus1_button.place(x=98, y=466)
SPR_plus1_button.place(x=98, y=498)
VIT_plus2_button.place(x=134, y=274)
MGT_plus2_button.place(x=134, y=306)
MND_plus2_button.place(x=134, y=338)
SKL_plus2_button.place(x=134, y=370)
SPD_plus2_button.place(x=134, y=402)
LUK_plus2_button.place(x=134, y=434)
DEF_plus2_button.place(x=134, y=466)
SPR_plus2_button.place(x=134, y=498)

VIT_levelup_input = Entry(tab_levelup, width=5, justify='center')
VIT_levelup_input.bind('<KeyRelease>', levelup_vit_num)
MGT_levelup_input = Entry(tab_levelup, width=5, justify='center')
MGT_levelup_input.bind('<KeyRelease>', levelup_mgt_num)
MND_levelup_input = Entry(tab_levelup, width=5, justify='center')
MND_levelup_input.bind('<KeyRelease>', levelup_mnd_num)
SKL_levelup_input = Entry(tab_levelup, width=5, justify='center')
SKL_levelup_input.bind('<KeyRelease>', levelup_skl_num)
SPD_levelup_input = Entry(tab_levelup, width=5, justify='center')
SPD_levelup_input.bind('<KeyRelease>', levelup_spd_num)
LUK_levelup_input = Entry(tab_levelup, width=5, justify='center')
LUK_levelup_input.bind('<KeyRelease>', levelup_luk_num)
DEF_levelup_input = Entry(tab_levelup, width=5, justify='center')
DEF_levelup_input.bind('<KeyRelease>', levelup_def_num)
SPR_levelup_input = Entry(tab_levelup, width=5, justify='center')
SPR_levelup_input.bind('<KeyRelease>', levelup_spr_num)
VIT_levelup_input.place(x=164, y=272)
MGT_levelup_input.place(x=164, y=304)
MND_levelup_input.place(x=164, y=336)
SKL_levelup_input.place(x=164, y=368)
SPD_levelup_input.place(x=164, y=400)
LUK_levelup_input.place(x=164, y=432)
DEF_levelup_input.place(x=164, y=464)
SPR_levelup_input.place(x=164, y=496)
# </editor-fold>

# <editor-fold desc="Statsheet tab UI">
image_statsheet = Image.open('UI Resources/Statsheet tab/statsheet_template.png')
image_resize_statsheet = ImageTk.PhotoImage(image_statsheet.resize([780,240]))
statsheet_image = Label(tab_statsheet, image=image_resize_statsheet)
statsheet_image.pack(side=BOTTOM)
# </editor-fold>

window.mainloop()