import turtle
import time
import random

posponer = 0.1
score = 0
high_score = 0

wn = turtle.Screen()

wn.title('Juego de Snake')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

#Cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('#1D8348')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,100)
comida.direction = 'stop'

#cuerpo serpiente
segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('#1D8348')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('score: 0         highscore: 0', align='center',font=('courier', 24, 'normal'))




def arriba():
    cabeza.direction = 'up'

def abajo():
    cabeza.direction = 'down'

def izquierda():
    cabeza.direction = 'left'

def derecha():
    cabeza.direction = 'right'


def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    
#teclado
wn.listen()
wn.onkeypress(arriba,'Up')
wn.onkeypress(abajo,'Down')
wn.onkeypress(izquierda,'Left')
wn.onkeypress(derecha,'Right')


while True:
    wn.update()

    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'
        score = 0
        texto.clear()
        texto.write('score: {}        highscore: {}'.format(score,high_score) , align='center',font=('courier', 24, 'normal'))

        for segmento in segmentos:
            segmento.goto(1000,1000)
        
        segmentos.clear()
    
    
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        cuerpoSerpiente = turtle.Turtle()
        cuerpoSerpiente.speed(0)
        cuerpoSerpiente.shape('square')
        cuerpoSerpiente.color('#239B56')
        cuerpoSerpiente.penup()
        segmentos.append(cuerpoSerpiente)

        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write('score: {}        highscore: {}'.format(score,high_score) , align='center',font=('courier', 24, 'normal'))
    

    totalseg = len(segmentos)
    for index in range(totalseg -1,0,-1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)

        
    if totalseg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            score = 0
            texto.clear()
            texto.write('score: {}        highscore: {}'.format(score,high_score) , align='center',font=('courier', 24, 'normal'))
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = 'stop'

            for segmento in segmentos:
                segmento.goto(1000,1000)
            segmentos.clear()

    time.sleep(posponer)