from datetime import date

dat1, date2 = input().split('-'), input().split('-')
date1 = date(int(dat1[0]), int(dat1[1]), int(dat1[2]))
date2 = date(int(date2[0]), int(date2[1]), int(date2[2]))
res = min(date1, date2)
print(res.strftime('%d-%m (%Y)'))