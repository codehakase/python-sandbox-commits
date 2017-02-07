# Function to convert different units of temperature
# K -> C
# F -> C
# R -> C

def tempConv(t, unit):
    return {
        "K->C": t - 273.15,
        "F->C": (t - 32) / 1.8,
        "R->C": (t - 491.67) * (5 / 9.0)
    }[unit]


print tempConv(200, 'F->C')
