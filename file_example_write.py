#lets create a journal
with open("journal.txt","w")as journal:
    while True: #infinite loop until q is pressed
        text=input("enter a journal entry: (press q to quit)")
        if text=="q":
            break
        journal.write(text.capitalize()+"\n")

