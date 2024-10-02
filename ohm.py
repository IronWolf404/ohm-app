import os
import json
from customtkinter import*
from ohm_functions import*
from tkinter import messagebox
from PIL import Image

ohm = CTk()
# size of app window:
ohm.geometry('600x350')

# Determine the base path for images
if getattr(sys, 'frozen', False):
    # If the application is run as a bundled executable
    base_path = sys._MEIPASS  # PyInstaller specific
else:
    # If the application is run as a script
    base_path = os.path.dirname(os.path.abspath(__file__))


# Set up the icon and image paths
icon_path = os.path.join(base_path, "images", "ohm.ico")
mode_image_paths = {
    'light': [
        os.path.join(base_path, "images", "mode-2.png"),
        os.path.join(base_path, "images", "color-2.png"),
        os.path.join(base_path, "images", "hover-2.png"),
        os.path.join(base_path, "images", "font-2.png"),
    ],
    'dark': [
        os.path.join(base_path, "images", "mode-1.png"),
        os.path.join(base_path, "images", "color-1.png"),
        os.path.join(base_path, "images", "hover-1.png"),
        os.path.join(base_path, "images", "font-1.png"),
    ]
}


# title bar:
ohm.title('ohm')
ohm.iconbitmap(icon_path)
ohm.resizable(False, False)

# tabs:
tab_frame = CTkFrame(master=ohm)
tab_frame.pack(side="top", padx=20, pady=20)

tabview = CTkTabview(master=tab_frame, width=600, height=350)
tabview.pack()

tab1 = tabview.add('color to ohm')
tab2 = tabview.add('ohm to color')
tab3 = tabview.add('setting')



#------------------------------------------------------(in tab1)------------------------------------------------------#
# RadioButton:
band4_var = IntVar(value=0)
band5_var = IntVar(value=1)
band6_var = IntVar(value=2)

def clear_widgets():
    # Hide or destroy all the labels and comboboxes
    label_1.place_forget()
    label_2.place_forget()
    label_3.place_forget()
    label_4.place_forget()
    label_5.place_forget()
    label_6.place_forget()

    combobox_band1.place_forget()
    combobox_band2.place_forget()
    combobox_band3.place_forget()
    combobox_Multiplier.place_forget()
    combobox_Tolerance.place_forget()
    combobox_PPM.place_forget()

    # If you have buttons or frames, clear them as well
    calculate_b4.place_forget()
    calculate_b5.place_forget()
    calculate_b6.place_forget()
    fram_resalt.place_forget()  # Adjust if needed

def band_check(select):
    clear_widgets()  # Clear previous widgets
    if select == 'band4':
        band5_var.set(1)
        band6_var.set(1)
        place(label_1, 0.38, 0.08, 'center')
        place(label_2, 0.72, 0.08, 'center')
        place(label_4, 0.342, 0.32, 'center')
        place(label_5, 0.68, 0.32, 'center')

        place(combobox_band1, 0.41, 0.175, 'center')
        place(combobox_band2, 0.75, 0.175, 'center')
        place(combobox_Multiplier, 0.41, 0.42, 'center')
        place(combobox_Tolerance, 0.75, 0.42, 'center')

        place(calculate_b4, 0.05, 0.775, 'w')

        place(fram_resalt, 0.58, 0.675, 'center')
        resalt.pack(anchor='s', expand=True, pady=10, padx=30)
        
    elif select == 'band5':
        band4_var.set(1)
        band6_var.set(1)
        place(label_1, 0.38, 0.08, 'center')
        place(label_2, 0.72, 0.08, 'center')
        place(label_3, 0.38, 0.32, 'center')
        place(label_4, 0.68, 0.32, 'center')
        place(label_5, 0.58, 0.56, 'center')

        place(combobox_band1, 0.41, 0.175, 'center')
        place(combobox_band2, 0.75, 0.175, 'center')
        place(combobox_band3, 0.41, 0.42, 'center')
        place(combobox_Multiplier, 0.75, 0.42, 'center')
        place(combobox_Tolerance, 0.58, 0.66, 'center')

        place(calculate_b5, 0.05, 0.775, 'w')

        place(fram_resalt, 0.58, 0.875, 'center')
        resalt.pack(anchor='s', expand=True, pady=10, padx=30)
        
    else:
        band4_var.set(1)
        band5_var.set(1)
        place(label_1, 0.38, 0.08, 'center')
        place(label_2, 0.72, 0.08, 'center')
        place(label_3, 0.38, 0.32, 'center')
        place(label_4, 0.68, 0.32, 'center')
        place(label_5, 0.345, 0.56, 'center')
        place(label_6, 0.655, 0.56, 'center')

        place(combobox_band1, 0.41, 0.175, 'center')
        place(combobox_band2, 0.75, 0.175, 'center')
        place(combobox_band3, 0.41, 0.42, 'center')
        place(combobox_Multiplier, 0.75, 0.42, 'center')
        place(combobox_Tolerance, 0.41, 0.66, 'center')
        place(combobox_PPM, 0.75, 0.66, 'center')

        place(calculate_b6, 0.05, 0.775, 'w')

        place(fram_resalt, 0.58, 0.875, 'center')
        resalt.pack(anchor='s', expand=True, pady=10, padx=30)


