import pickle
from tkinter import *

class Node:
    def __init__(self,nam,qst, grp):
        self.name = nam
        self.question = qst
        self.group = grp
        self.next = None
        self.previous = None
        self.left = None
        self.rigth = None

class LinkedList:
    def __init__(self):
        self.first = None

        source = open('Personajes', 'ab+')
        source.seek(0)

        try:
            self.first = pickle.load(source)
        except EOFError:
            pass
        finally:
            source.close()
            del source

    def add (self,name,question,group):
        if self.first is None:
            new_node = Node(name,question,group)
            self.first = new_node
            self.saveCharacters()
            return

        current = self.first

        while True:
            if current.group != group:
                if current.rigth == None:
                    new_node = Node(name,question,group)
                    new_node.left = current
                    current.rigth = new_node
                    self.saveCharacters()
                    return
                else:
                    current = current.rigth
            else:
                while True:
                    if current.next == None:
                        new_node = Node(name,question,group)
                        new_node.previous = current
                        current.next = new_node
                        self.saveCharacters()
                        break
                    else:
                        current = current.next
                break

    def saveCharacters(self):
        files = open('Personajes', 'wb')
        pickle.dump(self.first, files)
        files.close()
        del files

    def printCharacters(self):
        current = self.first
        while True:
            print('Nombre: ',current.name, '\nGrupo: ',current.group, '\n')
            if current.next == None:
                while current.previous != None:
                    current = current.previous
                if current.rigth != None:
                    current = current.rigth
                else:
                    break
            current = current.next

def Preguntas(currentt,Ventana, Txt):
    global num 
    global current
    num = 0
    current = currentt
    def Yes():
        global num
        global current
        num += 1
        print(num)
        if num== 1:
                txt = current.question+'\n'
                Txt.config(text=txt)
        elif num == 2:
            txt = 'Tu personaje es '+ current.name
            ImgChar.place(x = 570, y = 500)
            Txt.config(text=txt)
            Byes.place_forget()
            Bno.place_forget()
            Bsalir.place(x = 520, y = 850)
            num = 0
        else:
            if current.next == None:
                return(1)
            else:
                current = current.next
            if current.rigth == None:
                return(1)
            else:
                current = current.rigth
    def No():
        global num
        global current
        num -= 1
        if num== 1:
            print('bandera')
            while True:
                txt = current.question+'\n'
                Txt.config(text=txt)
                if num == 2:
                    txt = 'Tu personaje es '+ current.name
                    Txt.config(text=txt)
                    num = 0
                else:
                    if current.next == None:
                        return(1)
                    else:
                        current = current.next
        else:
            if current.rigth == None:
                return(1)
            else:
                current = current.rigth

    txt = 'Tu personaje pertenece al grupo de '+current.group+'?\n'
    Txt.config(text=txt)

    BtN = PhotoImage(file = './Fondos/No.png')
    BtY = PhotoImage(file = './Fondos/Si.png')
    Byes = Button(Ventana, image = BtY, command = Yes)
    Bno = Button(Ventana, image = BtN, command = No)
    Bno.place(x = 820, y = 500)
    Byes.place(x = 520, y = 500)

    BtS = PhotoImage(file = './Fondos/Continuar.png')
    Bsalir = Button(Ventana, image = BtS, command = Ventana.destroy)

    Char = PhotoImage(file = './Fotos_Personajes/Goku.png')
    ImgChar = Label(Ventana,image = Char)

    Ventana.mainloop()



def Inicio():
    def Juego():
        Bcont.place_forget()
        background.config(image = BG3)
        Preguntas(current,Ventana,Txt)

        Ventana.mainloop()
        

    def Instrucciones():
        Binicio.place_forget()

        Bcont.place(x = 520, y = 850)

        background.config(image = BG2)
        
        Txt.place(x = 50, y = 150, height = 300, width = 1300)

        Ventana.mainloop()

    Characters = LinkedList()
    
    current = Characters.first

    #Characters.add('Goku','Tu personaje vencio a Freezer en Namek?','Sayain Goku')
    #Characters.printCharacters()

    #Crear ventana
    Ventana = Tk()
    Ventana.geometry('1440x1024')

    #Cargamos todas las imagenes
    BG = PhotoImage(file = './Fondos/Fondo_Inicio.png')
    Bt = PhotoImage(file = './Fondos/Button.png')
    BtC = PhotoImage(file = './Fondos/Continuar.png')
    BG2 = PhotoImage(file = './Fondos/Fondo_Instrucciones.png')
    BG3 = PhotoImage(file = './Fondos/Fondo_Juego.png')


    #Agregamos un fondo
    background = Label(Ventana,image = BG)
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #Agregamos un boton
    Binicio = Button(Ventana, image = Bt, command = Instrucciones)
    Binicio.place(x = 520, y = 850)
    Bcont = Button(Ventana, image = BtC, command = Juego)

    #Agregamos cuadros de texto
    Txt = Label(Ventana, bg = '#FEF100', anchor = NW, fg = 'white', font = ('Sanchez',25), bd = 5, justify = 'left', text = 'Deberas pensar en un personaje, ya que lo hayas echo se te preguntara\ncaracteristicas de tu personaje y deberas responder si o no dependiendo si\ntu personaje tiene esa caracteristica, cuando el programa no logra\nadivinar el personaje te preguntara sus caracteristicas para agregarlo al\njuego.\n\nQue te diviertas.')
    
    Ventana.mainloop()

    #opc = Preguntas(current)

    #if opc == 1:
    #    print('\nAyudame a agregar un nuevo personaje: ')
    #    name = input('Nombre: ')
    #    quest = input('Ingrese una pregunta caracteristica para identificar al personaje: ')
    #    group = input('Ingrese al grupo al que pertenece: ')
    #    Characters.add(name, quest, group)
    #input()

Inicio()
