import os
from tkinter import ttk, Tk, Frame, Label, Button, Entry, StringVar
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfilename, asksaveasfile
from PIL import Image, ImageTk

# <editor-fold desc="Main window and tabs initial setup">
window = Tk()
window.title("Fire Emblem Akkadia")
window.geometry("1000x750+150+20")
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

lvlup_tab_ui = Image.open('UI Resources/Level up tab UI/levelup_tab_ui.png')
lvlup_tab_background_image = Image.open('UI Resources/Battle backgrounds/Plains.png')
lvlup_tab_main_image = Image.open('UI Resources/Level up tab UI/levelup_template.png')
lvlup_tab_ui.paste(lvlup_tab_background_image, (520,560), mask=lvlup_tab_background_image)
lvlup_tab_ui.paste(lvlup_tab_main_image, (520,560), mask=lvlup_tab_main_image)
lvlup_tab_ui_resize = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
lvlup_tab_ui_label = Label(tab_levelup, image=lvlup_tab_ui_resize)
lvlup_tab_ui_label.place(x=0, y=0)

statsheet_tab_ui = Image.open('UI Resources/Statsheet tab UI/statsheet_tab_ui.png')
statsheet_tab_main_image = Image.open('UI Resources/Statsheet tab UI/statsheet_template.png')
statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
statsheet_tab_ui_resize = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
statsheet_tab_ui_label = Label(tab_statsheet, image=statsheet_tab_ui_resize)
statsheet_tab_ui_label.place(x=0, y=0)

map_tab_ui = Image.open('UI Resources/Map tab/map_tab_ui.png')
map_tab_ui_resize = ImageTk.PhotoImage(map_tab_ui.resize([1000, 750]))
map_tab_ui_label = Label(tab_map, image=map_tab_ui_resize)
map_tab_ui_label.place(x=0, y=0)

portrait_names_hellions = os.listdir('UI Resources/Unit portraits/Hellions')
portrait_names_hellions_no_ext = [os.path.splitext(file)[0] for file in portrait_names_hellions]
portrait_names_allies = os.listdir('UI Resources/Unit portraits/Allies')
portrait_names_allies_no_ext = [os.path.splitext(file)[0] for file in portrait_names_allies]
portrait_names_foes = os.listdir('UI Resources/Unit portraits/Foes')
portrait_names_foes_no_ext = [os.path.splitext(file)[0] for file in portrait_names_foes]
portrait_names_generic_units = os.listdir('UI Resources/Unit portraits/Generic units')
portrait_names_generic_units_no_ext = [os.path.splitext(file)[0] for file in portrait_names_generic_units]
portrait_names_monsters = os.listdir('UI Resources/Unit portraits/Monsters')
portrait_names_monsters_no_ext = [os.path.splitext(file)[0] for file in portrait_names_monsters]

sprite_names_hellions = os.listdir('UI Resources/Unit sprites/Hellions')
sprite_names_hellions_no_ext = [os.path.splitext(file)[0] for file in sprite_names_hellions]
sprite_names_allies = os.listdir('UI Resources/Unit sprites/Allies')
sprite_names_allies_no_ext = [os.path.splitext(file)[0] for file in sprite_names_allies]
sprite_names_foes = os.listdir('UI Resources/Unit sprites/Foes')
sprite_names_foes_no_ext = [os.path.splitext(file)[0] for file in sprite_names_foes]

equipment_file = open('UI Resources/Equipment sprites/- Equipment list.txt', 'r')
equipment_list = equipment_file.read().splitlines()
equipment_images = os.listdir('UI Resources/Equipment sprites')
equipment_images_no_ext = [os.path.splitext(file)[0] for file in equipment_images]

rank_levels = ['S', 'A', 'B', 'C', 'D', 'E', 'None']
affinity_types = ['Fire', 'Thunder', 'Wind', 'Ice', 'Dark', 'Light', 'Anima', 'None']
weapon_types = ['Swords', 'Axes', 'Spears', 'Bows', 'Mysticism', 'Grave', 'Light', 'Theurgy', 'None']
# </editor-fold>
# -----------------------------------------------------------------------------
# <editor-fold desc="Levelup tab - unit update functions">
def lvlup_export_image():
    filename = asksaveasfile(mode='w', filetypes=(("png files", "*.png"),("all files", "*")), defaultextension='png')
    if not filename:
        return
    lvlup_tab_ui_crop = lvlup_tab_ui.crop([520, 560, 1480, 1200])
    lvlup_tab_ui_crop.save(filename.name)

def lvlup_name_edit(self):
    levelup_str = lvlup_name_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab UI/name_bg.png')
    lvlup_tab_ui.paste(levelup_word_background, (1256, 580), mask=levelup_word_background)
    word_x_coord = 0
    word_size_px = 4
    # loop to check how long the word is in pixels, -4 because of overlap
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/Dark font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/Dark font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/Dark font/' + letter + '.png')
        word_size_px += letter_image.size[0] - 4
    word_x_coord = 1384 - int(word_size_px / 2) # 1384 is half the size of the target area
    # loop to paste letters images one by one
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/Dark font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/Dark font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/Dark font/' + letter + '.png')
        lvlup_tab_ui.paste(letter_image, (word_x_coord, 604), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    # resize and merge back with tab UI
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_class_edit(self):
    levelup_str = lvlup_class_input.get()
    levelup_word_background = Image.open('UI Resources/Level up tab UI/class_bg.png')
    lvlup_tab_ui.paste(levelup_word_background, (552, 740), mask=levelup_word_background)
    word_x_coord = 0
    for letter in levelup_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        lvlup_tab_ui.paste(letter_image, (588 + word_x_coord, 764), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_level_edit(self):
    levelup_num = lvlup_level_input.get()
    lvlup_stat_background = Image.open('UI Resources/Level up tab UI/level_bg.png')
    lvlup_tab_ui.paste(lvlup_stat_background, (860, 740), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 768), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 768), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 768), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def lvlup_portrait_edit(self):
    unit_name = lvlup_unit_name.get().capitalize()
    if unit_name in portrait_names_hellions_no_ext:
        folder = 'Hellions'
    elif unit_name in portrait_names_allies_no_ext:
        folder = 'Allies'
    elif unit_name in portrait_names_foes_no_ext:
        folder = 'Foes'
    else:
        folder = ''
    if folder in ['Hellions', 'Allies', 'Foes']:
        unit_portrait = Image.open('UI Resources/Unit portraits/' + folder + '/' + unit_name + '.png').resize((384, 384))
    else:
        unit_portrait = Image.open('UI Resources/Unit portraits/empty_portrait.png')
    if lvlup_background_name.get().capitalize() in lvlup_background_names_no_ext:
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
    new_display = os.path.split(filename)[1]
    lvlup_unit_name.set(os.path.splitext(new_display)[0])