def calculat(selc):
    if selc == 'band4':
        selected_b1 = combobox_band1.get()
        selected_b2 = combobox_band2.get()
        selected_m = combobox_Multiplier.get()
        selected_t = combobox_Tolerance.get()
        sb1 = color_band.get(selected_b1, 0)
        sb2 = color_band.get(selected_b2, 0)
        sm = multiplier.get(selected_m, 0)
        st = tolerance.get(selected_t, 0)
        box.append([sb1, sb2 , sm , st])
            
        result = int(str(box[0][0]) + str(box[0][1])) * (box[0][2])
        K = result / 1000
        M = result / 1000000
        G = result / 1000000000

        if result < 1000:
            txt = f'{result}Ω ' + box[0][3]
        elif result < 1000000:
            txt = f'{K}kΩ ' + box[0][3]
        elif result < 1000000000:
            txt = f'{M}MΩ ' + box[0][3]
        else:
            txt = f'{G}GΩ ' + box[0][3]

        box.clear()
        resalt.configure(text=txt)

    elif selc == 'band5':
        selected_b1 = combobox_band1.get()
        selected_b2 = combobox_band2.get()
        selected_b3 = combobox_band3.get()
        selected_m = combobox_Multiplier.get()
        selected_t = combobox_Tolerance.get()
        sb1 = color_band.get(selected_b1, 0)
        sb2 = color_band.get(selected_b2, 0)
        sb3 = color_band.get(selected_b3, 0)
        sm = multiplier.get(selected_m, 0)
        st = tolerance.get(selected_t, 0)
        box.append([sb1, sb2, sb3, sm, st])
            
        result = int(str(box[0][0]) + str(box[0][1]) + str(box[0][2])) * (box[0][3])
        K = result / 1000
        M = result / 1000000
        G = result / 1000000000

        if result < 1000:
            txt = f'{result}Ω ' + box[0][4]
        elif result < 1000000:
            txt = f'{K}kΩ ' + box[0][4]
        elif result < 1000000000:
            txt = f'{M}MΩ ' + box[0][4]
        else:
            txt = f'{G}GΩ ' + box[0][4]

        box.clear()
        resalt.configure(text=txt)

    else:
        selected_b1 = combobox_band1.get()
        selected_b2 = combobox_band2.get()
        selected_b3 = combobox_band3.get()
        selected_m = combobox_Multiplier.get()
        selected_t = combobox_Tolerance.get()
        selected_p = combobox_PPM.get()
        sb1 = color_band.get(selected_b1, 0)
        sb2 = color_band.get(selected_b2, 0)
        sb3 = color_band.get(selected_b3, 0)
        sm = multiplier.get(selected_m, 0)
        st = tolerance.get(selected_t, 0)
        sp = ppm.get(selected_p, 0)
        box.append([sb1, sb2, sb3, sm, st, sp])
        
        result = int(str(box[0][0]) + str(box[0][1]) + str(box[0][2])) * (box[0][3])
        K = result / 1000
        M = result / 1000000
        G = result / 1000000000

        if result < 1000:
            txt = f'{result}Ω {box[0][4]} {box[0][5]}'
        elif result < 1000000:
            txt = f'{K}kΩ {box[0][4]} {box[0][5]}'
        elif result < 1000000000:
            txt = f'{M}MΩ {box[0][4]} {box[0][5]}'
        else:
            txt = f'{G}GΩ {box[0][4]} {box[0][5]}'

        box.clear()
        resalt.configure(text=txt)


