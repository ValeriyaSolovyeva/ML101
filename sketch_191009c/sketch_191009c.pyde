angle = 0
offset = 150
step = 100
speed = 0.07
num = 20
def setup():
    size(800, 300)
    fill(0)
    noStroke()
def draw():
    background(255, 255, 255)
    global angle 
    y1 = offset + sin(angle) * step
    y2 = offset + sin(angle + 0.4) * step
    y3 = offset + sin(angle + 0.5) * step
    y4 = offset + sin(angle + 0.7) * step
    y5 = offset + sin(angle + 0.9) * step
    y6 = offset + sin(angle + 1.1) * step
    y7 = offset + sin(angle + 1.4) * step
    y8 = offset + sin(angle + 1.5) * step
    ellipse(50, y1, 20, 20)
    ellipse(150, y2, 20, 20)
    ellipse(250, y3, 20, 20)
    ellipse(350, y4, 20, 20)
    ellipse(450, y5, 20, 20)
    ellipse(550, y6, 20, 20)
    ellipse(650, y7, 20, 20)
    ellipse(750, y8, 20, 20)
    y9 = offset + cos(angle + 5) * step
    y10 = offset + cos(angle + 6) * step
    y11 = offset + cos(angle + 7) * step
    y12 = offset + cos(angle + 8) * step
    y13 = offset + cos(angle + 9) * step
    y14 = offset + cos(angle + 10) * step
    y15 = offset + cos(angle + 11) * step
    y16 = offset + cos(angle + 12) * step
    fill (0, random (200,255), 255)
    ellipse(50, y9, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(150, y10, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(250, y11, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(350, y12, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(450, y13, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(550, y14, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(650, y15, 20, 20)
    fill (0, random (200,255), 255)
    ellipse(750, y16, 20, 20)
    angle = angle + speed
