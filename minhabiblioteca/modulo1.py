def fatorial(num):
     fat = 1
     for i in range(num):
        fat = fat*(num - i)
     return (f"O fatorial de {num} é: {fat}")
    
