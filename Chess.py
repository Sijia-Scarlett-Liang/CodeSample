
'''
Welcome to Gobang World

'''
import Track
import tkinter
import math


class Chess_Board_Canvas(tkinter.Canvas):
	"""
	Chess_Board_Canvas: design the chessboard by using tkinter.Canvas 
	"""
	def __init__(self, target=None, height=0, width=0):
		"""
		Initializing the chessboard by drawing points and grids.

		Attributes:
		target: a drawing object. It uses to add the title of the frame. 
		height: an integer that stands for the height of canvas.
		width: an integer that stands for the width of canvas.
        Track_Record: track the chessbroad status.

        Then, draw points and grids on the canvas.
		"""
		tkinter.Canvas.__init__(self, target, height=height, width=width)
		self.Track_Record = Track.Track_Record()
		self.draw_points()   #draw points on canvas
		self.draw_canvas()   #draw grids on canvas

	def draw_points(self):
		"""
		draw_points: define points on the coordinate of canvas
		"""
		self.chess_points = [[None for i in range(15)] for j in range(15)]

		for i in range(15):
			for j in range(15):
				self.chess_points[i][j] = Track.Point(i, j); 

	def draw_canvas(self):
		"""
		draw_canvas: define grids on canvas by using pixel coordinates.
		"""
		for i in range(15):  #draw vertical lines
			self.create_line(self.chess_points[i][0].pixel_x, self.chess_points[i][0].pixel_y, self.chess_points[i][14].pixel_x, self.chess_points[i][14].pixel_y)

		for j in range(15):  #draw horizontal lines
			self.create_line(self.chess_points[0][j].pixel_x, self.chess_points[0][j].pixel_y, self.chess_points[14][j].pixel_x, self.chess_points[14][j].pixel_y)
	

	def place_chess(self, click_place): 
		"""
		place_chess: validating the clicks. 
		
		Attributes:
		click_place: the mouse-get coordinate (x, y) on canvas. 

		step 1: Find a coordinate that the euclidean distance with the mouse-get locaton is less that 180. 
		checking if such cooridinate on chessbroad grid is empty.
		(a)if the step number is odd, place a white chess next.
		(b)if the step number is even, place a black chess next.
		step 2: updating the chess information on its color and the current step number. 
		step 3: check the win conditions. If the win conditions are satisfied, 
		print win message and stop the action of clicking.
		"""

		for i in range(15):
			for j in range(15):
				square_distance = math.pow((click_place.x - self.chess_points[i][j].pixel_x), 2) + math.pow((click_place.y - self.chess_points[i][j].pixel_y), 2)
	
				if (square_distance <= 180) and (not self.Track_Record.has_record(i, j)):
				 	##step 1 (a)
					if self.Track_Record.player() == 1:
						self.create_oval(self.chess_points[i][j].pixel_x-10, self.chess_points[i][j].pixel_y-10, self.chess_points[i][j].pixel_x+10, self.chess_points[i][j].pixel_y+10, fill='snow')
					##step 1 (b)
					elif self.Track_Record.player() == 2:
						self.create_oval(self.chess_points[i][j].pixel_x-10, self.chess_points[i][j].pixel_y-10, self.chess_points[i][j].pixel_x+10, self.chess_points[i][j].pixel_y+10, fill='gray1')
					##step 2
					self.Track_Record.insert_record(i, j)
					##step 3
					result = self.Track_Record.check()
					if result == 1:
						self.create_text(240, 550, text='the black wins')
						self.unbind('<Button-1>')
					elif result == 2:
						self.create_text(240, 550, text='the white wins')
						self.unbind('<Button-1>')


class Chess_Board_Frame(tkinter.Frame):
	"""
	Chess_Board_Frame: the master of widget that groups other widgets. It displays all activities. 
	"""
	def __init__(self, target=None):
		"""
		Define a frame which is the master of widget.
		Group the other widgets via the function create_widgets().
		"""
		tkinter.Frame.__init__(self, target)
		self.create_widgets()

	def create_widgets(self):
		"""
		Step 1: define the frame title
		Step 2: call the defined canvas
		Step 3: enable the click action to retrieve location information from the canvas 
		and pass it to the function, chess_board_canvas.place_chess. The button clicking will 
		stay active until one of the win conditions is satisfied. 

		"""
		self.chess_board_label_frame = tkinter.LabelFrame(self, text="Welcome to Gobang World", padx=10, pady=10) #step 1
		self.chess_board_canvas = Chess_Board_Canvas(self.chess_board_label_frame, height=600, width=600) #step 2
        
		self.chess_board_canvas.bind('<Button-1>', self.chess_board_canvas.place_chess) #step 3
        
		self.chess_board_label_frame.pack();
		self.chess_board_canvas.pack();
