import pygame
	
class Board:
	def __init__(self):
		self.screen = pygame.display.set_mode((1000, 820))
		self.background = pygame.image.load("res/board.jpg")
		gobanIcon = pygame.transform.scale(
			pygame.image.load("res/icon.png"), (20, 20))
		self.blackStone = pygame.transform.scale(
			pygame.image.load("res/black.png"), (38, 38))
		self.whiteStone = pygame.transform.scale(
			pygame.image.load("res/white.png"), (38, 38))
		pygame.display.set_caption("围棋")
		pygame.display.set_icon(gobanIcon)
		pygame.mixer.init(44100, -16, 1, 512)
		self.sounds = {}
		self.sounds["move"] = pygame.mixer.Sound("sound/move.wav")

		self.posX = 40
		self.posY = 40
		self.tileSize = 40
		self.htileSize = 20
		self.starSize = 5
		self.width = 19
		self.height = 19
		self.blackTurn = 1
		self.colors = {
			"BLACK": (0, 0, 0),
			"WHITE": (255, 255, 255)
		}
		self.tiles = [[0 for i in range(self.width)] for i in range(self.height)]

		self.mainLoop()

	def mainLoop(self):
		clock = pygame.time.Clock()
		run = True

		while run:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False
				if event.type == pygame.MOUSEBUTTONUP:
					self.getDown(event)

			self.screen.blit(self.background, (0, 0))
			self.drawBoard()
			self.drawStars()
			self.drawStones()
			pygame.display.update()

		pygame.quit()

	def drawBoard(self):
		for x in range(0, self.width):
			for y in range(0, self.height):
				pygame.draw.line(self.screen, self.colors["BLACK"],
								 (self.posX + x * self.tileSize, self.posY + y * self.tileSize), (self.posX + x * self.tileSize, self.posY + y))
				pygame.draw.line(self.screen, self.colors["BLACK"],
								 (self.posX + x * self.tileSize, self.posY + y * self.tileSize), (self.posX + x, self.posY + y * self.tileSize))

	def drawStars(self):
		starLocation = [3, 9, 15]
		for x in starLocation:
			for y in starLocation:
				pos = (int(self.posX + x*self.tileSize), int(self.posY + y*self.tileSize))
				pygame.draw.circle(self.screen, self.colors["BLACK"], pos, self.starSize)

	def drawStones(self):
		for x in range(0, self.width):
			for y in range(0, self.height):
				if self.tiles[x][y] == 1:
					pos = (int(self.posX + x*self.tileSize) - 19, int(self.posY + y*self.tileSize) - 19)
					self.screen.blit(self.blackStone, pos)
				if self.tiles[x][y] == -1:
					pos = (int(self.posX + x*self.tileSize) - 19, int(self.posY + y*self.tileSize) - 19)
					self.screen.blit(self.whiteStone, pos)

	def getPos(self, pos):
		adjustX = pos[0] - self.posX + self.htileSize
		adjustY = pos[1] - self.posY + self.htileSize
		if adjustX >= 760 or adjustY >= 760:
			return (-1, -1)
		mouseX = int(adjustX / self.tileSize)
		mouseY = int(adjustY / self.tileSize)
		return (mouseX, mouseY)

	def getDown(self, event):
		x, y = self.getPos(event.dict['pos'])
		if x < 0 or y < 0:
			return
		if self.tiles[x][y] != 0:
			return
		else:
			self.tiles[x][y] = self.blackTurn
			self.blackTurn = -self.blackTurn
			self.sounds["move"].play()

def main():
	game = Board()

if __name__ == '__main__':
	main()