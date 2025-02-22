start=int(input('Start:'))
end=int(input('End:'))
for row in range(start,end+1):
    fact=1
    for col in range(1,row+1):
       fact*=col
    print(f'{row}!={fact}')