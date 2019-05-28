screenTitle("Put the guy on fire out!")
objectsAdd(create(int(WIDTH/2), int(HEIGHT/2)-3, "bucket.png", blue, "apple"))
player = create(int(WIDTH/2), int(HEIGHT/2)+1, "player.png", orange, "player")
objectsAdd(create(-2, -2, "fireball.png", red, "fireball"))
objects[1].animations["IDLE"] = [0,1,2]
objects[1].maxlatency = 4
genMap("map.map", {"1":["grass", "grass.png", green]})
player.animations["Right"] = [0, 1]
player.animations["Left"] = [2, 3]
player.animations["IDLE"] = [0, 1, 0, 1, 2, 3, 2, 3]
player.animation = "IDLE"
player.maxlatency = 4
speed = 4
totalFireBalls = 0
goals = [10, 50, 100, 150, 200, 300, 400, 500]
goalindex = 0

while RUNNING:
    eventget = events()
    if not PAUSE:
        for event in eventget:
            if keydown(UPKEY, event):
                player.vy = -speed
                player.vx = 0
                player.animation = "Left"
            if keydown(DOWNKEY, event):
                player.vy = speed
                player.vx = 0
                player.animation = "Right"
            if keydown(LEFTKEY, event):
                player.vx = -speed
                player.vy = 0
                player.animation = "Left"
            if keydown(RIGHTKEY, event):
                player.vx = speed
                player.vy = 0
                player.animation = "Right"
        update(player)
        for object in objects:
            if collision(player, object, ["apple"]):
                SCORE += 10
                speed += .25
                object.x, object.y = (randint(0, WIDTH-1))*BLOCKSIZE*SCALE, (randint(0, HEIGHT-1))*BLOCKSIZE*SCALE
            if collision(player, object, ["fireball"]):
                SCORE -= goalindex
        if player.x <= -(BLOCKSIZE+1)*SCALE:
            player.x = WIDTH*BLOCKSIZE*SCALE-1
        if player.x >= (WIDTH)*BLOCKSIZE*SCALE:
            player.x = -(BLOCKSIZE) * SCALE
        if player.y <= -(BLOCKSIZE+1)*SCALE:
            player.y = HEIGHT*BLOCKSIZE*SCALE-1
        if player.y >= (HEIGHT)*BLOCKSIZE*SCALE:
            player.y = -(BLOCKSIZE) * SCALE
        for i in range(totalFireBalls):
            if objects[len(objects)-totalFireBalls+i].x <= 0:
                objects[len(objects) - totalFireBalls  + i].vx = 4
            if objects[len(objects)-totalFireBalls+i].x >= (WIDTH-1) * BLOCKSIZE * SCALE:
                objects[len(objects) - totalFireBalls+ i].vx = -4
            if objects[len(objects)-totalFireBalls+i].y <= 0:
                objects[len(objects) - totalFireBalls + i].vy = 4
            if objects[len(objects)-totalFireBalls+i].y >= (HEIGHT-1) * BLOCKSIZE * SCALE:
                objects[len(objects) - totalFireBalls + i].vy = -4
    if SCORE >= goals[goalindex]:
        player.sprite, player.size = spriteLoad("saved.png", PATH+"/Sprites/")
        player.animations["IDLE"] = [0]
        player.animation = "IDLE"
        player.vx = 0
        player.vy = 0
        player.index = 0
        for i in range(0, (FPS*3)+1):
            events()
            if RUNNING == False:
                break
            clearScreen()
            for object in range(1, len(objects)):
                draw(objects[object])
            draw(player)
            message("You saved the guy!", white, int((WIDTH * BLOCKSIZE * SCALE) / 2), 15, 15)
            display()
        player.sprite, player.size = spriteLoad("player.png", PATH+"/Sprites/")
        player.animations["IDLE"] = [0, 1, 0, 1, 2, 3, 2, 3]
        player.animation = "IDLE"
        player.maxlatency = 4
        speed = 4
        goalindex += 1
        if goalindex == len(goals):
            goalindex = 0
        for i in range(totalFireBalls):
            objectsRemove(objects[len(objects)-1])
        totalFireBalls = 0
        SCORE = 0
    if SCORE < 0:
        player.sprite, player.size = spriteLoad("lose.png", PATH+"/Sprites/")
        player.animations["IDLE"] = [0]
        player.animation = "IDLE"
        player.vx = 0
        player.vy = 0
        player.index = 0
        for i in range(0, (FPS*3)+1):
            events()
            if RUNNING == False:
                break
            clearScreen()
            for object in range(1, len(objects)):
                draw(objects[object])
            draw(player)
            message("The guy burnt...", white, int((WIDTH * BLOCKSIZE * SCALE) / 2), 15, 15)
            display()
        player.sprite, player.size = spriteLoad("player.png", PATH+"/Sprites/")
        player.animations["IDLE"] = [0, 1, 0, 1, 2, 3, 2, 3]
        player.animation = "IDLE"
        player.maxlatency = 4
        speed = 4
        goalindex = 0
        if goalindex == len(goals):
            goalindex = 0
        for i in range(totalFireBalls):
            objectsRemove(objects[len(objects)-1])
        totalFireBalls = 0
        SCORE = 0
    if int(SCORE/50 > totalFireBalls):
        clone(objects[1])
        objects[len(objects)-1].x = randint(0, WIDTH-1)*BLOCKSIZE*SCALE
        objects[len(objects)-1].y = randint(0, HEIGHT-1)*BLOCKSIZE*SCALE
        objects[len(objects) - 1].vx = choice([4, -4])
        objects[len(objects) - 1].vy = choice([4, -4])
        objects[len(objects) - 1].animations["IDLE"] = [0, 1, 2]
        objects[len(objects) - 1].maxlatency = 4
        totalFireBalls += 1
    clearScreen()
    for object in range(1,len(objects)):
        if not PAUSE:
            update(objects[object])
        draw(objects[object])
    if not PAUSE:
        update(objects[0])
    draw(objects[0])
    draw(player)
    message("Points: "+str(SCORE), white, int((WIDTH*BLOCKSIZE*SCALE)/4), 15, 15)
    message("Goal :"+str(goals[goalindex]), white, int((WIDTH*BLOCKSIZE*SCALE)/4)*3, 15, 15)
    if not player.vx and not player.vy:
        message("Level "+str(goalindex+1), white, int((WIDTH*BLOCKSIZE*SCALE)/2), int(((HEIGHT-1)*BLOCKSIZE*SCALE)/2)-20, 20)
        message("That guy is on fire!", white, int((WIDTH*BLOCKSIZE*SCALE)/2), int(((HEIGHT+2)*BLOCKSIZE*SCALE)/2)-20, 20)
    if PAUSE:
        message("PAUSE", white, int((WIDTH*BLOCKSIZE*SCALE)/2), 20, 20)
    display()
