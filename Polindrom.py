
# "А роза #упала - на лапу Азора   ?!"

my_text = input("Введите текст - ")
my_tuple = (".",","," ","#","-","?","!","*")
global rezult

def reverse(rev):
    return rev[::-1]

def func (pol):
    global rezult
    for i in my_tuple:
        if i in pol:
            rezult=(pol.replace(i,""))
            func(rezult)
        else:
            rezult = pol

text = my_text.lower()

if __name__ == '__main__':
    func(text)

print("Да, это палиндром" if reverse(rezult) == rezult else "Нет,это не палиндром")

























