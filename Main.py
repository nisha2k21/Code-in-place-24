from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Milestone #1: Set up the World
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')
    goal_x = 360
    goal_y = 360
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + SIZE, goal_y + SIZE, 'red')
    
    # Initial direction is to the right
    direction = 'Right'
    
    # Animation loop
    while True:
        # Milestone #3: Handle Key Press
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
            direction = 'Left'
        elif key == 'ArrowRight':
            direction = 'Right'
        elif key == 'ArrowUp':
            direction = 'Up'
        elif key == 'ArrowDown':
            direction = 'Down'
        
        # Milestone #2: Animate
        if direction == 'Left':
            canvas.move(player, -SIZE, 0)
        elif direction == 'Right':
            canvas.move(player, SIZE, 0)
        elif direction == 'Up':
            canvas.move(player, 0, -SIZE)
        elif direction == 'Down':
            canvas.move(player, 0, SIZE)
        
        # Milestone #4: Detecting collisions
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        
        if (player_x < 0 or player_x >= CANVAS_WIDTH or 
            player_y < 0 or player_y >= CANVAS_HEIGHT):
            print("Game Over!")
            break
        
        # Milestone #5: Moving the goal
        goal_x = canvas.get_left_x(goal)
        goal_y = canvas.get_top_y(goal)
        if player_x == goal_x and player_y == goal_y:
            goal_x = random.randint(0, (CANVAS_WIDTH // SIZE) - 1) * SIZE
            goal_y = random.randint(0, (CANVAS_HEIGHT // SIZE) - 1) * SIZE
            canvas.moveto(goal, goal_x, goal_y)
        
        # Sleep to control the animation speed
        time.sleep(DELAY)

if __name__ == '__main__':
    main()

