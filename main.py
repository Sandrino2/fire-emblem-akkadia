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
window.geometry("1000x650+150+100")
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
levelup_template_image = Image.open('UI Resources/Battle backgrounds/Plains (D).png')
levelup_preview_image = Image.open('UI Resources/Level up tab/levelup_template.png')
levelup_ui.paste(levelup_template_image, (520,560), mask=levelup_template_image)
levelup_ui.paste(levelup_preview_image, (520,560), mask=levelup_preview_image)
levelup_ui_resize = ImageTk.PhotoImage(levelup_ui.resize([1000,600]))
levelup_ui_label = Label(tab_levelup, image=levelup_ui_resize)
levelup_ui_label.place(x=0, y=0)
# </editor-fold>

# <editor-fold desc="Levelup tab - unit update functions">
def export_levelup_image():
    filename = asksaveasfile(mode='w', filetypes=(("png files", "*.png"),("all files", "*")), defaultextension='png')
    if not filename:
        return
    levelup_ui_crop = levelup_ui.crop([520, 560, 1480, 1200])
    levelup_ui_crop.save(filename.name)

def levelup_name(levelup_var):
    levelup_str = name_levelup_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/name_bg.png')
    levelup_ui.paste(levelup_word_background, (1256, 580), mask=levelup_word_background)
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
    word_x_coord = 1384 - int(word_size_px / 2)
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Dark font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Dark font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Dark font/' + letter + '.png')
        levelup_ui.paste(letter_image, (word_x_coord, 604), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_class(levelup_var):
    levelup_str = class_levelup_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/class_bg.png')
    levelup_ui.paste(levelup_word_background, (552, 740), mask=levelup_word_background)
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
        levelup_ui.paste(letter_image, (588 + word_x_coord, 764), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def levelup_lvl(levelup_var):
    levelup_num = lvl_levelup_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/level_bg.png')
    levelup_ui.paste(lvlup_stat_background, (860, 740), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (968, 768), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (936, 768), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (968, 768), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def lvlup_portrait_edit(self):
    if lvlup_unit_name.get():
        unit_portrait = Image.open('UI Resources/Unit portraits/' + lvlup_unit_name.get() + '.png').resize((384, 384))
        if lvlup_background_name.get():
            background_image = Image.open('UI Resources/Battle backgrounds/' + lvlup_background_name.get() + '.png')
        else:
            background_image = Image.open('UI Resources/Battle backgrounds/Plains.png')
        background_image_crop = background_image.crop([568, 256, 952, 640])
        levelup_ui.paste(background_image_crop, (1088, 816))
        levelup_ui.paste(unit_portrait, (1088, 816), mask=unit_portrait)
        levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
        levelup_ui_label.configure(image=levelup_ui_new)
        levelup_ui_label.image = levelup_ui_new
        levelup_ui.paste(unit_portrait, (1088, 816), mask=unit_portrait)
        levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
        levelup_ui_label.configure(image=levelup_ui_new)
        levelup_ui_label.image = levelup_ui_new

def lvlup_custom_portrait():
    filename = askopenfilename(initialdir='Desktop', title='Select an image', filetypes=(("png files", "*.png"),("all files", "*")))
    if not filename:
        return
    unit_portrait = Image.open(filename).resize((384, 384))
    if lvlup_background_name.get():
        background_image = Image.open('UI Resources/Battle backgrounds/' + lvlup_background_name.get() + '.png')
    else:
        background_image = Image.open('UI Resources/Battle backgrounds/Plains.png')
    background_image_crop = background_image.crop([568, 256, 952, 640])
    levelup_ui.paste(background_image_crop, (1088, 816))
    levelup_ui.paste(unit_portrait, (1088, 816), mask=unit_portrait)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new

def lvlup_background_edit(self):
    levelup_ui_crop_stats = levelup_ui.crop([544, 872, 1072, 1144])
    levelup_ui_crop_class = levelup_ui.crop([556, 744, 1060, 824])
    levelup_ui_crop_name = levelup_ui.crop([1260, 584, 1480, 664])
    print(lvlup_background_name.get())
    background_image = Image.open('UI Resources/Battle backgrounds/' + lvlup_background_name.get() + '.png')
    levelup_ui.paste(background_image, (520, 560))
    levelup_ui_template = Image.open('UI Resources/Level up tab/levelup_template.png')
    levelup_ui.paste(levelup_ui_template, (520, 560), mask=levelup_ui_template)
    levelup_ui.paste(levelup_ui_crop_stats, (544, 872))
    levelup_ui.paste(levelup_ui_crop_class, (556, 744))
    levelup_ui.paste(levelup_ui_crop_name, (1260, 584))
    lvlup_portrait_edit(0)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new
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
    levelup_ui.paste(lvlup_stat_background, (588, 876), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/VIT_levelup1.png')
        levelup_ui.paste(background, (588, 876), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/VIT_levelup2.png')
        levelup_ui.paste(background, (588, 876), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (712, 896), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (680, 896), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (712, 896), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (588, 940), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/MGT_levelup1.png')
        levelup_ui.paste(background, (588, 940), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/MGT_levelup2.png')
        levelup_ui.paste(background, (588, 940), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (712, 960), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (680, 960), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (712, 960), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (588, 1004), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/MND_levelup1.png')
        levelup_ui.paste(background, (588, 1004), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/MND_levelup2.png')
        levelup_ui.paste(background, (588, 1004), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (712, 1024), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (680, 1024), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (712, 1024), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (588, 1068), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/SKL_levelup1.png')
        levelup_ui.paste(background, (588, 1068), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/SKL_levelup2.png')
        levelup_ui.paste(background, (588, 1068), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (712, 1088), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (680, 1088), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (712, 1088), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (844, 876), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/SPD_levelup1.png')
        levelup_ui.paste(background, (844, 876), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/SPD_levelup2.png')
        levelup_ui.paste(background, (844, 876), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (968, 896), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (936, 896), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (968, 896), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (844, 940), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/LUK_levelup1.png')
        levelup_ui.paste(background, (844, 940), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/LUK_levelup2.png')
        levelup_ui.paste(background, (844, 940), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (968, 960), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (936, 960), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (968, 960), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (844, 1004), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/DEF_levelup1.png')
        levelup_ui.paste(background, (844, 1004), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/DEF_levelup2.png')
        levelup_ui.paste(background, (844, 1004), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (968, 1024), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (936, 1024), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (968, 1024), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
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
    levelup_ui.paste(lvlup_stat_background, (844, 1068), mask=lvlup_stat_background)
    if levelup_var == 1:
        background = Image.open('UI Resources/Level up tab/SPR_levelup1.png')
        levelup_ui.paste(background, (844, 1068), mask=background)
    if levelup_var == 2:
        background = Image.open('UI Resources/Level up tab/SPR_levelup2.png')
        levelup_ui.paste(background, (844, 1068), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (968, 1088), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        levelup_ui.paste(num_image1, (936, 1088), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        levelup_ui.paste(num_image2, (968, 1088), mask=num_image2)
    levelup_ui_new = ImageTk.PhotoImage(levelup_ui.resize([1000, 600]))
    levelup_ui_label.configure(image=levelup_ui_new)
    levelup_ui_label.image = levelup_ui_new
# </editor-fold>

# <editor-fold desc="Levelup tab - UI">
export_levelup_button = Button(tab_levelup, text='Export', command=export_levelup_image)
export_levelup_button.place(x=130, y=46)

name_levelup_input = Entry(tab_levelup, width=15, justify='center')
name_levelup_input.bind('<KeyRelease>', levelup_name)
class_levelup_input = Entry(tab_levelup, width=15, justify='center')
class_levelup_input.bind('<KeyRelease>', levelup_class)
lvl_levelup_input = Entry(tab_levelup, width=5, justify='center')
lvl_levelup_input.bind('<KeyRelease>', levelup_lvl)
name_levelup_input.place(x=104, y=114)
class_levelup_input.place(x=104, y=146)
lvl_levelup_input.place(x=134, y=178)

lvlup_portrait_names = os.listdir('UI Resources/Unit portraits')
lvlup_portrait_names_no_ext = [os.path.splitext(file)[0] for file in lvlup_portrait_names]
lvlup_unit_name = StringVar()
lvlup_portrait_menu = Combobox(tab_levelup, textvariable=lvlup_unit_name, width=10)
lvlup_portrait_menu['values'] = lvlup_portrait_names_no_ext
lvlup_portrait_menu.bind('<<ComboboxSelected>>', lvlup_portrait_edit)
lvlup_portrait_menu.place(x=352, y=48)

lvlup_custom_portrait_button = Button(tab_levelup, text='Custom', command=lvlup_custom_portrait)
lvlup_custom_portrait_button.place(x=446, y=46)

lvlup_background_names = os.listdir('UI Resources/Battle backgrounds')
lvlup_background_names_no_ext = [os.path.splitext(file)[0] for file in lvlup_background_names]
lvlup_background_name = StringVar()
lvlup_background_menu = Combobox(tab_levelup, textvariable=lvlup_background_name, width=16)
lvlup_background_menu['values'] = lvlup_background_names_no_ext
lvlup_background_menu.bind('<<ComboboxSelected>>', lvlup_background_edit)
lvlup_background_menu.place(x=380, y=112)

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
VIT_levelup_input.place(x=92, y=242)
MGT_levelup_input.place(x=92, y=274)
MND_levelup_input.place(x=92, y=306)
SKL_levelup_input.place(x=92, y=338)
SPD_levelup_input.place(x=92, y=370)
LUK_levelup_input.place(x=92, y=402)
DEF_levelup_input.place(x=92, y=434)
SPR_levelup_input.place(x=92, y=466)

levelup_plus1 = PhotoImage(file = 'UI Resources/Level up tab/plus_1.png')
levelup_plus2 = PhotoImage(file = 'UI Resources/Level up tab/plus_2.png')
VIT_plus1_button = Button(tab_levelup, command = levelup_vit_bg1, image = levelup_plus1, bg='#c0e8a0')
MGT_plus1_button = Button(tab_levelup, command = levelup_mgt_bg1, image = levelup_plus1, bg='#c0e8a0')
MND_plus1_button = Button(tab_levelup, command = levelup_mnd_bg1, image = levelup_plus1, bg='#c0e8a0')
SKL_plus1_button = Button(tab_levelup, command = levelup_skl_bg1, image = levelup_plus1, bg='#c0e8a0')
SPD_plus1_button = Button(tab_levelup, command = levelup_spd_bg1, image = levelup_plus1, bg='#c0e8a0')
LUK_plus1_button = Button(tab_levelup, command = levelup_luk_bg1, image = levelup_plus1, bg='#c0e8a0')
DEF_plus1_button = Button(tab_levelup, command = levelup_def_bg1, image = levelup_plus1, bg='#c0e8a0')
SPR_plus1_button = Button(tab_levelup, command = levelup_spr_bg1, image = levelup_plus1, bg='#c0e8a0')
VIT_plus2_button = Button(tab_levelup, command = levelup_vit_bg2, image = levelup_plus2, bg='#88d8c0')
MGT_plus2_button = Button(tab_levelup, command = levelup_mgt_bg2, image = levelup_plus2, bg='#88d8c0')
MND_plus2_button = Button(tab_levelup, command = levelup_mnd_bg2, image = levelup_plus2, bg='#88d8c0')
SKL_plus2_button = Button(tab_levelup, command = levelup_skl_bg2, image = levelup_plus2, bg='#88d8c0')
SPD_plus2_button = Button(tab_levelup, command = levelup_spd_bg2, image = levelup_plus2, bg='#88d8c0')
LUK_plus2_button = Button(tab_levelup, command = levelup_luk_bg2, image = levelup_plus2, bg='#88d8c0')
DEF_plus2_button = Button(tab_levelup, command = levelup_def_bg2, image = levelup_plus2, bg='#88d8c0')
SPR_plus2_button = Button(tab_levelup, command = levelup_spr_bg2, image = levelup_plus2, bg='#88d8c0')
VIT_plus1_button.place(x=136, y=241)
MGT_plus1_button.place(x=136, y=273)
MND_plus1_button.place(x=136, y=305)
SKL_plus1_button.place(x=136, y=337)
SPD_plus1_button.place(x=136, y=369)
LUK_plus1_button.place(x=136, y=401)
DEF_plus1_button.place(x=136, y=433)
SPR_plus1_button.place(x=136, y=465)
VIT_plus2_button.place(x=168, y=241)
MGT_plus2_button.place(x=168, y=273)
MND_plus2_button.place(x=168, y=305)
SKL_plus2_button.place(x=168, y=337)
SPD_plus2_button.place(x=168, y=369)
LUK_plus2_button.place(x=168, y=401)
DEF_plus2_button.place(x=168, y=433)
SPR_plus2_button.place(x=168, y=465)
# </editor-fold>

# <editor-fold desc="Statsheet tab UI">
image_statsheet = Image.open('UI Resources/Statsheet tab/statsheet_template.png')
image_resize_statsheet = ImageTk.PhotoImage(image_statsheet.resize([780,240]))
statsheet_image = Label(tab_statsheet, image=image_resize_statsheet)
statsheet_image.pack(side=BOTTOM)
# </editor-fold>

window.mainloop()