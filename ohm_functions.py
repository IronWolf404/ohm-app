# functions:
def place(Name, X, Y, postion):
    Name.place(relx=X, rely=Y, anchor=postion)

def place_nunpos(Name, X, Y):
    Name.place(relx=X, rely=Y)

# listes:
color_band = {
              'Black': 0,
              'Brown': 1,
              'Red': 2,
              'Orange': 3,
              'Yellow': 4,
              'Green': 5,
              'Blue': 6,
              'violet': 7,
              'Grey': 8,
              'White': 9
}

multiplier={
            'Black': 1,
            'Brown': 10,
            'Red': 100,
            'Orange': 1000,
            'Yellow': 10000,
            'Green': 100000,
            'Blue': 1000000,
            'violet': 10000000,
            'Grey': 100000000,
            'White': 1000000000,
            'Gold': 0.1,
            'Silver': 0.01
}

tolerance={
            'Brown': '±1%',
            'Red': '±2%',
            'Green': '±0.5%',
            'Blue': '±0.25%',
            'violet': '±0.10%',
            'Grey': '±0.05%',
            'Gold': '±5%',
            'Silver': '±10%',
            'no color': '±20%'
}

ppm = {
       'Brown': '100ppm',
       'Red': '50ppm',
       'Orange': '15ppm',
       'Yellow': '25ppm',
       'Blue': '10ppm',
       'violet': '5ppm',
       'White': '1ppm'
}

type = {
    'Ω': 1,
    'k' : 1000,
    'M' : 1000000,
    'G' : 1000000000
}

band = {
    0: 'Black',
    1: 'Brown',
    2: 'Red',
    3: 'Orange',
    4: 'Yellow',
    5: 'Green',
    6: 'Blue',
    7: 'violet',
    8: 'Grey',
    9: 'White'
}

tolerance_2 = {
    '±1%': 'Brown',
    '±2%': 'Red',
    '±0.5%': 'Green',
    '±0.25%': 'Blue',
    '±0.10%': 'violet',
    '±0.05%': 'Grey',
    '±5%': 'Gold',
    '±10%': 'Silver',
    '±20%': 'no color'
}

col_btn = {
    'Deep Sky Blue': '#1F538D',
    'Dark Red': '#8D1F21',
    'Forest Green': '#238D1F',
    'Bright Yellow': '#C9A824',
    'Teal': '#1F808D',
    'Purple': '#771F8D',
    'Dark Magenta': '#8D1F61'
}

col_hbtn = {
    'Dark Blue': '#013E75',
    'Dark Red': '#750110',
    'Dark Green': '#0B7501',
    'Dark Gold': '#A3821E',
    'Dark Teal': '#017175',
    'Dark Purple': '#500175',
    'Dark Magenta': '#75015C'
}

col_tbtn = {
    'white': 'white',
    'black': 'black',
}