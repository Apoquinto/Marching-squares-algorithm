import pygame, sys
import random
def generateState( cellsX, cellsY, state ):
	for line in range( cellsY + 1 ):
		state.append( [ ] )
		for cell in range( cellsX + 1 ):
			state[ line ].append( random.randint(0, 1) )

def generateImage( screen, cellsX, cellsY, cellSize, notActive, state ):
	for y in range( cellsY ):
		for x in range( cellsX ):
			poly = [( ( x + 0.4 ) * cellSize, 	( y + 0.4 )     * cellSize ),
					( ( x + 0.6 ) * cellSize, ( y + 0.4 ) 	  * cellSize ),
					( ( x + 0.6 ) * cellSize, ( y + 0.6 ) * cellSize ),
					( ( x + 0.4 ) * cellSize, 	( y + 0.6 ) * cellSize ) ]
			'''
			if( state[ y ][ x ] == 0 ):
				pygame.draw.polygon( screen, notActive, poly, 0 )
			'''

def getValor( a, b, c, d ):
	return 8 * a + 4 * b + 2 * c + 1 * d

def paintLine( screen, a, b, outline ):
	pygame.draw.line(screen, outline, a, b, 2)

def marchingSquares( screen, cellsX, cellsY, cellSize, outline, state  ):
	for y in range( cellsY ):
		for x in range( cellsX ):
			val = getValor( ( state[ y ][ x ] ), 
						  ( state[ y ][ x + 1 ] ), 
						  ( state[ y + 1 ][ x + 1 ] ), 
						  ( state[ y + 1 ][ x ] ) )
			
			a = [ ( ( x ) 	  * cellSize ), 	( ( y + 0.5 ) * cellSize ) ]
			b = [ ( ( x + 0.5 ) * cellSize ), 	( ( y ) 	  * cellSize ) ]
			c = [ ( ( x + 1 ) 	  * cellSize ), ( ( y + 0.5 ) * cellSize ) ]
			d = [ ( ( x + 0.5 ) * cellSize ), 	( ( y + 1 )   * cellSize ) ]

			if val == 1: paintLine( screen, a, d, outline )
			elif val == 2: paintLine( screen, c, d, outline )
			elif val == 3: paintLine( screen, a, c, outline )
			elif val == 4: paintLine( screen, b, c, outline )
			elif val == 5: 
				paintLine( screen, a, d, outline )
				paintLine( screen, b, c, outline )
			elif val == 6: paintLine( screen, b, d, outline )
			elif val == 7: paintLine( screen, a, b, outline )
			elif val == 8: paintLine( screen, a, b, outline )
			elif val == 9: paintLine( screen, b, d, outline )
			elif val == 10: 
				paintLine( screen, a, d, outline )
				paintLine( screen, b, c, outline )
			elif val == 11: paintLine( screen, b, c, outline )
			elif val == 12: paintLine( screen, a, c, outline )
			elif val == 13: paintLine( screen, d, c, outline )
			elif val == 14: paintLine( screen, a, d, outline )

def main():

	# start pygame
	pygame.init()

	# -| Colors |-

	bg = ( 220, 220, 220 )
	border = ( 160, 160, 160 )
	notActive = ( 92, 92, 92 )
	outline = ( 25, 102, 255 )

	# -| screen |-

	cellsX, cellsY = 50, 50
	cellSize = 10
	size = ( cellsX * cellSize, cellsY * cellSize )
	screen = pygame.display.set_mode( size )

	screen.fill( bg )
	pygame.display.set_caption('Marching squares algorithm')

	# -| State |-
	state = [ ]

	generateState( cellsX, cellsY, state )

	generateImage( screen, cellsX, cellsY, cellSize, notActive, state )

	marchingSquares( screen, cellsX, cellsY, cellSize, notActive, state  )

	# -| Actualizar screen |-
	pygame.display.flip()

	while( True ):
		for event in pygame.event.get():
			if( event.type == pygame.QUIT ):
				sys.exit()

if __name__ == '__main__':

	main()