band4 = CTkRadioButton(master=tab1, text='4 Band', variable=band4_var, command=lambda: band_check('band4'))
band5 = CTkRadioButton(master=tab1, text='5 Band', variable=band5_var, command=lambda: band_check('band5'))
band6 = CTkRadioButton(master=tab1, text='6 Band', variable=band6_var, command=lambda: band_check('band6'))

place(band4, 0.05, 0.17, 'w')
place(band5, 0.05, 0.3, 'w')
place(band6, 0.05, 0.425, 'w')

label_1 = CTkLabel(master=tab1, text='1st Band of Color')
label_2 = CTkLabel(master=tab1, text='2nd Band of Color')
label_3 = CTkLabel(master=tab1, text='3rd Band of Color')
label_4 = CTkLabel(master=tab1, text='Multiplier')
label_5 = CTkLabel(master=tab1, text='Tolerance')
label_6 = CTkLabel(master=tab1, text='PPM')

box = []

combobox_band1 = CTkComboBox(master=tab1, values=list(color_band.keys()))
combobox_band2 = CTkComboBox(master=tab1, values=list(color_band.keys()))
combobox_band3 = CTkComboBox(master=tab1, values=list(color_band.keys()))
combobox_Multiplier = CTkComboBox(master=tab1, values=list(multiplier.keys()))
combobox_Tolerance = CTkComboBox(master=tab1, values=list(tolerance.keys()))
combobox_PPM = CTkComboBox(master=tab1, values=list(ppm.keys()))

size = CTkFont(size=60)
calculate_b4 = CTkButton(master=tab1, text='Ω', font=size, width=60, height=50, corner_radius=20, command=lambda: calculat('band4'))
calculate_b5 = CTkButton(master=tab1, text='Ω', font=size, width=60, height=50, corner_radius=20, command=lambda: calculat('band5'))
calculate_b6 = CTkButton(master=tab1, text='Ω', font=size, width=60, height=50, corner_radius=20, command=lambda: calculat('band6'))

# result:
fram_resalt = CTkFrame(master=tab1)
resalt = CTkLabel(master=fram_resalt, text='result', font=('Consolas', 15))

# the defult chek
band_check('band4')



#------------------------------------------------------(in tab2)------------------------------------------------------#
# RadioButton:
band4_varab = IntVar(value=0)
band5_varab = IntVar(value=1)


def clear_item():
    btn_1.place_forget()
    btn_2.place_forget()

def selected(select):
    clear_item()
    if select == 'band4-oc':
        band5_varab.set(1)
        place(btn_1, 0.5, 0.55, 'center')
        place(resalt_Foc, 0.5, 0.8, 'center')
        resalt_oc.pack(anchor='s', expand=True, pady=10, padx=30)
    else:
        band4_varab.set(1)
        place(btn_2, 0.5, 0.55, 'center')
        place(resalt_Foc, 0.5, 0.8, 'center')
        resalt_oc.pack(anchor='s', expand=True, pady=10, padx=30)


def band_4():
    l.clear()
    try:
        input = float(enter.get())  # Attempt to convert input to float
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")  # Show error message
        return  # Exit the function if there's an error

    input = float(enter.get())
    selected_type = box_bands.get()  # Get the selected ohm type
    multip = type.get(selected_type, 0)

    if input < 1.0 and selected_type == 'Ω':
        result = input / 0.01
        l.append(result)

        first_digit = int(str(int(l[0]))[0])
        second_digit = int(str(int(l[0]))[1])
        toler = tolerance_2.get(box_tolrn.get(), 0)

        color1 = band[first_digit]
        color2 = band[second_digit]
        color3 = 'Silver'
        color4 = toler

        res = f'{color1} - {color2} - {color3} - {color4}'
        resalt_oc.configure(text=res)

    elif input<10 and input>=1.0 and selected_type == 'Ω':
        result = input / 0.1
        l.append(result)

        first_digit = int(str(int(l[0]))[0])
        second_digit = int(str(int(l[0]))[1])
        toler = tolerance_2.get(box_tolrn.get(), 0)

        color1 = band[first_digit]
        color2 = band[second_digit]
        color3 = 'Gold'
        color4 = toler

        res = f'{color1} - {color2} - {color3} - {color4}'
        resalt_oc.configure(text=res)
    
    else:
        result = input * multip
        l.append(result)

        first_digit = int(str(int(l[0]))[0])
        second_digit = int(str(int(l[0]))[1])
        multiplier = len(str(int(l[0]))[2:])
        toler = tolerance_2.get(box_tolrn.get(), 0)

        color1 = band[first_digit]
        color2 = band[second_digit]
        color3 = band[multiplier]
        color4 = toler

        res = f'{color1} - {color2} - {color3} - {color4}'
        resalt_oc.configure(text=res)


