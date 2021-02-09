def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """
    w = []
    for i in two_dim_words:
        w += i
    w.sort(key=len)
    
    return w


def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """
    w ={}
    e=[]
    ee = []
    qq = set(numbers)
    for i in range(9):
        e.append(numbers.count(i))
    for i in range(4):
        ee.append(max(e))
        f = e.index(max(e))
        w[f] = max(e)
        e.pop(f)
    return w


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    pass


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    pass

def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    pass


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """
    qq = set()
    pp = []
    ppp = []
    r = (len(lst1),len(lst2))
    y = int(max(r))
    o = int(min(r))
    qq = set(lst1)
    ww = set(lst2)
    p = qq - ww
    pp = list(p)
    pp.sort()
    return pp


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """

    return res

