import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk

# <editor-fold desc="Main window and tabs initial setup">
window = Tk()
window.title("Fire Emblem Akkadia")
window.geometry("1000x750+150+100")
window.resizable(False, False)
window.iconbitmap('UI Resources/fe_akkadia.ico')

tabControl = ttk.Notebook(window)
tab_levelup = Frame(tabControl)
tab_statsheet = Frame(tabControl)
tab_map = Frame(tabControl)

tabControl.add(tab_levelup, text = '  Level up  ')
tabControl.add(tab_statsheet, text = '  Statsheet  ')
tabControl.add(tab_map, text = '  Map  ')
tabControl.pack(expand = 1, fill = 'both')

lvlup_tab_ui = Image.open('UI Resources/Level up tab/levelup_tab_ui.png')
lvlup_tab_background_image = Image.open('UI Resources/Battle backgrounds/Plains.png')
lvlup_tab_template_image = Image.open('UI Resources/Level up tab/levelup_template.png')
lvlup_tab_ui.paste(lvlup_tab_background_image, (520,560), mask=lvlup_tab_background_image)
lvlup_tab_ui.paste(lvlup_tab_template_image, (520,560), mask=lvlup_tab_template_image)
lvlup_tab_ui_resize = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
lvlup_tab_ui_label = Label(tab_levelup, image=lvlup_tab_ui_resize)
lvlup_tab_ui_label.place(x=0, y=0)

statsheet_tab_ui = Image.open('UI Resources/Statsheet tab/statsheet_tab_ui.png')
statsheet_tab_ui_resize = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
statsheet_tab_ui_label = Label(tab_statsheet, image=statsheet_tab_ui_resize)
statsheet_tab_ui_label.place(x=0, y=0)
# </editor-fold>
# -----------------------------------------------------------------------------
# <editor-fold desc="Levelup tab - unit update functions">
def lvlup_export_image():
    filename = asksaveasfile(mode='w', filetypes=(("png files", "*.png"),("all files", "*")), defaultextension='png')
    if not filename:
        return
    lvlup_tab_ui_crop = lvlup_tab_ui.crop([520, 560, 1480, 1200])
    lvlup_tab_ui_crop.save(filename.name)

def lvlup_name_edit(x):
    levelup_str = lvlup_name_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/name_bg.png')
    lvlup_tab_ui.paste(levelup_word_background, (1256, 580), mask=levelup_word_background)
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
        lvlup_tab_ui.paste(letter_image, (word_x_coord, 604), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_class_edit(x):
    levelup_str = lvlup_class_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab/class_bg.png')
    lvlup_tab_ui.paste(levelup_word_background, (552, 740), mask=levelup_word_background)
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
        lvlup_tab_ui.paste(letter_image, (588 + word_x_coord, 764), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_level_edit(x):
    levelup_num = lvlup_level_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/level_bg.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (860, 740), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 768), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 768), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 768), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_portrait_edit(self):
    if lvlup_unit_name.get():
        unit_portrait = Image.open('UI Resources/Unit portraits/' + lvlup_unit_name.get() + '.png').resize((384, 384))
        if lvlup_background_name.get():
            background_image = Image.open('UI Resources/Battle backgrounds/' + lvlup_background_name.get() + '.png')
        else:
            background_image = Image.open('UI Resources/Battle backgrounds/Plains.png')
        background_image_crop = background_image.crop([568, 256, 952, 640])
        lvlup_tab_ui.paste(background_image_crop, (1088, 816))
        lvlup_tab_ui.paste(unit_portrait, (1088, 816), mask=unit_portrait)
        lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
        lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
        lvlup_tab_ui_label.image = lvlup_tab_ui_new
        lvlup_tab_ui.paste(unit_portrait, (1088, 816), mask=unit_portrait)
        lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
        lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
        lvlup_tab_ui_label.image = lvlup_tab_ui_new

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
    lvlup_tab_ui.paste(background_image_crop, (1088, 816))
    lvlup_tab_ui.paste(unit_portrait, (1088, 816), mask=unit_portrait)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_background_edit(self):
    lvlup_tab_ui_crop_stats = lvlup_tab_ui.crop([544, 872, 1072, 1144])
    lvlup_tab_ui_crop_class = lvlup_tab_ui.crop([556, 744, 1060, 824])
    lvlup_tab_ui_crop_name = lvlup_tab_ui.crop([1260, 584, 1480, 664])
    background_image = Image.open('UI Resources/Battle backgrounds/' + lvlup_background_name.get() + '.png')
    lvlup_tab_ui.paste(background_image, (520, 560))
    lvlup_tab_ui_template = Image.open('UI Resources/Level up tab/levelup_template.png')
    lvlup_tab_ui.paste(lvlup_tab_ui_template, (520, 560), mask=lvlup_tab_ui_template)
    lvlup_tab_ui.paste(lvlup_tab_ui_crop_stats, (544, 872))
    lvlup_tab_ui.paste(lvlup_tab_ui_crop_class, (556, 744))
    lvlup_tab_ui.paste(lvlup_tab_ui_crop_name, (1260, 584))
    lvlup_portrait_edit(0)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new