def band_5():
    l.clear()
    try:
        input = float(enter.get())  # Attempt to convert input to float
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")  # Show error message
        return  # Exit the function if there's an error

    input = float(enter.get())
    selected_type = box_bands.get()  # Get the selected ohm type
    multip = type.get(selected_type, 0)

    if input < 1.0 and selected_type == 'Ω':
        result = input / 0.01
        l.append(result)

        first_digit = int(str(int(l[0]))[0])
        second_digit = int(str(int(l[0]))[1])
        third_digit = int(str(int(l[0]))[2])
        toler = tolerance_2.get(box_tolrn.get(), 0)

        color1 = band[first_digit]
        color2 = band[second_digit]
        color3 = band[third_digit]
        color4 = 'Silver'
        color5 = toler

        res = f'{color1} - {color2} - {color3} - {color4} - {color5}'
        resalt_oc.configure(text=res)

    elif input<10 and input>=1.0 and selected_type == 'Ω':
        result = input / 0.1
        l.append(result)

        first_digit = int(str(int(l[0]))[0])
        second_digit = int(str(int(l[0]))[1])
        third_digit = int(str(int(l[0]))[2])
        toler = tolerance_2.get(box_tolrn.get(), 0)

        color1 = band[first_digit]
        color2 = band[second_digit]
        color3 = band[third_digit]
        color4 = 'Gold'
        color5 = toler

        res = f'{color1} - {color2} - {color3} - {color4} - {color5}'
        resalt_oc.configure(text=res)
    
    else:
        result = input * multip
        l.append(result)

        first_digit = int(str(int(l[0]))[0])
        second_digit = int(str(int(l[0]))[1])
        third_digit = int(str(int(l[0]))[2])
        multiplier = len(str(int(l[0]))[3:])
        toler = tolerance_2.get(box_tolrn.get(), 0)

        color1 = band[first_digit]
        color2 = band[second_digit]
        color3 = band[third_digit]
        color4 = band[multiplier]
        color5 = toler

        res = f'{color1} - {color2} - {color3} - {color4} - {color5}'
        resalt_oc.configure(text=res)

l = []

band4_oc = CTkRadioButton(master=tab2, text='4 Band', variable=band4_varab, command=lambda: selected('band4-oc'))
band5_oc = CTkRadioButton(master=tab2, text='5 Band', variable=band5_varab, command=lambda: selected('band5-oc'))
place(band4_oc, 0.4, 0.1, 'center')
place(band5_oc, 0.7, 0.1, 'center')

enter = CTkEntry(master=tab2, placeholder_text='Enter value...')
place(enter, 0.35, 0.3, 'center')

box_bands = CTkComboBox(master=tab2, values=list(type), width=60)
box_tolrn = CTkComboBox(master=tab2, values=list(tolerance_2), width=80)
place(box_bands, 0.54, 0.3, 'center')
place(box_tolrn, 0.675, 0.3, 'center')

bold = CTkFont(family="DIN", size=20, weight="bold")
btn_1 = CTkButton(master=tab2, text='calculate', font=bold, width=80, height=50, corner_radius=25, command=lambda: band_4())
btn_2 = CTkButton(master=tab2, text='calculate', font=bold, width=80, height=50, corner_radius=25, command=lambda: band_5())

# result:
resalt_Foc = CTkFrame(master=tab2)
resalt_oc = CTkLabel(master=resalt_Foc, text='band color', font=('Consolas', 15))

# the defult chek
selected('band4-oc')