def lvlup_background_edit(self):
    lvlup_tab_ui_crop_stats = lvlup_tab_ui.crop([544, 872, 1072, 1144])
    lvlup_tab_ui_crop_class = lvlup_tab_ui.crop([556, 744, 1060, 824])
    lvlup_tab_ui_crop_name = lvlup_tab_ui.crop([1260, 584, 1480, 664])
    background_image = Image.open('UI Resources/Battle backgrounds/' + lvlup_background_name.get() + '.png')
    lvlup_tab_ui.paste(background_image, (520, 560))
    lvlup_tab_ui_template = Image.open('UI Resources/Level up tab UI/levelup_template.png')
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
def levelup_vit_edit(self):
    levelup_num = lvlup_VIT_input.get()
    levelup_plus = lvlup_VIT_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/VIT_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 876), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (760, 876), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/VIT_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 876), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 896), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 896), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 896), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_mgt_edit(self):
    levelup_num = lvlup_MGT_input.get()
    levelup_plus = lvlup_MGT_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/MGT_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 940), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (760, 940), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/MGT_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 940), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 960), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 960), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 960), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_mnd_edit(self):
    levelup_num = lvlup_MND_input.get()
    levelup_plus = lvlup_MND_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/MND_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 1004), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (760, 1004), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/MND_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 1004), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 1024), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 1024), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 1024), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_skl_edit(self):
    levelup_num = lvlup_SKL_input.get()
    levelup_plus = lvlup_SKL_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/SKL_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 1068), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (760, 1068), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/SKL_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (588, 1068), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (712, 1088), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (680, 1088), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (712, 1088), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_spd_edit(self):
    levelup_num = lvlup_SPD_input.get()
    levelup_plus = lvlup_SPD_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/SPD_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 876), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (1016, 876), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/SPD_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 876), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 896), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 896), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 896), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_luk_edit(self):
    levelup_num = lvlup_LUK_input.get()
    levelup_plus = lvlup_LUK_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/LUK_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 940), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (1016, 940), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/LUK_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 940), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 960), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 960), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 960), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_def_edit(self):
    levelup_num = lvlup_DEF_input.get()
    levelup_plus = lvlup_DEF_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/DEF_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 1004), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (1016, 1004), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/DEF_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 1004), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 1024), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 1024), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 1024), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new

def levelup_spr_edit(self):
    levelup_num = lvlup_SPR_input.get()
    levelup_plus = lvlup_SPR_plus_input.get()
    if levelup_plus in ['1','2','3','4','5', '6']:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/SPR_levelup.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 1068), mask=lvlup_stat_background)
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/plus_' + levelup_plus + '.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (1016, 1068), mask=lvlup_stat_background)
    else:
        lvlup_stat_background = Image.open('UI Resources/Level up tab UI/SPR_neutral.png')
        lvlup_tab_ui.paste(lvlup_stat_background, (844, 1068), mask=lvlup_stat_background)
    if len(levelup_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (968, 1088), mask=num_image1)
    if len(levelup_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + levelup_num[0] + '.png')
        lvlup_tab_ui.paste(num_image1, (936, 1088), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + levelup_num[1] + '.png')
        lvlup_tab_ui.paste(num_image2, (968, 1088), mask=num_image2)
    lvlup_tab_ui_new = ImageTk.PhotoImage(lvlup_tab_ui.resize([1000, 750]))
    lvlup_tab_ui_label.configure(image=lvlup_tab_ui_new)
    lvlup_tab_ui_label.image = lvlup_tab_ui_new
# </editor-fold>

# <editor-fold desc="Levelup tab - UI">
lvlup_export_button = Button(tab_levelup, text='Export', width=7, command=lvlup_export_image)
lvlup_export_button.place(x=130, y=46)

lvlup_name_input = Entry(tab_levelup, width=15, justify='center')
lvlup_class_input = Entry(tab_levelup, width=15, justify='center')
lvlup_level_input = Entry(tab_levelup, width=5, justify='center')
lvlup_name_input.bind('<KeyRelease>', lvlup_name_edit)
lvlup_class_input.bind('<KeyRelease>', lvlup_class_edit)
lvlup_level_input.bind('<KeyRelease>', lvlup_level_edit)
lvlup_name_input.place(x=104, y=114)
lvlup_class_input.place(x=104, y=146)
lvlup_level_input.place(x=134, y=178)

lvlup_VIT_input = Entry(tab_levelup, width=6, justify='center')
lvlup_MGT_input = Entry(tab_levelup, width=6, justify='center')
lvlup_MND_input = Entry(tab_levelup, width=6, justify='center')
lvlup_SKL_input = Entry(tab_levelup, width=6, justify='center')
lvlup_SPD_input = Entry(tab_levelup, width=6, justify='center')
lvlup_LUK_input = Entry(tab_levelup, width=6, justify='center')
lvlup_DEF_input = Entry(tab_levelup, width=6, justify='center')
lvlup_SPR_input = Entry(tab_levelup, width=6, justify='center')
lvlup_VIT_input.bind('<KeyRelease>', levelup_vit_edit)
lvlup_MGT_input.bind('<KeyRelease>', levelup_mgt_edit)
lvlup_MND_input.bind('<KeyRelease>', levelup_mnd_edit)
lvlup_SKL_input.bind('<KeyRelease>', levelup_skl_edit)
lvlup_SPD_input.bind('<KeyRelease>', levelup_spd_edit)
lvlup_LUK_input.bind('<KeyRelease>', levelup_luk_edit)
lvlup_DEF_input.bind('<KeyRelease>', levelup_def_edit)
lvlup_SPR_input.bind('<KeyRelease>', levelup_spr_edit)
lvlup_VIT_input.place(x=94, y=242)
lvlup_MGT_input.place(x=94, y=274)
lvlup_MND_input.place(x=94, y=306)
lvlup_SKL_input.place(x=94, y=338)
lvlup_SPD_input.place(x=94, y=370)
lvlup_LUK_input.place(x=94, y=402)
lvlup_DEF_input.place(x=94, y=434)
lvlup_SPR_input.place(x=94, y=466)

lvlup_VIT_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_MGT_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_MND_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_SKL_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_SPD_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_LUK_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_DEF_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_SPR_plus_input = Entry(tab_levelup, width=6, justify='center')
lvlup_VIT_plus_input.bind('<KeyRelease>', levelup_vit_edit)
lvlup_MGT_plus_input.bind('<KeyRelease>', levelup_mgt_edit)
lvlup_MND_plus_input.bind('<KeyRelease>', levelup_mnd_edit)
lvlup_SKL_plus_input.bind('<KeyRelease>', levelup_skl_edit)
lvlup_SPD_plus_input.bind('<KeyRelease>', levelup_spd_edit)
lvlup_LUK_plus_input.bind('<KeyRelease>', levelup_luk_edit)
lvlup_DEF_plus_input.bind('<KeyRelease>', levelup_def_edit)
lvlup_SPR_plus_input.bind('<KeyRelease>', levelup_spr_edit)
lvlup_VIT_plus_input.place(x=158, y=241)
lvlup_MGT_plus_input.place(x=158, y=273)
lvlup_MND_plus_input.place(x=158, y=305)
lvlup_SKL_plus_input.place(x=158, y=337)
lvlup_SPD_plus_input.place(x=158, y=369)
lvlup_LUK_plus_input.place(x=158, y=401)
lvlup_DEF_plus_input.place(x=158, y=433)
lvlup_SPR_plus_input.place(x=158, y=465)

