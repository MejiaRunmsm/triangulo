import pygame

WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

def draw_plano_cartesiano():
    posSquare = 0
    while(posSquare <= WIDTH or posSquare <= WIDTH):
        pygame.draw.lines(WIN, WHITE, closed=False, points=[(0,posSquare), (WIDTH,posSquare)], width=1 )
        pygame.draw.lines(WIN, WHITE, closed=False, points=[(posSquare,0), (posSquare,HEIGHT)], width=1 )
        posSquare += 100

def det(a,b):
        return a[0]*b[1]-a[1]*b[0]

class Triangulo: 
    def __init__(self, A, B, C):
        self.Ax = A[0]
        self.Ay = A[1]
        self.A = (A[0], HEIGHT-A[1])

        self.Bx = B[0]
        self.By = B[1]
        self.B = (B[0], HEIGHT-B[1])

        self.Cx = C[0]
        self.Cy = C[1]
        self.C = (C[0], HEIGHT-C[1])

        self.Dx = self.Bx-self.Ax
        self.Dy = self.By-self.Ay
        self.Ex = self.Cx-self.Ax
        self.Ey = self.Cy-self.Ay

    def obtenerW(self, Px, Py):

        #w1 = -(self.Ex*(self.Ay+Py) + self.Ey*(Px-self.Ax))/(self.Dx*self.Ey - self.Dy*self.Ex)
        #w2 = (Py - self.Ay - w1*self.Dy)/self.Ey

        w1 = ( det((Px,Py),(self.Dx,self.Dy)) - det((self.Ax,self.Ay),(self.Dx,self.Dy)) )/(det((self.Ex,self.Ey),(self.Dx,self.Dy)))
        w2 = -( det((Px,Py),(self.Ex,self.Ey)) - det((self.Ax,self.Ay),(self.Ex,self.Ey)) )/(det((self.Ex,self.Ey),(self.Dx,self.Dy)))
        #print(w1,w2)
        return ( w1,w2 )
    
    def draw(self):
        pygame.draw.lines(WIN, YELLOW, closed=True, points=[self.A, self.B, self.C], width=2)
        #pygame.draw.lines(WIN, GREEN, closed=False, points=[(self.Bx,self.By), (self.Cx,self.Cy)])
        #pygame.draw.lines(WIN, BLUE, closed=False, points=[(self.Cx,self.Cy), (self.Ax,self.Ay)])

    def draw_vecs(self, Px, Py):
        W = self.obtenerW(Px,Py)
        print((self.Ax+W[0]*self.Ex, self.Ay+W[0]*self.Ey))
        pygame.draw.lines(WIN, BLUE, closed=False, points=[self.A, (self.Ax+W[1]*self.Dx, HEIGHT-(self.Ay+W[1]*self.Dy))], width=4)
        pygame.draw.lines(WIN, BLUE, closed=False, points=[self.A, (self.Ax+W[0]*self.Ex, HEIGHT-(self.Ay+W[0]*self.Ey))], width=4)
        pygame.draw.lines(WIN, BLUE, closed=False, points=[(self.Ax+W[1]*self.Dx, HEIGHT-(self.Ay+W[1]*self.Dy)), (self.Ax+W[0]*self.Ex+W[1]*self.Dx, HEIGHT-(self.Ay+W[0]*self.Ey+W[1]*self.Dy))], width=4)

class Punto:
    def __init__(self, x, y):
        self.Cx = x
        self.Cy = y
        self.C = (x, HEIGHT-y)

    def setPos(self, x, y):
        self.Cx = x
        self.Cy = y
        self.C = (x, HEIGHT-y)

    def draw(self):
        w = triangulo.obtenerW(self.Cx,self.Cy)
        if (w[0] >= 0 and w[1] >= 0 and w[0]+w[1] <=1):
            pygame.draw.circle(WIN, GREEN, self.C, 6)
        else:
            pygame.draw.circle(WIN, RED, self.C, 6)


def draw_window():
    WIN.fill(BLACK)
    draw_plano_cartesiano()
    
    triangulo.draw()
    triangulo.draw_vecs(punto.Cx, punto.Cy)
    punto.draw()

    pygame.display.update()


triangulo = Triangulo((100,100),(200,400),(400,200))
punto = Punto(200,200)
#print((punto.Cx,punto.Cy))
#print (triangulo.obtenerW(punto.Cx,punto.Cy))

def main():    

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                x,y = pygame.mouse.get_pos()
                print(x,HEIGHT-y)
                punto.setPos(x,HEIGHT-y)


        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()

