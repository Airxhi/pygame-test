import pygame, math, sys, random


def rotate(x, y, theta):
    return x * math.cos(theta) + y * math.sin(theta), -x * math.sin(theta) + y * math.cos(theta)


class Game:
    screen = None
    running = False
    car = None
    map = None

    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.get_surface()
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Test driving game")

    def get_point_list(self, i, points):
        p1 = (i * 100 - self.car.getX(), points[i]*400 + 100)
        p2 = (i * 100 - self.car.getX(), points[i]*400 + 200)
        p3 = ((i+1) * 100 - self.car.getX(), points[i + 1]*400 + 100)
        p4 = ((i+1) * 100 - self.car.getX(), points[i + 1]*400 + 200)
        return [p1, p2, p4, p3]

    def draw_map(self):
        points = self.map.get_points()
        for i in range(len(points) - 1):
            pygame.draw.polygon(self.screen, (80, 80, 80),self.get_point_list(i,points))

    def draw_car(self):
        pygame.draw.polygon(self.screen, (150, 150, 150), self.car.get_poly_nox())
        # pygame.draw.rect(self.screen, (255, 0, 0), ((self.car.x - 10, self.car.y - 5), (10, 10)))

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_map()
        self.draw_car()
        pygame.display.flip()

    def start(self):
        self.__init__()
        self.initialise()
        self.running = True
        self.game_loop()

    def initialise(self):
        self.car = Car()
        self.map = Map()

    def game_loop(self):
        while self.running:
            self.do_logic()
            self.draw()

    def check_keypress(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.car.move(0.5)
        elif pressed[pygame.K_DOWN]:
            self.car.move(-0.5)
        if pressed[pygame.K_RIGHT]:
            self.car.rotate(-0.01)
        elif pressed[pygame.K_LEFT]:
            self.car.rotate(0.01)

    def do_logic(self):
        self.check_keypress()
        self.check_exit()

    def check_exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def exit_game(self):
        pygame.display.quit()
        pygame.quit()


class Car:
    x = 80  # centre x of car
    y = 80  # centre y of car
    vx = 0
    vy = 0
    theta = 0

    def move(self, n):
        self.x += n * math.cos(self.theta)
        self.y += n * -math.sin(self.theta)
        print(self.x, self.y)

    def rotate(self, delta_theta):
        self.theta += delta_theta

    def getX(self):
        return self.x

    def get_poly(self):
        x1, y1 = rotate(20, 0, self.theta)
        p1 = (self.x + x1, self.y + y1)
        x2, y2 = rotate(-20, 10, self.theta)
        p2 = (self.x + x2, self.y + y2)
        x3, y3 = rotate(-20, -10, self.theta)
        p3 = (self.x + x3, self.y + y3)
        return [p1, p2, p3]

    def get_poly_nox(self):
        x1, y1 = rotate(20, 0, self.theta)
        p1 = (300 + x1, self.y + y1)
        x2, y2 = rotate(-20, 10, self.theta)
        p2 = (300 + x2, self.y + y2)
        x3, y3 = rotate(-20, -10, self.theta)
        p3 = (300 + x3, self.y + y3)
        return [p1, p2, p3]


class Map:
    points = []

    def __init__(self):
        temp_points = []
        for i in range(100):
            temp_points.append(random.random())

        self.points.append(temp_points[0])
        for i in range(len(temp_points) - 1):
            self.points.append((temp_points[i] + temp_points[i + 1]) / 2)
        self.points.append(temp_points[len(temp_points) - 1])

    def get_points(self):
        return self.points


def main():
    game = Game()
    game.start()


main()