lvlup_unit_name = StringVar()
lvlup_portrait_menu = Combobox(tab_levelup, textvariable=lvlup_unit_name, width=10, justify='center')
lvlup_portrait_menu['values'] = [''] + ['- HELLIONS -'] + portrait_names_hellions_no_ext + [''] + ['- ALLIES -'] + portrait_names_allies_no_ext + [''] + ['- FOES -'] + portrait_names_foes_no_ext
lvlup_portrait_menu.bind('<<ComboboxSelected>>', lvlup_portrait_edit)
lvlup_portrait_menu.bind('<KeyRelease>', lvlup_portrait_edit)
lvlup_portrait_menu.place(x=352, y=48)

lvlup_custom_portrait_button = Button(tab_levelup, text='Custom', command=lvlup_custom_portrait)
lvlup_custom_portrait_button.place(x=446, y=46)

lvlup_background_names = os.listdir('UI Resources/Battle backgrounds')
lvlup_background_names_no_ext = [os.path.splitext(file)[0] for file in lvlup_background_names]
lvlup_background_name = StringVar()
lvlup_background_name.set('Plains')
lvlup_background_menu = Combobox(tab_levelup, textvariable=lvlup_background_name, width=16, justify='center')
lvlup_background_menu['values'] = lvlup_background_names_no_ext
lvlup_background_menu.bind('<<ComboboxSelected>>', lvlup_background_edit)
lvlup_background_menu.bind('<KeyRelease>', lvlup_background_edit)
lvlup_background_menu.place(x=380, y=112)
# </editor-fold>
# -----------------------------------------------------------------------------
# <editor-fold desc="Statsheet tab - unit update functions">
def statsheet_load_image():
    filename = askopenfilename(initialdir='Desktop', title='Select an image', filetypes=(("png files", "*.png"),("all files", "*")))
    if not filename:
        return
    loaded_statsheet = Image.open(filename)
    statsheet_tab_main_image.paste(loaded_statsheet.resize([2080, 640]), (0, 0))
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_export_image():
    filename = asksaveasfile(mode='w', filetypes=(("png files", "*.png"),("all files", "*")), defaultextension='png')
    if not filename:
        return
    statsheet_tab_ui_crop = statsheet_tab_ui.crop([216, 912, 1776, 1392]).resize([1560, 480])
    statsheet_tab_ui_crop.save(filename.name)

def statsheet_name_edit(self):
    statsheet_str = statsheet_name_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/name_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (16, 332))
    word_size_px = 4
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/Dark font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/Dark font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/Dark font/' + letter + '.png')
        word_size_px += letter_image.size[0] - 4
    word_x_coord = 236 - int(word_size_px / 2)
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (word_x_coord, 332), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_class_edit(self):
    statsheet_str = statsheet_class_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/class_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (32, 428), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (32 + word_x_coord, 428), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_level_edit(self):
    statsheet_num = statsheet_level_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/level_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (28, 488), mask=statsheet_word_background)
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (128, 500), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (128, 500), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (160, 500), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_portrait_edit(self):
    statsheet_portrait_background = Image.open('UI Resources/Statsheet tab UI/portrait_bg.png')
    statsheet_tab_main_image.paste(statsheet_portrait_background, (16, 16))
    if statsheet_portrait_name.get().capitalize() in portrait_names_hellions_no_ext:
        folder = 'Hellions'
    elif statsheet_portrait_name.get().capitalize() in portrait_names_allies_no_ext:
        folder = 'Allies'
    elif statsheet_portrait_name.get().capitalize() in portrait_names_foes_no_ext:
        folder = 'Foes'
    elif statsheet_portrait_name.get().capitalize() in portrait_names_generic_units_no_ext:
        folder = 'Generic units'
    elif statsheet_portrait_name.get().capitalize() in portrait_names_monsters_no_ext:
        folder = 'Monsters'
    else:
        unit_portrait = Image.open('UI Resources/Unit portraits/empty_portrait.png')
        unit_portrait_crop = unit_portrait.crop([24, 68, 344, 356])
        return
    unit_portrait = Image.open('UI Resources/Unit portraits/' + folder + '/' + statsheet_portrait_name.get() + '.png')
    if folder in ['Hellions', 'Allies', 'Foes']:
        unit_portrait_crop = unit_portrait.resize((384, 384)).crop([24, 68, 344, 356])
        statsheet_tab_main_image.paste(unit_portrait_crop, (32, 32), mask=unit_portrait_crop)
    if folder in ['Generic units', 'Monsters']:
        statsheet_tab_main_image.paste(unit_portrait, (32, 32), mask=unit_portrait)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_custom_portrait():
    filename = askopenfilename(initialdir='UI Resources/Unit portraits', title='Select an image',
                               filetypes=(("png files", "*.png"),("all files", "*")))
    if not filename:
        return
    statsheet_portrait_background = Image.open('UI Resources/Statsheet tab UI/portrait_bg.png')
    statsheet_tab_main_image.paste(statsheet_portrait_background, (16, 16))
    unit_portrait = Image.open(filename).resize((384, 384))
    unit_portrait_crop = unit_portrait.crop([24, 68, 344, 356])
    statsheet_tab_main_image.paste(unit_portrait_crop, (32, 32), mask=unit_portrait_crop)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
    new_display = os.path.split(filename)[1]
    statsheet_portrait_name.set(os.path.splitext(new_display)[0])

