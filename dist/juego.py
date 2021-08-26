from tkinter import *
from tkinter import Canvas
from random import randint
from tkinter.messagebox import*

letrasUsadas=[]
vidas=6
letrasAcertadas=0

'''
Verifica si la letra que se ingreso en el entry pertenece a la palabra del archivo plano y cuantas veces esta
'''
def probarletra():
    global vidas
    global letrasAcertadas
    letrasUsadas.append(letraObtenida.get()) # Agrega a la lista letrasUsadas la letra que ingreso el usuario
    conjuntoLetras[ord(letraObtenida.get())-97].config(text="") # ord nos permite pasar de caracter a su parte entera - quita la letra que digito el usuario
    if letraObtenida.get() in palabra: 
        if palabra.count(letraObtenida.get())>1: # Comprueba si la letra esta mas de una vez en la palabra
            letrasAcertadas+=palabra.count(letraObtenida.get()) # Cuantas veces esta la letra en la palabra y aumenta el contador de letras acertadas
            for i in range(len(palabra)):
                if palabra[i]==letraObtenida.get(): # Verifica la poisicion donde esta la letra obtenida
                    guiones[i].config(text=""+letraObtenida.get()) #  Anexa la letra obtenida
        else: # Si solo hay una letra en la palabra
            letrasAcertadas+=1
            guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get()) #  Anexa la letra obtenida - index le da ubicacion de la letra en la palabra
        if letrasAcertadas==len(palabra): # Verifica si el numero de las letras acertadas es el mismo a la longitud de la palabra
            showwarning(title="Victoria", message= "Adivinaste la palabra!!!!")
    else: # Sino se baja una vida y se pinta una parte del cuerpo
        vidas-=1   
        dibujar_cuerpo()  
        if vidas ==0:
            showwarning(title="Derrota",message= "se te han acabado las vidas")
    letra.delete(0, 'end')
    letra.focus()


# funcion para acomodar las letras del abcedaria en el frame
def colocarLetras():
    x=50
    y=150
    contador=0
    Label(juego,text="Letras sin usar", bg="darkred", fg="white", font=("Arial italic", 15)).place(x=50,y=80)
    for i in range(26): # 
        contador+=1
        conjuntoLetras[i].place(x=x,y=y) #Le da la posicion en X y Y a las letras del abcedario
        x+=30
        if contador==5: # Cuando llega a 5 aumenta su eje Y y en X se reinicia
            y+=35
            contador=0
            x=50
    
def dibujar_cuerpo():
    if vidas == 5:
        # Cabeza
        canvas.create_oval(200, 90, 270, 160, width=4, outline="black")
    elif vidas == 4:
        # Cuerpo
        canvas.create_rectangle(235, 160, 245, 350, fill="black")
    elif vidas == 3:
        # Brazo izquierdo
        canvas.create_line(200, 230, 235, 175, width=5, fill="black")
    elif vidas == 2:
        # Brazo derecho
        canvas.create_line(245, 175, 280, 230, width=5, fill="black")
    elif vidas == 1:
        # pierna izquierda
        canvas.create_line(200, 440, 235, 350, width=5, fill="black")
    elif vidas == 0:
        # pierna derecha
        canvas.create_line(245, 350, 280, 440, width=5, fill="black")       
              

# Crea la raiz donde se va a configurar el tkinter
tablero = Tk()
tablero.title("AHORCADO")
tablero.iconbitmap("Anonyymous.ico")
tablero.config(relief="groove", bd=10)
tablero.resizable(False, False)

# Lee el archivo plano donde estan las palabras a adivinar
archivo=open("palabras.txt","r")
conjuntopalabras=list(archivo.read().split("\n")) # Crea una lista de las palabras que encontro en el archivo plano

palabra = conjuntopalabras[randint(0, len(conjuntopalabras)-1)].lower() # Toma una palabra aleatoriamente de la lista y las convierte a minuscula

letraObtenida=StringVar() # almacena como variable la letra que digito el usuario

# Cuadro izquierdo del juego
juego = Frame(tablero)
juego.config(width=550, height=600, relief="sunken", bd=15, bg="darkred")
juego.grid_propagate(False)
juego.pack(side=LEFT, anchor=W, fill=BOTH)

letrero = Label(juego, text="Ingresar letra", font=("Verdana", 20), bg="darkred", fg="white")
letrero.grid(row=0, column=0, padx=10, pady=10)

letra = Entry(juego, width=2, font=("Vedana", 24), textvariable=letraObtenida)
letra.grid(row=0, column=1, padx=10, pady=10)

btn_probar = Button(juego, text="Probar", bg="darkgray", bd= 5, width=10, height=2, command=probarletra)
btn_probar.grid(row=1, column=1, pady=10)

btn_salir = Button(juego, text="Salir", bg="darkgray", bd=5, width=10, height=2, command=tablero.destroy).place(x=320, y=70)

# Importa la imagen del ahorcado
from tkinter import PhotoImage
foto = PhotoImage(file="ahorcado.png")
Label(juego, image=foto).place(x=250, y=150)

# Crea el contenedor del canvas
dibujo = Frame(tablero) # Tablero derecho
dibujo.pack(side=RIGHT, anchor=E) # Lo ubica en el lado derecho en la direccion Este
dibujo.config(relief="sunken", bd=15, bg="black")

# Crea el linezo donde se va a dibujar
canvas = Canvas(dibujo, width=500, height=600, bg="darkred")
canvas.pack(expand=YES, fill=BOTH)

guiones=[Label(juego,text="_", font=("Arial italic",25), bg="darkred") for _ in palabra ]
cordenadaX=50 
for i in range(len(palabra)):
    guiones[i].place(x=cordenadaX,y=450) #Dependiendo del numero de letras de la palabra, va colocando guiones
    cordenadaX+=50    

conjuntoLetras=[Label(juego,text=chr(j+97),font=("Arial italic",20), bg="darkred", fg="white", padx=5) for j in range(26)] # Conjunto de letras del abcdario
colocarLetras()

# Tronco del conlagero
canvas.create_rectangle(450, 50, 470, 550, fill="black")
# Linea que va hacai la izquierda
canvas.create_rectangle(230, 30, 470, 50, fill="black")
# Linea que representa la soga
canvas.create_rectangle(230, 50, 250, 90, fill="black")

tablero.mainloop()
