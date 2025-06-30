def solution(n: int) -> int:
    # your code    
    is_simple_numbers = [True] * (n + 1)
    is_simple_numbers[0] = False
    is_simple_numbers[1] = False
    # решето эратосфена
    for i in range(2, int(n ** 0.5) + 1):
        if is_simple_numbers[i]:                
            for num in range(i * i, n + 1, i):
                is_simple_numbers[num] = False

    simple_numbers = []
    for i in range(2, n + 1):
        if is_simple_numbers[i]:
            simple_numbers.append(i)
    
    simple_numbers_count = len(simple_numbers)
    # print(simple_numbers)
    if simple_numbers_count <= 2:
        return 0
    ans = 0    
    '''
    Мы должны перебирать все пары для q1 = 2, все тройки для q1 = 3, все пятерки для q1 =5, и тд. 
    И это очень вычислительно затратно... 
    но взглянем на условие: сумма этих комбинаций должна делиться на **2**q1 - ЧЕТНОЕ ЧИСЛО. 
    1) Все простые числа за исключением 2 - нечетные
    2) Значит длина комбинаций за исключением пар - тоже нечетная (3 - 3, 5 - 5 и тд)
    3) **Сумма нечетного количества нечетных чисел всегда будет нечетной**
    4) Соответственно нечетное число на четное делиться не может.
    То есть мы должны искать только пары - q1 = 2 - всегда
    '''    
    # q1 = 2
    # d = q1 * 2 = 4
    # index of q1 всегда 1


    # ДОЛГО
    # for i in range(1, simple_numbers_count):
    #     q2 = simple_numbers[i]
    #     for j in range(i + 1, simple_numbers_count):
    #         q3 = simple_numbers[j]
    #         if (q2 + q3) % d == 0:
    #             ans += 1                

    '''
    Надо чтобы сумма q2+q3 делилась на 4, 
    любое нечетное число при делении на 4 дает либо 1 либо 3 в остатке,
    то есть оно может быть вида 4k + 1 или 4k + 3, где k - целый остаток от деления 
    нам нужны пары вида (4k + 1, 4k + 3) или (4k + 3, 4k + 1) - так как (4k_1 + 3 + 4k_2 + 1) % 4 === 0
    '''
    mod1_count = 0
    mod3_count = 0
    ans = 0
    for i in range(1, simple_numbers_count):
        if simple_numbers[i] % 4 == 1:
            mod1_count += 1
            ans += mod3_count
        if simple_numbers[i] % 4 == 3:
            mod3_count += 1
            ans += mod1_count             
    
    return ans
print('answer', solution(7))