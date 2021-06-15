# Разделенные поля с графиками

import  matplotlib . pyplot  как  plt
импортировать  numpy  как  np

# Линейная зависимость
х  =  нп . linspace ( 0 , 10 , 50 )
у1  =  х

# Квадратичная зависимость
y2  = [ i ** 2  вместо  i  в  x ]

plt . figure ( figsize = ( 9 , 9 )) # Настройка размеров подложки
plt . subplot ( 2 , 1 , 1 )   # Расположение поля в области графика
plt . сюжет ( x , y1 )
plt . title ( "Зависимость: y1 = x, y2 = x ^ 2" )
plt . ylabel ( "y1" , fontsize = 14 ) # ось y
plt . grid ( True ) # реал тру сетка (стринги)
plt . подзаговор ( 2 , 1 , 2 )
plt . plot ( x , y2 ) # Построение графика
plt . xlabel ( "x" , fontsize = 14 ) # Ось x
plt . ylabel ( "y2" , fontsize = 14 ) # Ось y
plt . grid ( True ) # Сетка

plt . показать ()
