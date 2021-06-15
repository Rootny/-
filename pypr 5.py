# Построение графиков

импортировать  numpy  как  np
import  matplotlib . pyplot  как  plt

x  = [ 1 , 5 , 10 , 15 , 20 ] # Список № 1
y  = [ 1 , 7 , 3 , 5 , 11 ]    # Список № 2

plt . plot ( x , y , label = 'steel price' )             # Корды
plt . title ( 'Цена на графике' , размер шрифта = 15 )
plt . xlabel ( 'Day' , fontsize = 12 , color = 'blue' )    # Колор
plt . ylabel ( 'Price' , fontsize = 12 , color = 'blue' ) # Колор
plt . легенда ()
plt . сетка ( True )
plt . text ( 15 , 4 , 'подрасти!' )

plt . показать ()