def statsheet_sprite_edit(self):
    statsheet_sprite_background = Image.open('UI Resources/Statsheet tab UI/unit_sprite_bg.png')
    statsheet_tab_main_image.paste(statsheet_sprite_background, (256, 416))
    unit_sprite = statsheet_sprite_name.get().capitalize()
    if unit_sprite in sprite_names_hellions_no_ext:
        folder = 'Hellions'
    elif unit_sprite in sprite_names_allies_no_ext:
        folder = 'Allies'
    elif unit_sprite in sprite_names_foes_no_ext:
        folder = 'Foes'
    else:
        return
    statsheet_unit_sprite_image = Image.open('UI Resources/Unit sprites/'+ folder + '/' + unit_sprite + '.png').resize((128, 128))
    statsheet_tab_main_image.paste(statsheet_unit_sprite_image, (256, 422), mask=statsheet_unit_sprite_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_custom_sprite():
    filename = askopenfilename(initialdir='UI Resources/Unit sprites', title='Select an image',
                               filetypes=(("png files", "*.png"), ("all files", "*")))
    if not filename:
        return
    statsheet_sprite_background = Image.open('UI Resources/Statsheet tab UI/unit_sprite_bg.png')
    statsheet_tab_main_image.paste(statsheet_sprite_background, (256, 416))
    statsheet_unit_sprite_image = Image.open(filename).resize((128, 128))
    statsheet_tab_main_image.paste(statsheet_unit_sprite_image, (256, 422), mask=statsheet_unit_sprite_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
    new_display = os.path.split(filename)[1]
    statsheet_sprite_name.set(os.path.splitext(new_display)[0])
# </editor-fold>

# <editor-fold desc="Statsheet tab - traits update functions">
def statsheet_trait1_edit(self):
    statsheet_str = statsheet_trait1_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/trait1_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (672, 324), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (672 + word_x_coord, 324), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_trait2_edit(self):
    statsheet_str = statsheet_trait2_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/trait2_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (672, 380), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (672 + word_x_coord, 380), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_trait3_edit(self):
    statsheet_str = statsheet_trait3_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/trait3_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (672, 436), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (672 + word_x_coord, 436), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_trait4_edit(self):
    statsheet_str = statsheet_trait4_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/trait4_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (672, 492), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (672 + word_x_coord, 492), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
# </editor-fold>

# <editor-fold desc="Statsheet tab - stat update functions">
def statsheet_vit_num_edit(self):
    statsheet_num = statsheet_VIT_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/hp_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (28, 556))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (160, 564), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (128, 564), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (160, 564), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_mgt_num_edit(self):
    statsheet_num = statsheet_MGT_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 116))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 116))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 132))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 116), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 116), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 116), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 116))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 132))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 116), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 116), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_mnd_num_edit(self):
    statsheet_num = statsheet_MND_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 180))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 180))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 196))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 180), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 180), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 180), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 180))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 196))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 180), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 180), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_skl_num_edit(self):
    statsheet_num = statsheet_SKL_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 244))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 244))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 260))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 244), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 244), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 244), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 244))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 260))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 244), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 244), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_spd_num_edit(self):
    statsheet_num = statsheet_SPD_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 308))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 308))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 324))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 308), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 308), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 308), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 308))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 324))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 308), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 308), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_luk_num_edit(self):
    statsheet_num = statsheet_LUK_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 372))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 372))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 388))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 372), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 372), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 372), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 372))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 388))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 372), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 372), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_def_num_edit(self):
    statsheet_num = statsheet_DEF_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 436))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 436))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 452))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 436), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 436), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 436), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 436))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 452))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 436), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 436), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_spr_num_edit(self):
    statsheet_num = statsheet_SPR_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 500))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 500))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 516))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (544, 500), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (512, 500), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (544, 500), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (496, 500))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (496, 516))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (512, 500), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (544, 500), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_mov_num_edit(self):
    statsheet_num = statsheet_MOV_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/movement_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (764, 116))
    elif 0 <= int(statsheet_num) <= 13:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/movement_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (764, 116))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/movement_statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (764, 132))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (800, 116), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (768, 116), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (800, 116), mask=num_image2)
    elif 14 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/movement_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (764, 116))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/movement_statbar_13.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (764, 132))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (768, 116), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (800, 116), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_mount_edit(self):
    mount_type = statsheet_mount_type_input.get().capitalize()
    if mount_type in ['Horse', 'Pegasus', 'Wyvern']:
        statsheet_mount_background = Image.open('UI Resources/Statsheet tab UI/mount_icon_bg.png')
        statsheet_mount_image = Image.open('UI Resources/Statsheet tab UI/' + mount_type + '_icon.png')
        statsheet_tab_main_image.paste(statsheet_mount_background, (844, 96))
        statsheet_tab_main_image.paste(statsheet_mount_image, (844, 96), mask=statsheet_mount_image)
    elif mount_type == 'None':
        statsheet_mount_image = Image.open('UI Resources/Statsheet tab UI/mount_icon_bg.png')
        statsheet_tab_main_image.paste(statsheet_mount_image, (844, 96))
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_con_num_edit(self):
    statsheet_num = statsheet_CON_input.get()
    if statsheet_num == '':
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (752, 180))
    elif 0 <= int(statsheet_num) <= 20:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (752, 180))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_' + statsheet_num + '.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (752, 196))
        if len(statsheet_num) == 1:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (800, 180), mask=num_image1)
        elif len(statsheet_num) == 2:
            num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
            statsheet_tab_main_image.paste(num_image1, (768, 180), mask=num_image1)
            num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
            statsheet_tab_main_image.paste(num_image2, (800, 180), mask=num_image2)
    elif 21 <= int(statsheet_num) <= 99:
        statsheet_num_background = Image.open('UI Resources/Statsheet tab UI/stat_num_bg.png')
        statsheet_tab_main_image.paste(statsheet_num_background, (752, 180))
        statsheet_statbar_image = Image.open('UI Resources/Statsheet tab UI/statbar_20.png')
        statsheet_tab_main_image.paste(statsheet_statbar_image, (752, 196))
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (768, 180), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (800, 180), mask=num_image2)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_unit_affinity_edit(self):
    affinity_type = statsheet_unit_affinity_type.get().capitalize()
    if affinity_type in ['Fire', 'Thunder', 'Wind', 'Ice', 'Dark', 'Light', 'Anima']:
        statsheet_affinity_background = Image.open('UI Resources/Statsheet tab UI/affinity_stat_bg.png')
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/' + affinity_type + '_affinity.png')
        statsheet_tab_main_image.paste(statsheet_affinity_background, (772, 232))
        statsheet_tab_main_image.paste(statsheet_affinity_image, (772, 232), mask=statsheet_affinity_image)
    elif affinity_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/no_affinity.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (772, 232))
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
# </editor-fold>

# <editor-fold desc="Statsheet tab - equipment update functions">
def statsheet_equipped_item_edit(self):
    return

def statsheet_equip1_edit(self):
    statsheet_str = statsheet_equip1_input.get().capitalize()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/no_equip_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1040, 108))
    if statsheet_str == '':
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 96))
    elif statsheet_str in equipment_images_no_ext:
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 96))
        statsheet_weapon_image = Image.open('UI Resources/Equipment sprites/' + statsheet_str + '.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image, (976, 96), mask=statsheet_weapon_image)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1040 + word_x_coord, 108), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_equip2_edit(self):
    statsheet_str = statsheet_equip2_input.get().capitalize()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/no_equip_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1040, 172))
    if statsheet_str == '':
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 160))
    elif statsheet_str in equipment_images_no_ext:
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 160))
        statsheet_weapon_image = Image.open('UI Resources/Equipment sprites/' + statsheet_str + '.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image, (976, 160), mask=statsheet_weapon_image)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1040 + word_x_coord, 172), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_equip3_edit(self):
    statsheet_str = statsheet_equip3_input.get().capitalize()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/no_equip_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1040, 236))
    if statsheet_str == '':
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 224))
    elif statsheet_str in equipment_images_no_ext:
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 224))
        statsheet_weapon_image = Image.open('UI Resources/Equipment sprites/' + statsheet_str + '.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image, (976, 224), mask=statsheet_weapon_image)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1040 + word_x_coord, 236), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_equip4_edit(self):
    statsheet_str = statsheet_equip4_input.get().capitalize()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/no_equip_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1040, 300))
    if statsheet_str == '':
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 288))
    elif statsheet_str in equipment_images_no_ext:
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 288))
        statsheet_weapon_image = Image.open('UI Resources/Equipment sprites/' + statsheet_str + '.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image, (976, 288), mask=statsheet_weapon_image)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1040 + word_x_coord, 300), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_equip5_edit(self):
    statsheet_str = statsheet_equip5_input.get().capitalize()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/no_equip_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1040, 364))
    if statsheet_str == '':
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 352))
    elif statsheet_str in equipment_images_no_ext:
        statsheet_weapon_image_background = Image.open('UI Resources/Statsheet tab UI/equip_sprite_bg.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image_background, (976, 352))
        statsheet_weapon_image = Image.open('UI Resources/Equipment sprites/' + statsheet_str + '.png')
        statsheet_tab_main_image.paste(statsheet_weapon_image, (976, 352), mask=statsheet_weapon_image)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1040 + word_x_coord, 364), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_equip1_uses_edit(self):
    return

