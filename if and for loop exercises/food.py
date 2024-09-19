indian=['samosa','daal','naan']
chinese=['egg role','pot sticker','fried rice']
italian=['pizza','pasta','risotto']

dish=input('enter a dish: ')
if dish in indian:
    print(f"{dish} is indian")
elif dish in chinese:
    print(f"{dish} is chinese")
elif dish in italian:
    print(f"{dish} is italian")
else:
    print("i don't know what it is")