
# функция ввода пользователя. Здесь их входных данных получается отсортированный массив. 
def userInput():
    target = int(input("Загаданное число:" ))
    min = int(input("Нижняя граница:" ))
    max = int(input("Верхняя граница:" ))
    arr = []
    for i in range(min, max + 1):
        arr.append(i)
        i += 1
    arr.sort()
    # print(arr)
    return target, arr



# реализация алгоритма бинарного поиска
def guess(target, arr):
    min = arr[0]
    length = len(arr)
    max = arr[length - 1]
    mid = 0
    counter = 0

    while min <= max:
        counter += 1
        # print('Число итераций:', counter)
        mid = (max + min) // 2
        # print('mid', arr[mid])

        if arr[mid] < target:
            min = mid + 1
        elif arr[mid] > target:
            max = mid - 1
        else:
            #искомое число
            return arr[mid], counter
        


#итоговая функция
def mainFunc():
    target, arr = userInput()
    guessedNum, iterationNum = guess(target, arr)
    # return [guessedNum, iterationNum]
    print("Угаданное число:", guessedNum,  "\nКоличество итераций:", iterationNum)
mainFunc()