# </editor-fold>

# <editor-fold desc="Levelup tab - stat update functions">
def lvlup_vit_plus1_bg_edit():
    x = 1
    levelup_vit_num_edit(x)
def lvlup_vit_plus2_bg_edit():
    x = 2
    levelup_vit_num_edit(x)
def levelup_vit_num_edit(x):
    levelup_num = lvlup_VIT_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/VIT_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (588, 876), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/VIT_levelup1.png')
        lvlup_tab_ui.paste(background, (588, 876), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/VIT_levelup2.png')
        lvlup_tab_ui.paste(background, (588, 876), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 896), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 896), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 896), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_mgt_plus1_bg_edit():
    x = 1
    levelup_mgt_num_edit(x)
def lvlup_mgt_plus2_bg_edit():
    x = 2
    levelup_mgt_num_edit(x)
def levelup_mgt_num_edit(x):
    levelup_num = lvlup_MGT_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/MGT_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (588, 940), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/MGT_levelup1.png')
        lvlup_tab_ui.paste(background, (588, 940), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/MGT_levelup2.png')
        lvlup_tab_ui.paste(background, (588, 940), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 960), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 960), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 960), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_mnd_plus1_bg_edit():
    x = 1
    levelup_mnd_num_edit(x)
def lvlup_mnd_plus2_bg_edit():
    x = 2
    levelup_mnd_num_edit(x)
def levelup_mnd_num_edit(x):
    levelup_num = lvlup_MND_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/MND_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (588, 1004), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/MND_levelup1.png')
        lvlup_tab_ui.paste(background, (588, 1004), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/MND_levelup2.png')
        lvlup_tab_ui.paste(background, (588, 1004), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 1024), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 1024), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 1024), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_skl_plus1_bg_edit():
    x = 1
    levelup_skl_num_edit(x)
def lvlup_skl_plus2_bg_edit():
    x = 2
    levelup_skl_num_edit(x)
def levelup_skl_num_edit(x):
    levelup_num = lvlup_SKL_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SKL_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (588, 1068), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/SKL_levelup1.png')
        lvlup_tab_ui.paste(background, (588, 1068), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/SKL_levelup2.png')
        lvlup_tab_ui.paste(background, (588, 1068), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 1088), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 1088), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 1088), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_spd_plus1_bg_edit():
    x = 1
    levelup_spd_num_edit(x)
def lvlup_spd_plus2_bg_edit():
    x = 2
    levelup_spd_num_edit(x)
def levelup_spd_num_edit(x):
    levelup_num = lvlup_SPD_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SPD_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (844, 876), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/SPD_levelup1.png')
        lvlup_tab_ui.paste(background, (844, 876), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/SPD_levelup2.png')
        lvlup_tab_ui.paste(background, (844, 876), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 896), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 896), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 896), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_luk_plus1_bg_edit():
    x = 1
    levelup_luk_num_edit(x)
