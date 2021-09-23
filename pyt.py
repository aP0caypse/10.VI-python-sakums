import math
x1=float(input("x1:"))
y1=float(input("y1:"))
x2=float(input("x2:"))
y2=float(input("y2:"))
x3=float(input("x3:"))
y3=float(input("y3:"))
a12=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
a23=math.sqrt((x2-x3)*(x2-x3)+(y3-y2)*(y3-y2))
a31=math.sqrt((x3-x1)*(x3-x1)+(y3-y1)*(y3-y1))
print(a12,a23,31)
if a12<(a23+a31) and a23<(a12+a31) and a31<(a23+a12):

    l=a12+a23+a31
    p2=l/2

    S=math.sqrt(p2*(p2-a12)*(p2-a23)*(p2-a31))

    e=S/l
    print("taisnstūra efektivitāte:{0:.4e}".format(e))
else:
    print("trijsturis nav iespejams")
