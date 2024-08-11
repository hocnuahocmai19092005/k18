point = {
    "ma01" : 1,
    "ma02" : 2,
    "ma03" : 3,
    "ma04" :4
}
dem = 0
for d in point.values():
    if d >= 3 and d <= 3.5:
        dem += 1
print(dem)
point["ma05"] = 0
a = []
for msv, d in point.items():
    if d < 2:
        a.append(msv)
for i in a:
    point.pop(i)
print(point)
