import funcion33 as f

def main():
    jugador=[]
    while True:
        print('1.- registrar puntajes')
        print('2.- listar todos los puntajes')
        print('3.- imprimir por tipo')
        print('4.- salir')

        opcion = input('selecione una opcion')

        if opcion == '1':
            f.registrar_puntajes(jugador)
        elif opcion == '2':
            f.listar_todos_los_puntajes(jugador)
        elif opcion == '3':
            f.imprimir_por_tipo(jugador)
        elif opcion == '4':
            print('salien del programa')
            break
        else:
            print('opcion no valida,intente denuevo')
if __name__ == 'main':
   main()



