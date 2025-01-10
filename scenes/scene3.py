from manim import ArcBetweenPoints, MoveAlongPath, PI
from constants import *
from intial import Intial

class Scene3:
    def __init__(self):
        self.intial = Intial()
    
    def moveAValuesAcross(self, matrix, row):
        move_animations = []
        for col in range(MATRIX_ROW_COL_CT):
            #First column
            if col == 0:
                intial_entry = row
                final_point_entry = row + (MATRIX_ROW_COL_CT - 1)
                
                arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), angle=PI/2)
                move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_A_VGROUP], arcPath))
            
            #Rest of the columns
            else:
                intial_entry = row
                final_point_entry = row - 1
                
                arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), angle=PI/2)
                move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_A_VGROUP], arcPath))
                    
        return move_animations
            
    def moveBValuesUp(self, matrix, col):
        move_animations = []
        for row in range(MATRIX_ROW_COL_CT):
            #First Row
            if row == 0:
                intial_entry = col
                final_point_entry = col + (MATRIX_ROW_COL_CT * (MATRIX_ROW_COL_CT - 1))
                
                arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcPath))
            
            #Rest of the rows
            else:
                intial_entry = col + (row * MATRIX_ROW_COL_CT)
                final_point_entry = col + ((row - 1) * MATRIX_ROW_COL_CT)
                
                arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
                move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcPath))
                    
        return move_animations