#------------------------------------------------------(in tab3)------------------------------------------------------#w
def mode():
    if switch_mode.get():
        set_appearance_mode('light')
        col_mode = '#333333'
        col_box = '#EBEBEB'
        col_tab = '#A3A3A3'
        col_bord = col_b
        color_result = '#E0E0E0'
        color = '#E0E0E0'
        img1 = CTkImage(Image.open(mode_image_paths['light'][0]), size=(30, 30))
        img2 = CTkImage(Image.open(mode_image_paths['light'][1]), size=(30, 30))
        img3 = CTkImage(Image.open(mode_image_paths['light'][2]), size=(30, 30))
        img4 = CTkImage(Image.open(mode_image_paths['light'][3]), size=(30, 30))
        save_mode_setting("light")
    else:
        set_appearance_mode('dark')
        col_mode = '#D5D9DE'
        col_box = '#343638'
        col_tab = '#343638'
        col_bord = '#333333'
        color_result = '#474747'
        color = '#474747'
        img1 = CTkImage(Image.open(mode_image_paths['dark'][0]), size=(30, 30))
        img2 = CTkImage(Image.open(mode_image_paths['dark'][1]), size=(30, 30))
        img3 = CTkImage(Image.open(mode_image_paths['dark'][2]), size=(30, 30))
        img4 = CTkImage(Image.open(mode_image_paths['dark'][3]), size=(30, 30))
        save_mode_setting("dark")
    
    # Update the frame colors
    fram_resalt.configure(fg_color=color_result)
    resalt_Foc.configure(fg_color=color_result)
    fram_mode.configure(fg_color=color)
    fram_color_btn.configure(fg_color=color)
    fram_color_hover.configure(fg_color=color)
    fram_color_text.configure(fg_color=color)
    img_mode.configure(image=img1)
    img_color_btn.configure(image=img2)
    img_color_hover.configure(image=img3)
    img_color_text.configure(image=img4)
    switch_mode.configure(button_color=col_mode, button_hover_color=col_mode, border_color=col_bord)
    combobox_band1.configure(fg_color=col_box)
    combobox_band2.configure(fg_color=col_box)
    combobox_band3.configure(fg_color=col_box)
    combobox_Multiplier.configure(fg_color=col_box)
    combobox_Tolerance.configure(fg_color=col_box)
    combobox_PPM.configure(fg_color=col_box)
    box_bands.configure(fg_color=col_box)
    box_tolrn.configure(fg_color=col_box)
    box_color_btn.configure(fg_color=col_box)
    box_color_hbtn.configure(fg_color=col_box)
    box_color_tbtn.configure(fg_color=col_box)
    enter.configure(fg_color=col_box)
    tabview.configure(segmented_button_unselected_color=col_tab, segmented_button_unselected_hover_color=col_tab)

# Function to save mode setting
def save_mode_setting(mode):
    settings = load_settings()
    settings["mode"] = mode
    save_settings(settings['button_color'], settings['hover_color'], settings['text_color'], mode)

# Define the path for settings.json in the user's home directory
settings_file_path = os.path.join(os.path.expanduser("~"), "settings.json")

# Function to load saved settings from a JSON file
def load_settings():
    if not os.path.exists(settings_file_path):
        # Create default settings if file does not exist
        default_settings = {
            'button_color': '#1F538D',
            'hover_color': '#013E75',
            'text_color': 'white',
            'mode': 'dark'
        }
        with open(settings_file_path, "w") as file:
            json.dump(default_settings, file)
        return default_settings
    
    try:
        with open(settings_file_path, "r") as file:
            settings = json.load(file)
            return settings
    except PermissionError:
        print("Permission denied: Unable to read settings.json. Please check your file permissions.")
        return {'button_color': 'Deep Sky Blue', 'hover_color': 'Dark Blue', 'text_color': 'white', 'mode': 'dark'}

# Function to save settings to a JSON file
def save_settings(button_color, hover_color, text_color, mode_setting):
    try:
        with open(settings_file_path, "w") as file:
            json.dump({
                'button_color': button_color,
                'hover_color': hover_color,
                'text_color': text_color,
                'mode': mode_setting
            }, file)
    except PermissionError:
        print("Permission denied: Unable to write to settings.json. Please check your file permissions.")

# Load the saved settings when the app starts
saved_settings = load_settings()
col_b = saved_settings.get('button_color', 'Deep Sky Blue')
col_h = saved_settings.get('hover_color', 'Dark Blue')
col_t = saved_settings.get('text_color', 'white')
current_mode = saved_settings.get('mode', 'dark')

