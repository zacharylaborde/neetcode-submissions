class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        # Initialize the game's parameters.
        self.width = width
        self.height = height
        self.food = food
        self.score = 0
        self.snake = [[0,0]]


    def move(self, direction: str) -> int:
        # STEP 1: Update the snake's position

        ## Get the new head's position.
        new_head = self.snake[-1].copy()
        if direction == "D":
            new_head[0] += 1      
        elif direction == "U":
            new_head[0] -= 1
        elif direction == "L":
            new_head[1] -= 1
        elif direction == "R":
            new_head[1] += 1
        
        ## Add the new head
        self.snake.append(new_head)
        
        ## Remove the old tail
        ### We keep it for later just in case.
        old_tail = self.snake.pop(0)
        


        # STEP 2: Collision Checking
        collision = False

        ## Check for self-collision.
        for body_part in self.snake[:-1]:
            if body_part == new_head:
                collision = True

        ## Check for wall collision.
        if new_head[0] >= self.height or new_head[0] < 0:
            collision = True
        if new_head[1] >= self.width or new_head[1] < 0:
            collision = True
        
        ## End game if snake collides with wall or self.
        if collision:
            return -1

        # 4. now we can check for collision with the
        #    apple. If the snake collides with the
        #    apple, then incrememnt the game's score.
        #    simultaneously, the snakes length should
        #    be increased by one. If there are no
        #    more apples in the apples array, then
        #    end the game by returning a -1.
        if self.score >= len(self.food):
            return self.score
        
        if new_head == self.food[self.score]:
            self.score += 1
            self.snake.insert(0, old_tail)
        
        return self.score

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