def statsheet_equip2_uses_edit(self):
    return

def statsheet_equip3_uses_edit(self):
    return

def statsheet_equip4_uses_edit(self):
    return

def statsheet_equip5_uses_edit(self):
    return

def statsheet_weapon_attack_edit(self):
    statsheet_num = statsheet_weapon_attack_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/weapon_stat_bg_2num.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1168, 436))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1200, 436), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1168, 436), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1200, 436), mask=num_image2)
    if statsheet_num == '':
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1168, 428), mask=num_dash)
        statsheet_tab_main_image.paste(num_dash, (1200, 428), mask=num_dash)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_weapon_critical_edit(self):
    statsheet_num = statsheet_weapon_critical_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/weapon_stat_bg_2num.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1392, 436))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1424, 436), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1392, 436), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1424, 436), mask=num_image2)
    if statsheet_num == '':
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1392, 428), mask=num_dash)
        statsheet_tab_main_image.paste(num_dash, (1424, 428), mask=num_dash)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_weapon_accuracy_edit(self):
    statsheet_num = statsheet_weapon_accuracy_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/weapon_stat_bg_3num.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1136, 500))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1200, 500), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1168, 500), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1200, 500), mask=num_image2)
    if len(statsheet_num) == 3:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1136, 500), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1168, 500), mask=num_image2)
        num_image3 = Image.open('UI Resources/Fonts/num' + statsheet_num[2] + '.png')
        statsheet_tab_main_image.paste(num_image3, (1200, 500), mask=num_image3)
    if statsheet_num == '':
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1168, 492), mask=num_dash)
        statsheet_tab_main_image.paste(num_dash, (1200, 492), mask=num_dash)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_weapon_avoid_edit(self):
    statsheet_num = statsheet_weapon_avoid_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/weapon_stat_bg_2num.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1392, 500))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1424, 500), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1392, 500), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1424, 500), mask=num_image2)
    if statsheet_num == '':
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1392, 492), mask=num_dash)
        statsheet_tab_main_image.paste(num_dash, (1424, 492), mask=num_dash)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_weapon_weight_edit(self):
    statsheet_num = statsheet_weapon_weight_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/weapon_stat_bg_2num.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1168, 564))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1200, 564), mask=num_image1)
    if len(statsheet_num) == 2:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1168, 564), mask=num_image1)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[1] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1200, 564), mask=num_image2)
    if statsheet_num == '':
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1168, 556), mask=num_dash)
        statsheet_tab_main_image.paste(num_dash, (1200, 556), mask=num_dash)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_weapon_range_edit(self):
    statsheet_num = statsheet_weapon_range_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/weapon_stat_bg_3num.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1360, 564))
    if len(statsheet_num) == 1:
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1424, 564), mask=num_image1)
    if len(statsheet_num) == 3 and statsheet_num[1] == '-':
        num_image1 = Image.open('UI Resources/Fonts/num' + statsheet_num[0] + '.png')
        statsheet_tab_main_image.paste(num_image1, (1364, 564), mask=num_image1)
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1392, 560), mask=num_dash)
        num_image2 = Image.open('UI Resources/Fonts/num' + statsheet_num[2] + '.png')
        statsheet_tab_main_image.paste(num_image2, (1424, 564), mask=num_image2)
    if statsheet_num == '':
        num_dash = Image.open('UI Resources/Statsheet tab UI/rank_none.png')
        statsheet_tab_main_image.paste(num_dash, (1392, 556), mask=num_dash)
        statsheet_tab_main_image.paste(num_dash, (1424, 556), mask=num_dash)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
# </editor-fold>

# <editor-fold desc="Statsheet tab - proficiency update functions">
def statsheet_proficiency_type1_edit(self):
    weapon_type = statsheet_proficiency_type1_input.get().capitalize()
    if weapon_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_icon_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1540, 100))
    elif weapon_type in weapon_types:
        statsheet_affinity_image = Image.open('UI Resources/Weapon proficiency icons/' + weapon_type + '_icon.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1540, 100), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_type2_edit(self):
    weapon_type = statsheet_proficiency_type2_input.get().capitalize()
    if weapon_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_icon_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1796, 100))
    elif weapon_type in weapon_types:
        statsheet_affinity_image = Image.open('UI Resources/Weapon proficiency icons/' + weapon_type + '_icon.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1796, 100), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_type3_edit(self):
    weapon_type = statsheet_proficiency_type3_input.get().capitalize()
    if weapon_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_icon_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1540, 164))
    elif weapon_type in weapon_types:
        statsheet_affinity_image = Image.open('UI Resources/Weapon proficiency icons/' + weapon_type + '_icon.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1540, 164), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_type4_edit(self):
    weapon_type = statsheet_proficiency_type4_input.get().capitalize()
    if weapon_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_icon_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1796, 164))
    elif weapon_type in weapon_types:
        statsheet_affinity_image = Image.open('UI Resources/Weapon proficiency icons/' + weapon_type + '_icon.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1796, 164), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_rank1_edit(self):
    proficiency_rank = statsheet_proficiency_rank1_input.get().capitalize()
    if proficiency_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + proficiency_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1692, 108))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1692, 108), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_rank2_edit(self):
    proficiency_rank = statsheet_proficiency_rank2_input.get().capitalize()
    if proficiency_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + proficiency_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1948, 108))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1948, 108), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_rank3_edit(self):
    proficiency_rank = statsheet_proficiency_rank3_input.get().capitalize()
    if proficiency_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + proficiency_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1692, 172))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1692, 172), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_proficiency_rank4_edit(self):
    proficiency_rank = statsheet_proficiency_rank4_input.get().capitalize()
    if proficiency_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/weapon_proficiency_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + proficiency_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1948, 172))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1948, 172), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
# </editor-fold>

