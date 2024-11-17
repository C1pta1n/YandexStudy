def min_days_to_complete_tasks(n, k, directions):
    # Сортируем направления
    directions.sort()
    
    # Инициализация количества дней
    days = 0
    i = 0
    
    while i < n:
        # Увеличиваем счетчик дней
        days += 1
        
        # Устанавливаем предел для текущей группы дел
        current_end = directions[i] + k
        
        # Пропускаем все подходящие направления в текущий день
        while i < n and directions[i] <= current_end:
            i += 1
    
    return days

# Считывание данных
n, k = map(int, input().strip().split())
directions = list(map(int, input().strip().split()))

# Вывод результата
result = min_days_to_complete_tasks(n, k, directions)
print(result)