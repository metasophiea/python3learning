import matplotlib, numpy
import matplotlib.pyplot

# -- Styling
# there is an option to style the drawn graph with a two (ish) character string. Below is a listing 
# of all the possible styling commands
# =============================================
# character       description
# =============================================
# '-'             solid line style
# '--'            dashed line style
# '-.'            dash-dot line style
# ':'             dotted line style
# '.'             point marker
# ','             pixel marker
# 'o'             circle marker
# 'v'             triangle_down marker
# '^'             triangle_up marker
# '<'             triangle_left marker
# '>'             triangle_right marker
# '1'             tri_down marker
# '2'             tri_up marker
# '3'             tri_left marker
# '4'             tri_right marker
# 's'             square marker
# 'p'             pentagon marker
# '*'             star marker
# 'h'             hexagon1 marker
# 'H'             hexagon2 marker
# '+'             plus marker
# 'x'             x marker
# 'D'             diamond marker
# 'd'             thin_diamond marker
# '|'             vline marker
# '_'             hline marker
# ===============================================
#
# ==================
# character   color
# ==================
# 'b'         blue
# 'g'         green
# 'r'         red
# 'c'         cyan
# 'm'         magenta
# 'y'         yellow
# 'k'         black
# 'w'         white
# ==================

# clear entire plot
matplotlib.pyplot.clf()

# multiple plotting with a single command
matplotlib.pyplot.plot(
# graphing as a red dashed line
    [0, 1, 1.75, 3],
    [1, 20, 8, 23],
    "--r",
# repeated graphing with the same data but differnet styling
    [0, 1, 1.75, 3],
    [1, 20, 8, 23],
    "oy"
)

# graphing as descrete dots of blue
matplotlib.pyplot.plot(
    [1, -4.5, 16, 23],
    "ob"
)

matplotlib.pyplot.show()