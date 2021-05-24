x = 1
angle = 0
ydalene = 2
def setup():
    size (600,400)

def draw():
    global x,angle,ydalene
    
    if x < 281:
        translate(300,200)
        stroke(random(255),random(255),random(255))
        rotate(radians(angle))
        rect(x,20,80,60)
        ellipse(x,0,20,20)
    x = x + 0.5
    angle = angle + 130
    if  x == 280:
         background(283)
    if  x > 282:
        strokeWeight(150)
        stroke(255,255,255)
        point(random(0,600),random(0,400))
    if  x > 283:
        strokeWeight(150)
        stroke(255,255,0)
        point(300,200)
        textSize(30)
        text(u"КОНЕЦ",250,210) 
        
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
