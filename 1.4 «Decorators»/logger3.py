# Применить написанный логгер к приложению из любого предыдущего д/з.
from logger1 import info_decorator

if __name__ == '__main__':
    with open('mylog.log', "r") as file:
        print(file.read())

    @info_decorator
    def voenkomat(height, age, children, study):
        if age >= 18 and age <= 27:
            if children < 2:
                if study == False:
                    if height < 170:
                        return ('В танкисты')
                    elif height < 210:
                        return('На флот')
                    elif height < 185:
                        return('В десантники')
                    else:
                        return('В другие войска')
                else:
                    return('Непризывной по учебе')
            else:
                return('Непризывной из-за детей')
        else:
            return('Непризывной возраст')

    print(voenkomat(180, 19, 1, True))
