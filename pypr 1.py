# Построение графика 

import  matplotlib . pyplot  как  plt
импортировать  numpy  как  np

х  =  нп . linspace ( 0 , 10 , 50 )
у  =  х

plt . title ( "Линейная зависимость y = x" )   
plt . xlabel ( "x" )                            # Ось x
plt . ylabel ( "y" )                            # Ось y
plt . grid ()                                 # Визуал сетки
plt . plot ( x , y , "r--" )                      # Настройка графика, (r - красный цвет, "-" это пунктирная линия.)
plt . показать ()