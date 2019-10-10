def setup():
    size(700, 700)
    noFill()
    frameRate(10)

def draw():
    background(255, 100, 200)
    for x in range(0, width - 70, 70):
        for y in range(0, height - 20, 20):
            for i in range(100, 200, 100):
                ellipse(x, y, 50, 50)
            fill(255, 120, random (0,200))
            strokeWeight(random (0,50))
            ellipse(x, y, x + random(0, 150), y + random(0, 150))
