def solution(n: int, m: int, p: list[int]) -> list[int]:        
    # lower_bound будет хранить минимально допустимое значение для res_p[i]
    # upper_bound будет хранить максимально допустимое значение для res_p[i]

    # Заполняем lower_bound проходом слева направо
    lower_bound = [0] * n 
    
    # Инициализация первого элемента
    if p[0] != -1:
        if p[0] < m: # Если первый раунд меньше минимального заработка
            return [-1]
        lower_bound[0] = p[0]
    else:
        lower_bound[0] = m # Минимальный возможный заработок за первый раунд

    for i in range(1, n):
        if p[i] != -1:
            # Если значение p[i] известно, оно должно быть не меньше p[i-1] + m
            if p[i] < lower_bound[i-1] + m:
                return [-1]
            lower_bound[i] = p[i]
        else:
            # Если p[i] неизвестно, его минимальное значение - это p[i-1] + m
            lower_bound[i] = lower_bound[i-1] + m

    # Заполняем upper_bound проходом справа налево

    #    Убеждаемся, что каждое значение не превышает p[i+1] - m
    upper_bound = [0] * n

    # Инициализация последнего элемента
    if p[n-1] != -1:
        upper_bound[n-1] = p[n-1]
    else:
        '''
        Если последний элемент неизвестен, ему нет верхнего ограничения от последующих
        Но ему есть ограничение от предыдущих: он должен быть не меньше lower_bound[n-1]                        
        '''        
        upper_bound[n-1] = lower_bound[n-1] 


    for i in range(n - 2, -1, -1):
        if p[i] != -1:
            # Если p[i] известно, оно должно быть не больше p[i+1] - m
            if p[i] > upper_bound[i+1] - m:
                return [-1]
            upper_bound[i] = p[i]
        else:
            # Если p[i] неизвестно, его максимальное значение - это p[i+1] - m
            upper_bound[i] = upper_bound[i+1] - m
        
        # upper_bound[i] также не может быть меньше lower_bound[i]
        # Если границы пересеклись, решение невозможно
        if upper_bound[i] < lower_bound[i]:
            return [-1] 

    '''
    Восстанавливаем res_p с учетом обеих границ
    Если p[i] == -1, мы можем выбрать любое значение между lower_bound[i] и upper_bound[i].        
    Для восстановления используем upper_bound как окончательный массив, так как он
    уже скорректирован сверху, и если -1 были, они заполнены максимальным возможным значением
    при условии выполнения p[i] <= p[i+1] - m.        
    '''          
    res_p = [0] * n
    res_p[n-1] = upper_bound[n-1] # Последний элемент определяется upper_bound

    for i in range(n - 2, -1, -1):
        if p[i] != -1:
            res_p[i] = p[i]
        else:            
            res_p[i] = res_p[i+1] - m                                                             


    # после восстановления надо только посчитать разницу между res_p[i] и res_p[i + 1], 
    # отталкиваясь от первого элемента
    ans = [0] * n
    ans[0] = res_p[0]
    
    for i in range(1, n):
        ans[i] = res_p[i] - res_p[i - 1]

    return ans

print(solution(3, 1, [1, 2, 3]))