# <editor-fold desc="Statsheet tab - supports update functions">
def statsheet_support1_affinity_edit(self):
    affinity_type = statsheet_support_affinity_type1.get().capitalize()
    if affinity_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/support_affinity_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1636, 264), mask=statsheet_affinity_image)
    elif affinity_type in affinity_types:
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/' + affinity_type + '_affinity.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1636, 264), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support2_affinity_edit(self):
    affinity_type = statsheet_support_affinity_type2.get().capitalize()
    if affinity_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/support_affinity_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1636, 328), mask=statsheet_affinity_image)
    elif affinity_type in affinity_types:
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/' + affinity_type + '_affinity.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1636, 328), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support3_affinity_edit(self):
    affinity_type = statsheet_support_affinity_type3.get().capitalize()
    if affinity_type == 'None':
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/support_affinity_bg.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1636, 392), mask=statsheet_affinity_image)
    elif affinity_type in affinity_types:
        statsheet_affinity_image = Image.open('UI Resources/Statsheet tab UI/' + affinity_type + '_affinity.png')
        statsheet_tab_main_image.paste(statsheet_affinity_image, (1636, 392), mask=statsheet_affinity_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support1_name_edit(self):
    statsheet_str = statsheet_support1_name_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/support_name_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1728, 268), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1728 + word_x_coord, 268), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support2_name_edit(self):
    statsheet_str = statsheet_support2_name_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/support_name_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1728, 332), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1728 + word_x_coord, 332), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support3_name_edit(self):
    statsheet_str = statsheet_support3_name_input.get()
    statsheet_word_background = Image.open('UI Resources/Statsheet tab UI/support_name_bg.png')
    statsheet_tab_main_image.paste(statsheet_word_background, (1728, 396), mask=statsheet_word_background)
    word_x_coord = 0
    for letter in statsheet_str:
        if letter.isupper():
            letter_image = Image.open('UI Resources/Fonts/White font/upper_' + letter + '.png')
        elif letter.islower():
            letter_image = Image.open('UI Resources/Fonts/White font/lower_' + letter + '.png')
        else:
            if letter.isspace():
                letter = 'blank_space'
            letter_image = Image.open('UI Resources/Fonts/White font/' + letter + '.png')
        statsheet_tab_main_image.paste(letter_image, (1728 + word_x_coord, 396), mask=letter_image)
        word_x_coord += letter_image.size[0] - 4
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support1_rank_edit(self):
    support_rank = statsheet_support_rank1.get().capitalize()
    if support_rank == 'None':
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/support_rank_bg.png')
        statsheet_tab_main_image.paste(statsheet_rank_image, (1920, 268), mask=statsheet_rank_image)
    elif support_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/support_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + support_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1920, 268))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1920, 268), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support2_rank_edit(self):
    support_rank = statsheet_support_rank2.get().capitalize()
    if support_rank == 'None':
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/support_rank_bg.png')
        statsheet_tab_main_image.paste(statsheet_rank_image, (1920, 333), mask=statsheet_rank_image)
    elif support_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/support_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + support_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1920, 333))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1920, 333), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new

def statsheet_support3_rank_edit(self):
    support_rank = statsheet_support_rank3.get().capitalize()
    if support_rank == 'None':
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/support_rank_bg.png')
        statsheet_tab_main_image.paste(statsheet_rank_image, (1920, 400), mask=statsheet_rank_image)
    elif support_rank in rank_levels:
        statsheet_rank_background = Image.open('UI Resources/Statsheet tab UI/support_rank_bg.png')
        statsheet_rank_image = Image.open('UI Resources/Statsheet tab UI/rank_' + support_rank + '.png')
        statsheet_tab_main_image.paste(statsheet_rank_background, (1920, 400))
        statsheet_tab_main_image.paste(statsheet_rank_image, (1920, 400), mask=statsheet_rank_image)
    statsheet_tab_ui.paste(statsheet_tab_main_image.resize([1560, 480]), (216, 912))
    statsheet_tab_ui_new = ImageTk.PhotoImage(statsheet_tab_ui.resize([1000, 750]))
    statsheet_tab_ui_label.configure(image=statsheet_tab_ui_new)
    statsheet_tab_ui_label.image = statsheet_tab_ui_new
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

statsheet_portrait_name = StringVar()
statsheet_sprite_name = StringVar()
statsheet_portrait_name_input = Combobox(tab_statsheet, textvariable=statsheet_portrait_name, width=17, justify='center')
statsheet_sprite_name_input = Combobox(tab_statsheet, textvariable=statsheet_sprite_name, width=17, justify='center')
statsheet_portrait_name_input['values'] = [''] + ['-- HELLIONS --'] + portrait_names_hellions_no_ext + [''] + ['-- ALLIES --'] + portrait_names_allies_no_ext + [''] + ['-- FOES --'] + portrait_names_foes_no_ext + [''] + ['-- GENERIC --'] + portrait_names_generic_units_no_ext + [''] + ['-- MONSTERS --'] + portrait_names_monsters_no_ext
statsheet_sprite_name_input['values'] = [''] + ['-- HELLIONS --'] + sprite_names_hellions_no_ext + [''] + ['-- ALLIES --'] + sprite_names_allies_no_ext + [''] + ['-- FOES --'] + sprite_names_foes_no_ext
statsheet_portrait_name_input.bind('<<ComboboxSelected>>', statsheet_portrait_edit)
statsheet_portrait_name_input.bind('<KeyRelease>', statsheet_portrait_edit)
statsheet_sprite_name_input.bind('<<ComboboxSelected>>', statsheet_sprite_edit)
statsheet_sprite_name_input.bind('<KeyRelease>', statsheet_sprite_edit)
statsheet_portrait_name_input.place(x=330, y=48)
statsheet_sprite_name_input.place(x=330, y=80)

statsheet_custom_portrait_button = Button(tab_statsheet, text='Custom', command=statsheet_custom_portrait)
statsheet_custom_sprite_button = Button(tab_statsheet, text='Custom', command=statsheet_custom_sprite)
statsheet_custom_portrait_button.place(x=466, y=46)
statsheet_custom_sprite_button.place(x=466, y=78)

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

statsheet_MOV_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_CON_input = Entry(tab_statsheet, width=5, justify='center')
statsheet_unit_affinity_type = StringVar()
statsheet_unit_affinity_type.set('None')
statsheet_unit_affinity_input = Combobox(tab_statsheet, values=affinity_types, width=8, justify='center',
                                         textvariable=statsheet_unit_affinity_type)
statsheet_MOV_input.bind('<KeyRelease>', statsheet_mov_num_edit)
statsheet_CON_input.bind('<KeyRelease>', statsheet_con_num_edit)
statsheet_unit_affinity_input.bind('<<ComboboxSelected>>', statsheet_unit_affinity_edit)
statsheet_unit_affinity_input.bind('<KeyRelease>', statsheet_unit_affinity_edit)
statsheet_MOV_input.place(x=468, y=145)
statsheet_CON_input.place(x=468, y=177)
statsheet_unit_affinity_input.place(x=468, y=209)

