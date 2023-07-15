var1 = "Hello"
ext_var1 = "Hello," + "long sentence"

name = "Subhajit"
ttle = "Chaudhuri"

intpr = f"Hello1 {name} {ttle}"

# var_frmt = "Hello2 {} {}"
# frmtd = var_frmt.format(name, ttle)
var_frmt = "Hello2 {}"
frmtd = var_frmt.format(name)

# print(intpr)
# print(frmtd)
print(frmtd.upper())
print(frmtd.lower())
print(frmtd.replace("Subha", "Biswa"))