# Function to update the button's colors
def update_button():
    calculate_b4.configure(fg_color=col_b, hover_color=col_h, text_color=col_t)
    calculate_b5.configure(fg_color=col_b, hover_color=col_h, text_color=col_t)
    calculate_b6.configure(fg_color=col_b, hover_color=col_h, text_color=col_t)
    btn_1.configure(fg_color=col_b, hover_color=col_h, text_color=col_t)
    btn_2.configure(fg_color=col_b, hover_color=col_h, text_color=col_t)
    band4.configure(fg_color=col_b, hover_color=col_h)
    band5.configure(fg_color=col_b, hover_color=col_h)
    band6.configure(fg_color=col_b, hover_color=col_h)
    band4_oc.configure(fg_color=col_b, hover_color=col_h)
    band5_oc.configure(fg_color=col_b, hover_color=col_h)
    tabview.configure(segmented_button_selected_color=col_b, segmented_button_selected_hover_color=col_b, segmented_button_fg_color=col_b)
    switch_mode.configure(progress_color=col_b)
    enter.configure(border_color=col_b)
    combobox_band1.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    combobox_band2.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    combobox_band3.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    combobox_Multiplier.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    combobox_Tolerance.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    combobox_PPM.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    box_bands.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    box_tolrn.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    box_color_btn.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    box_color_hbtn.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)
    box_color_tbtn.configure(button_color=col_b, button_hover_color=col_h, border_color=col_b)

# Function for ComboBox to change the button color
def change_button_color(selected_color):
    global col_b
    col_b = col_btn.get(selected_color, 0)
    update_button()
    save_settings(col_b, col_h, col_t, current_mode)

# Function for ComboBox to change the button hover (clicked) color
def change_hover_color(selected_color):
    global col_h
    col_h = col_hbtn.get(selected_color, 0)
    update_button()
    save_settings(col_b, col_h, col_t, current_mode)

# Function for ComboBox to change the button text color
def change_text_color(selected_color):
    global col_t
    col_t = col_tbtn.get(selected_color, 0)
    update_button()
    save_settings(col_b, col_h, col_t, current_mode)

# Setup your app frames and widgets
w = 520
h = 50

fram_mode = CTkFrame(master=tab3, width=w, height=h)
fram_color_btn = CTkFrame(master=tab3, width=w, height=h)
fram_color_hover = CTkFrame(master=tab3, width=w, height=h)
fram_color_text = CTkFrame(master=tab3, width=w, height=h)
fram_mode.pack(pady=5)
fram_color_btn.pack(pady=5)
fram_color_hover.pack(pady=5)
fram_color_text.pack(pady=5)

# Create labels with images
img_mode = CTkLabel(fram_mode, text=None)
img_color_btn = CTkLabel(fram_color_btn, text=None)
img_color_hover = CTkLabel(fram_color_hover, text=None)
img_color_text = CTkLabel(fram_color_text, text=None)
img_mode.place(relx=0.075, rely=0.5, anchor='w')
img_color_btn.place(relx=0.075, rely=0.5, anchor='w')
img_color_hover.place(relx=0.075, rely=0.5, anchor='w')
img_color_text.place(relx=0.075, rely=0.5, anchor='w')

box_color_btn = CTkComboBox(master=fram_color_btn, values=list(col_btn), command=change_button_color)
box_color_hbtn = CTkComboBox(master=fram_color_hover, values=list(col_hbtn), command=change_hover_color)
box_color_tbtn = CTkComboBox(master=fram_color_text, values=list(col_tbtn), command=change_text_color)
box_color_btn.place(relx=0.945, rely=0.5, anchor='e')
box_color_hbtn.place(relx=0.945, rely=0.5, anchor='e')
box_color_tbtn.place(relx=0.945, rely=0.5, anchor='e')
box_color_btn.set('Deep Sky Blue')
box_color_hbtn.set('Dark Blue')
box_color_tbtn.set('white')

bold_font = CTkFont(family="Helvetica", size=15, weight="bold")

label_mode = CTkLabel(fram_mode, text='App mode', font=bold_font)
label_col = CTkLabel(fram_color_btn, text='Button color', font=bold_font)
label_hcol = CTkLabel(fram_color_hover, text='Button hover color', font=bold_font)
label_tcol = CTkLabel(fram_color_text, text='Button text color', font=bold_font)
label_mode.place(relx=0.23, rely=0.5, anchor='center')
label_col.place(relx=0.25, rely=0.5, anchor='center')
label_hcol.place(relx=0.29, rely=0.5, anchor='center')
label_tcol.place(relx=0.275, rely=0.5, anchor='center')

# Define switch_mode and configure it
switch_mode = CTkSwitch(fram_mode, text='light', fg_color='#333333')
switch_mode.place(relx=0.9, rely=0.5, anchor='center')
switch_mode.configure(command=mode)

# Restore the saved mode after switch_mode has been created
if current_mode == 'light':
    switch_mode.select()
else:
    switch_mode.deselect()


# Initial load of the saved mode and colors
mode()
update_button()

ohm.mainloop()