from datetime import date

def age(birthdate):
    
    birthdate = birthdate.split('-')
    today = str(date.today()).split('-')
    age = int(today[0]) - int(birthdate[2]) 
    if today[1] == birthdate[1]:
        if today[2] > birthdate[0]:
            return age + 1
    elif today[1] > birthdate[1]:
        return age + 1
    else: return age
    

print(age("01-06-1990"))