statsheet_mount_type = StringVar
statsheet_mount_type_input = Combobox(tab_statsheet, values=['Horse', 'Pegasus', 'Wyvern', 'None'], width=2,
                                      justify='center', textvariable=statsheet_mount_type)
statsheet_mount_type_input.bind('<<ComboboxSelected>>', statsheet_mount_edit)
statsheet_mount_type_input.place(x=510, y=144)

statsheet_equipped_item = StringVar()
statsheet_equipped_item.set('#1')
statsheet_equipped_item_input = Combobox(tab_statsheet, values=['#1', '#2', '#3', '#4', '#5', 'None'], width=5,
                                         justify='center', textvariable=statsheet_equipped_item)
statsheet_equipped_item_input.bind('<<ComboboxSelected>>', statsheet_equipped_item_edit)
statsheet_equipped_item_input.bind('<KeyRelease>', statsheet_equipped_item_edit)
statsheet_equipped_item_input.place(x=696, y=49)

statsheet_equip1_name = StringVar()
statsheet_equip2_name = StringVar()
statsheet_equip3_name = StringVar()
statsheet_equip4_name = StringVar()
statsheet_equip5_name = StringVar()
statsheet_equip1_input = Combobox(tab_statsheet, values=equipment_list, width=13, justify='center',
                                  textvariable=statsheet_equip1_name)
statsheet_equip2_input = Combobox(tab_statsheet, values=equipment_list, width=13, justify='center',
                                  textvariable=statsheet_equip2_name)
statsheet_equip3_input = Combobox(tab_statsheet, values=equipment_list, width=13, justify='center',
                                  textvariable=statsheet_equip3_name)
statsheet_equip4_input = Combobox(tab_statsheet, values=equipment_list, width=13, justify='center',
                                  textvariable=statsheet_equip4_name)
statsheet_equip5_input = Combobox(tab_statsheet, values=equipment_list, width=13, justify='center',
                                  textvariable=statsheet_equip5_name)
statsheet_equip1_input.bind('<<ComboboxSelected>>', statsheet_equip1_edit)
statsheet_equip2_input.bind('<<ComboboxSelected>>', statsheet_equip2_edit)
statsheet_equip3_input.bind('<<ComboboxSelected>>', statsheet_equip3_edit)
statsheet_equip4_input.bind('<<ComboboxSelected>>', statsheet_equip4_edit)
statsheet_equip5_input.bind('<<ComboboxSelected>>', statsheet_equip5_edit)
statsheet_equip1_input.bind('<KeyRelease>', statsheet_equip1_edit)
statsheet_equip2_input.bind('<KeyRelease>', statsheet_equip2_edit)
statsheet_equip3_input.bind('<KeyRelease>', statsheet_equip3_edit)
statsheet_equip4_input.bind('<KeyRelease>', statsheet_equip4_edit)
statsheet_equip5_input.bind('<KeyRelease>', statsheet_equip5_edit)
statsheet_equip1_input.place(x=600, y=79)
statsheet_equip2_input.place(x=600, y=111)
statsheet_equip3_input.place(x=600, y=143)
statsheet_equip4_input.place(x=600, y=175)
statsheet_equip5_input.place(x=600, y=207)

statsheet_equip1_uses_input = Entry(tab_statsheet, width=6, justify='center')
statsheet_equip2_uses_input = Entry(tab_statsheet, width=6, justify='center')
statsheet_equip3_uses_input = Entry(tab_statsheet, width=6, justify='center')
statsheet_equip4_uses_input = Entry(tab_statsheet, width=6, justify='center')
statsheet_equip5_uses_input = Entry(tab_statsheet, width=6, justify='center')
statsheet_equip1_uses_input.bind('<KeyRelease>', statsheet_equip1_uses_edit)
statsheet_equip2_uses_input.bind('<KeyRelease>', statsheet_equip2_uses_edit)
statsheet_equip3_uses_input.bind('<KeyRelease>', statsheet_equip3_uses_edit)
statsheet_equip4_uses_input.bind('<KeyRelease>', statsheet_equip4_uses_edit)
statsheet_equip5_uses_input.bind('<KeyRelease>', statsheet_equip5_uses_edit)
statsheet_equip1_uses_input.place(x=714, y=80)
statsheet_equip2_uses_input.place(x=714, y=112)
statsheet_equip3_uses_input.place(x=714, y=144)
statsheet_equip4_uses_input.place(x=714, y=176)
statsheet_equip5_uses_input.place(x=714, y=208)

statsheet_weapon_attack_input = Entry(tab_statsheet, width=8, justify='center')
statsheet_weapon_critical_input = Entry(tab_statsheet, width=8, justify='center')
statsheet_weapon_accuracy_input = Entry(tab_statsheet, width=8, justify='center')
statsheet_weapon_avoid_input = Entry(tab_statsheet, width=8, justify='center')
statsheet_weapon_weight_input = Entry(tab_statsheet, width=8, justify='center')
statsheet_weapon_range_input = Entry(tab_statsheet, width=8, justify='center')
statsheet_weapon_attack_input.bind('<KeyRelease>', statsheet_weapon_attack_edit)
statsheet_weapon_critical_input.bind('<KeyRelease>', statsheet_weapon_critical_edit)
statsheet_weapon_accuracy_input.bind('<KeyRelease>', statsheet_weapon_accuracy_edit)
statsheet_weapon_avoid_input.bind('<KeyRelease>', statsheet_weapon_avoid_edit)
statsheet_weapon_weight_input.bind('<KeyRelease>', statsheet_weapon_weight_edit)
statsheet_weapon_range_input.bind('<KeyRelease>', statsheet_weapon_range_edit)
statsheet_weapon_attack_input.place(x=690, y=241)
statsheet_weapon_critical_input.place(x=690, y=273)
statsheet_weapon_accuracy_input.place(x=690, y=305)
statsheet_weapon_avoid_input.place(x=690, y=337)
statsheet_weapon_weight_input.place(x=690, y=369)
statsheet_weapon_range_input.place(x=690, y=401)

statsheet_proficiency_type1 = StringVar()
statsheet_proficiency_type1.set('Swords')
statsheet_proficiency_type2 = StringVar()
statsheet_proficiency_type2.set('Axes')
statsheet_proficiency_type3 = StringVar()
statsheet_proficiency_type3.set('Spears')
statsheet_proficiency_type4 = StringVar()
statsheet_proficiency_type4.set('Bows')
statsheet_proficiency_type1_input = Combobox(tab_statsheet, values=weapon_types, width=10, justify='center',
                                             textvariable=statsheet_proficiency_type1)
statsheet_proficiency_type2_input = Combobox(tab_statsheet, values=weapon_types, width=10, justify='center',
                                             textvariable=statsheet_proficiency_type2)
statsheet_proficiency_type3_input = Combobox(tab_statsheet, values=weapon_types, width=10, justify='center',
                                             textvariable=statsheet_proficiency_type3)
statsheet_proficiency_type4_input = Combobox(tab_statsheet, values=weapon_types, width=10, justify='center',
                                             textvariable=statsheet_proficiency_type4)
