time_in = input('Enter time in 12hr clock time in format hh:mm:ssAM or hh:mm:ssPM ')
time_list = time_in.split(':')

if 'PM' in time_list[2]:
    if int(time_list[0]) != 12:
        hr = str(int(time_list[0])+12)
    else:
        hr = time_list[0]
    sec = time_list[2].strip('PM')
else:
    hr = int(time_list[0])
    if hr == 12:
        hr = '00'
    sec = time_list[2].strip('AM')
mi = time_list[1]

#print(hr,sec,mi,sep=':')
print(':'.join([hr,mi,sec]))
'''
#Solution 1 
ins = input().strip()

is_pm = ins[-2:].lower() == 'pm'
time_list = list(map(int, ins[:-2].split(':')))

if is_pm and time_list[0] < 12:
    time_list[0] += 12

if not is_pm and time_list[0] == 12:
    time_list[0] = 0

print(':'.join(map(lambda x: str(x).rjust(2, '0'), time_list)))


#Solution 2
t=list(input().split(':'))
if t[0]=="12" : t[0]="00"
if t[2][-2:]=='PM': t[0]=str(int(t[0])+12)
t[2]=t[2][:-2]
print(":".join(t))
'''