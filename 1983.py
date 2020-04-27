studnt = int(input())
regisno = []
note = []
for i in  range(studnt):
    r,n = input().split()
    regisno.append(r)
    note.append(float(n))
notemax = max(note)
if notemax<8:
    print('Minimum note not reached')
else:
    a = note.index(notemax)
    print(regisno[a])