statsheet_proficiency_type1_input.bind('<<ComboboxSelected>>', statsheet_proficiency_type1_edit)
statsheet_proficiency_type2_input.bind('<<ComboboxSelected>>', statsheet_proficiency_type2_edit)
statsheet_proficiency_type3_input.bind('<<ComboboxSelected>>', statsheet_proficiency_type3_edit)
statsheet_proficiency_type4_input.bind('<<ComboboxSelected>>', statsheet_proficiency_type4_edit)
statsheet_proficiency_type1_input.bind('<KeyRelease>', statsheet_proficiency_type1_edit)
statsheet_proficiency_type2_input.bind('<KeyRelease>', statsheet_proficiency_type2_edit)
statsheet_proficiency_type3_input.bind('<KeyRelease>', statsheet_proficiency_type3_edit)
statsheet_proficiency_type4_input.bind('<KeyRelease>', statsheet_proficiency_type4_edit)
statsheet_proficiency_type1_input.place(x=816, y=80)
statsheet_proficiency_type2_input.place(x=816, y=112)
statsheet_proficiency_type3_input.place(x=816, y=144)
statsheet_proficiency_type4_input.place(x=816, y=176)

statsheet_proficiency_rank1 = StringVar()
statsheet_proficiency_rank2 = StringVar()
statsheet_proficiency_rank3 = StringVar()
statsheet_proficiency_rank4 = StringVar()
statsheet_proficiency_rank1_input = Combobox(tab_statsheet, values=rank_levels, width=5, justify='center',
                                             textvariable=statsheet_proficiency_rank1)
statsheet_proficiency_rank2_input = Combobox(tab_statsheet, values=rank_levels, width=5, justify='center',
                                             textvariable=statsheet_proficiency_rank2)
statsheet_proficiency_rank3_input = Combobox(tab_statsheet, values=rank_levels, width=5, justify='center',
                                             textvariable=statsheet_proficiency_rank3)
statsheet_proficiency_rank4_input = Combobox(tab_statsheet, values=rank_levels, width=5, justify='center',
                                             textvariable=statsheet_proficiency_rank4)
statsheet_proficiency_rank1_input.bind('<<ComboboxSelected>>', statsheet_proficiency_rank1_edit)
statsheet_proficiency_rank2_input.bind('<<ComboboxSelected>>', statsheet_proficiency_rank2_edit)
statsheet_proficiency_rank3_input.bind('<<ComboboxSelected>>', statsheet_proficiency_rank3_edit)
statsheet_proficiency_rank4_input.bind('<<ComboboxSelected>>', statsheet_proficiency_rank4_edit)
statsheet_proficiency_rank1_input.bind('<KeyRelease>', statsheet_proficiency_rank1_edit)
statsheet_proficiency_rank2_input.bind('<KeyRelease>', statsheet_proficiency_rank2_edit)
statsheet_proficiency_rank3_input.bind('<KeyRelease>', statsheet_proficiency_rank3_edit)
statsheet_proficiency_rank4_input.bind('<KeyRelease>', statsheet_proficiency_rank4_edit)
statsheet_proficiency_rank1_input.place(x=910, y=80)
statsheet_proficiency_rank2_input.place(x=910, y=112)
statsheet_proficiency_rank3_input.place(x=910, y=144)
statsheet_proficiency_rank4_input.place(x=910, y=176)

statsheet_support_affinity_type1 = StringVar()
statsheet_support_affinity_type2 = StringVar()
statsheet_support_affinity_type3 = StringVar()
statsheet_support1_affinity_input = Combobox(tab_statsheet, values=affinity_types, width=3, justify='center',
                                             textvariable=statsheet_support_affinity_type1)
statsheet_support2_affinity_input = Combobox(tab_statsheet, values=affinity_types, width=3, justify='center',
                                             textvariable=statsheet_support_affinity_type2)
statsheet_support3_affinity_input = Combobox(tab_statsheet, values=affinity_types, width=3, justify='center',
                                             textvariable=statsheet_support_affinity_type3)
statsheet_support1_affinity_input.bind('<<ComboboxSelected>>', statsheet_support1_affinity_edit)
statsheet_support2_affinity_input.bind('<<ComboboxSelected>>', statsheet_support2_affinity_edit)
statsheet_support3_affinity_input.bind('<<ComboboxSelected>>', statsheet_support3_affinity_edit)
statsheet_support1_affinity_input.bind('<KeyRelease>', statsheet_support1_affinity_edit)
statsheet_support2_affinity_input.bind('<KeyRelease>', statsheet_support2_affinity_edit)
statsheet_support3_affinity_input.bind('<KeyRelease>', statsheet_support3_affinity_edit)
statsheet_support1_affinity_input.place(x=810, y=272)
statsheet_support2_affinity_input.place(x=810, y=304)
statsheet_support3_affinity_input.place(x=810, y=336)

statsheet_support1_name_input = Entry(tab_statsheet, width=10, justify='center')
statsheet_support2_name_input = Entry(tab_statsheet, width=10, justify='center')
statsheet_support3_name_input = Entry(tab_statsheet, width=10, justify='center')
statsheet_support1_name_input.bind('<KeyRelease>', statsheet_support1_name_edit)
statsheet_support2_name_input.bind('<KeyRelease>', statsheet_support2_name_edit)
statsheet_support3_name_input.bind('<KeyRelease>', statsheet_support3_name_edit)
statsheet_support1_name_input.place(x=860, y=273)
statsheet_support2_name_input.place(x=860, y=305)
statsheet_support3_name_input.place(x=860, y=337)

statsheet_support_rank1 = StringVar()
statsheet_support_rank2 = StringVar()
statsheet_support_rank3 = StringVar()
statsheet_support1_rank_input = Combobox(tab_statsheet, values=rank_levels, width=2, justify='center',
                                         textvariable=statsheet_support_rank1)
statsheet_support2_rank_input = Combobox(tab_statsheet, values=rank_levels, width=2, justify='center',
                                         textvariable=statsheet_support_rank2)
statsheet_support3_rank_input = Combobox(tab_statsheet, values=rank_levels, width=2, justify='center',
                                         textvariable=statsheet_support_rank3)
statsheet_support1_rank_input.bind('<<ComboboxSelected>>', statsheet_support1_rank_edit)
statsheet_support1_rank_input.bind('<KeyRelease>', statsheet_support1_rank_edit)
statsheet_support2_rank_input.bind('<<ComboboxSelected>>', statsheet_support2_rank_edit)
statsheet_support2_rank_input.bind('<KeyRelease>', statsheet_support2_rank_edit)
statsheet_support3_rank_input.bind('<<ComboboxSelected>>', statsheet_support3_rank_edit)
statsheet_support3_rank_input.bind('<KeyRelease>', statsheet_support3_rank_edit)
statsheet_support1_rank_input.place(x=932, y=272)
statsheet_support2_rank_input.place(x=932, y=304)
statsheet_support3_rank_input.place(x=932, y=336)
# </editor-fold>

window.mainloop()