import pygame, sys
import random
def generateState( cellsX, cellsY, state ):
	for line in range( cellsY ):
		state.append( [ ] )
		for cell in range( cellsX ):
			state[ line ].append( random.randint(0, 1) )

def generateImage( screen, cellsX, cellsY, cellSize, notActive, state ):
	for y in range( cellsY ):
		for x in range( cellsX ):
			poly = [ ( ( x ) 	   * cellSize, ( y ) 	 * cellSize ),
					 ( ( x ) 	   * cellSize, ( y + 1 ) * cellSize ),
					 ( ( x + 1 ) * cellSize,   ( y ) 	 * cellSize ),
					 ( ( x + 1 ) * cellSize,   ( y + 1 ) * cellSize )]

			if( state[ y ][ x ] == 0 ):
				pygame.draw.polygon( screen, notActive, poly, 0 )

def main():

	# start pygame
	pygame.init()

	# -| Colors |-

	bg = ( 220, 220, 220 )
	border = ( 160, 160, 160 )
	notActive = ( 92, 92, 92 )
	outline = ( 25, 102, 255 )

	# -| screen |-

	cellsX, cellsY = 10, 6
	cellSize = 100
	size = ( cellsX * cellSize, cellsY * cellSize )
	screen = pygame.display.set_mode( size )

	screen.fill( bg )
	pygame.display.set_caption('Marching squares algorithm')

	# -| State |-
	state = [ ]

	generateState( cellsX, cellsY, state )

	generateImage( screen, cellsX, cellsY, cellSize, notActive, state )

	# -| Actualizar screen |-
	pygame.display.flip()

	for line in state:
		print( line )

	while( True ):
		for event in pygame.event.get():
			if( event.type == pygame.QUIT ):
				sys.exit()


if __name__ == '__main__':

	main()