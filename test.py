def angle_avg(angle,n):
    diff = 0.0
    last = angle[0]
    sum  = angle[0]
    i = 0
    print last
    for i in range(1,n):
        last += (angle[i] - angle[i - 1] + 180) % 360 - 180
        sum  += last
        #print last
    sum = float(sum)
    return (sum/n)%360

# a = [350,10,10,340,150,180,190,200]
# print angle_avg(a,8)
a = [88.75]*8
a.append(350)
print angle_avg(a,9)