def lvlup_luk_plus2_bg_edit():
    x = 2
    levelup_luk_num_edit(x)
def levelup_luk_num_edit(x):
    levelup_num = lvlup_LUK_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/LUK_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (844, 940), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/LUK_levelup1.png')
        lvlup_tab_ui.paste(background, (844, 940), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/LUK_levelup2.png')
        lvlup_tab_ui.paste(background, (844, 940), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 960), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 960), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 960), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_def_plus1_bg_edit():
    x = 1
    levelup_def_num_edit(x)
def lvlup_def_plus2_bg_edit():
    x = 2
    levelup_def_num_edit(x)
def levelup_def_num_edit(x):
    levelup_num = lvlup_DEF_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/DEF_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (844, 1004), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/DEF_levelup1.png')
        lvlup_tab_ui.paste(background, (844, 1004), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/DEF_levelup2.png')
        lvlup_tab_ui.paste(background, (844, 1004), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 1024), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 1024), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 1024), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_spr_plus1_bg_edit():
    x = 1
    levelup_spr_num_edit(x)
def lvlup_spr_plus2_bg_edit():
    x = 2
    levelup_spr_num_edit(x)
def levelup_spr_num_edit(x):
    levelup_num = lvlup_SPR_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab/SPR_neutral.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (844, 1068), mask=lvlup_stat_background)
    if x == 1:
        background = Image.open('UI Resources/Level up tab/SPR_levelup1.png')
        lvlup_tab_ui.paste(background, (844, 1068), mask=background)
    if x == 2:
        background = Image.open('UI Resources/Level up tab/SPR_levelup2.png')
        lvlup_tab_ui.paste(background, (844, 1068), mask=background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 1088), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 1088), mask=num_image1)
        num_image2 = Image.open('UI Resources/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 1088), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new
# </editor-fold>

# <editor-fold desc="Levelup tab - UI">
lvlup_export_button = Button(tab_levelup, text='Export', width=7, command=lvlup_export_image)
lvlup_export_button.place(x=130, y=46)

lvlup_name_input = Entry(tab_levelup, width=15, justify='center')
lvlup_name_input.bind('<KeyRelease>', lvlup_name_edit)
lvlup_class_input = Entry(tab_levelup, width=15, justify='center')
lvlup_class_input.bind('<KeyRelease>', lvlup_class_edit)
lvlup_level_input = Entry(tab_levelup, width=5, justify='center')
lvlup_level_input.bind('<KeyRelease>', lvlup_level_edit)
lvlup_name_input.place(x=104, y=114)
lvlup_class_input.place(x=104, y=146)
lvlup_level_input.place(x=134, y=178)

lvlup_VIT_input = Entry(tab_levelup, width=5, justify='center')
lvlup_VIT_input.bind('<KeyRelease>', levelup_vit_num_edit)
lvlup_MGT_input = Entry(tab_levelup, width=5, justify='center')
lvlup_MGT_input.bind('<KeyRelease>', levelup_mgt_num_edit)
lvlup_MND_input = Entry(tab_levelup, width=5, justify='center')
lvlup_MND_input.bind('<KeyRelease>', levelup_mnd_num_edit)
lvlup_SKL_input = Entry(tab_levelup, width=5, justify='center')
lvlup_SKL_input.bind('<KeyRelease>', levelup_skl_num_edit)
lvlup_SPD_input = Entry(tab_levelup, width=5, justify='center')
lvlup_SPD_input.bind('<KeyRelease>', levelup_spd_num_edit)
lvlup_LUK_input = Entry(tab_levelup, width=5, justify='center')
lvlup_LUK_input.bind('<KeyRelease>', levelup_luk_num_edit)
lvlup_DEF_input = Entry(tab_levelup, width=5, justify='center')
lvlup_DEF_input.bind('<KeyRelease>', levelup_def_num_edit)
lvlup_SPR_input = Entry(tab_levelup, width=5, justify='center')
lvlup_SPR_input.bind('<KeyRelease>', levelup_spr_num_edit)
lvlup_VIT_input.place(x=92, y=242)
lvlup_MGT_input.place(x=92, y=274)
lvlup_MND_input.place(x=92, y=306)
lvlup_SKL_input.place(x=92, y=338)
lvlup_SPD_input.place(x=92, y=370)
lvlup_LUK_input.place(x=92, y=402)
lvlup_DEF_input.place(x=92, y=434)
lvlup_SPR_input.place(x=92, y=466)

lvlup_plus1_image = PhotoImage(file = 'UI Resources/Level up tab/plus_1.png')
lvlup_plus2_image = PhotoImage(file = 'UI Resources/Level up tab/plus_2.png')
lvlup_VIT_plus1_button = Button(tab_levelup, command = lvlup_vit_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_MGT_plus1_button = Button(tab_levelup, command = lvlup_mgt_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_MND_plus1_button = Button(tab_levelup, command = lvlup_mnd_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_SKL_plus1_button = Button(tab_levelup, command = lvlup_skl_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_SPD_plus1_button = Button(tab_levelup, command = lvlup_spd_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_LUK_plus1_button = Button(tab_levelup, command = lvlup_luk_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_DEF_plus1_button = Button(tab_levelup, command = lvlup_def_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_SPR_plus1_button = Button(tab_levelup, command = lvlup_spr_plus1_bg_edit, image = lvlup_plus1_image, bg='#c0e8a0')
lvlup_VIT_plus2_button = Button(tab_levelup, command = lvlup_vit_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_MGT_plus2_button = Button(tab_levelup, command = lvlup_mgt_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_MND_plus2_button = Button(tab_levelup, command = lvlup_mnd_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_SKL_plus2_button = Button(tab_levelup, command = lvlup_skl_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_SPD_plus2_button = Button(tab_levelup, command = lvlup_spd_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_LUK_plus2_button = Button(tab_levelup, command = lvlup_luk_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_DEF_plus2_button = Button(tab_levelup, command = lvlup_def_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_SPR_plus2_button = Button(tab_levelup, command = lvlup_spr_plus2_bg_edit, image = lvlup_plus2_image, bg='#88d8c0')
lvlup_VIT_plus1_button.place(x=136, y=241)
lvlup_MGT_plus1_button.place(x=136, y=273)
lvlup_MND_plus1_button.place(x=136, y=305)
lvlup_SKL_plus1_button.place(x=136, y=337)
lvlup_SPD_plus1_button.place(x=136, y=369)
lvlup_LUK_plus1_button.place(x=136, y=401)
lvlup_DEF_plus1_button.place(x=136, y=433)
lvlup_SPR_plus1_button.place(x=136, y=465)
lvlup_VIT_plus2_button.place(x=168, y=241)
lvlup_MGT_plus2_button.place(x=168, y=273)
lvlup_MND_plus2_button.place(x=168, y=305)
lvlup_SKL_plus2_button.place(x=168, y=337)
lvlup_SPD_plus2_button.place(x=168, y=369)
lvlup_LUK_plus2_button.place(x=168, y=401)
lvlup_DEF_plus2_button.place(x=168, y=433)
lvlup_SPR_plus2_button.place(x=168, y=465)

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
# </editor-fold>
# -----------------------------------------------------------------------------
# <editor-fold desc="Statsheet tab - unit update functions">
def statsheet_load_image():
    return

def statsheet_export_image():
    return

def statsheet_name_edit(x):
    return

def statsheet_class_edit(x):
    return

def statsheet_level_edit(x):
    return

def statsheet_portrait_edit(self):
    return

def statsheet_custom_portrait():
    return

def statsheet_sprite_edit(self):
    return

def statsheet_custom_sprite():
    return
# </editor-fold>

# <editor-fold desc="Statsheet tab - traits update functions">
def statsheet_trait1_edit(x):
    return

def statsheet_trait2_edit(x):
    return

def statsheet_trait3_edit(x):
    return

def statsheet_trait4_edit(x):
    return
# </editor-fold>

# <editor-fold desc="Statsheet tab - stat update functions">
def statsheet_vit_num_edit(x):
    return

def statsheet_mgt_num_edit(x):
    return

def statsheet_mnd_num_edit(x):
    return

def statsheet_skl_num_edit(x):
    return

def statsheet_spd_num_edit(x):
    return

def statsheet_luk_num_edit(x):
    return

def statsheet_def_num_edit(x):
    return

def statsheet_spr_num_edit(x):
    return
# </editor-fold>

# <editor-fold desc="Statsheet tab - equipment update functions">

# </editor-fold>

# <editor-fold desc="Statsheet tab - proficiency update functions">

# </editor-fold>

# <editor-fold desc="Statsheet tab - supports update functions">

# </editor-fold>

# <editor-fold desc="Statsheet tab - UI">
statsheet_load_button = Button(tab_statsheet, text='Load', width=7, command=statsheet_load_image)
statsheet_export_button = Button(tab_statsheet, text='Export', width=7, command=statsheet_export_image)
statsheet_load_button.place(x=54, y=78)
statsheet_export_button.place(x=129, y=78)

statsheet_name_input = Entry(tab_statsheet, width=15, justify='center')
statsheet_class_input = Entry(tab_statsheet, width=15, justify='center')
statsheet_level_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_name_input.bind('<KeyRelease>', statsheet_name_edit)
statsheet_class_input.bind('<KeyRelease>', statsheet_class_edit)
statsheet_level_input.bind('<KeyRelease>', statsheet_level_edit)
statsheet_name_input.place(x=104, y=146)
statsheet_class_input.place(x=104, y=178)
statsheet_level_input.place(x=134, y=210)

statsheet_trait1_input = Entry(tab_statsheet, width=17, justify='center')
statsheet_trait2_input = Entry(tab_statsheet, width=17, justify='center')
statsheet_trait3_input = Entry(tab_statsheet, width=17, justify='center')
statsheet_trait4_input = Entry(tab_statsheet, width=17, justify='center')
statsheet_trait1_input.bind('<KeyRelease>', statsheet_trait1_edit)
statsheet_trait2_input.bind('<KeyRelease>', statsheet_trait2_edit)
statsheet_trait3_input.bind('<KeyRelease>', statsheet_trait3_edit)
statsheet_trait4_input.bind('<KeyRelease>', statsheet_trait4_edit)
statsheet_trait1_input.place(x=52, y=305)
statsheet_trait2_input.place(x=52, y=337)
statsheet_trait3_input.place(x=52, y=369)
statsheet_trait4_input.place(x=52, y=401)

statsheet_VIT_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_MGT_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_MND_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_SKL_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_SPD_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_LUK_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_DEF_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_SPR_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_VIT_input.bind('<KeyRelease>', statsheet_vit_num_edit)
statsheet_MGT_input.bind('<KeyRelease>', statsheet_mgt_num_edit)
statsheet_MND_input.bind('<KeyRelease>', statsheet_mnd_num_edit)
statsheet_SKL_input.bind('<KeyRelease>', statsheet_skl_num_edit)
statsheet_SPD_input.bind('<KeyRelease>', statsheet_spd_num_edit)
statsheet_LUK_input.bind('<KeyRelease>', statsheet_luk_num_edit)
statsheet_DEF_input.bind('<KeyRelease>', statsheet_def_num_edit)
statsheet_SPR_input.bind('<KeyRelease>', statsheet_spr_num_edit)
statsheet_VIT_input.place(x=310, y=145)
statsheet_MGT_input.place(x=310, y=177)
statsheet_MND_input.place(x=310, y=209)
statsheet_SKL_input.place(x=310, y=241)
statsheet_SPD_input.place(x=310, y=273)
statsheet_LUK_input.place(x=310, y=305)
statsheet_DEF_input.place(x=310, y=337)
statsheet_SPR_input.place(x=310, y=369)
# </editor-fold>

window.mainloop()