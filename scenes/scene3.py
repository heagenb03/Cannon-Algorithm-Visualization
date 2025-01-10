from manim import ArcBetweenPoints, MoveAlongPath, PI
import numpy as np
from constants import *
from intial import Intial

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.entry_a_values = np.array(MATRIX_A_NUMBERS.copy())
        self.entry_b_values = np.array(MATRIX_B_NUMBERS.copy())
        
    def moveAValuesAcross(self, matrix, row):
        move_animations = []
        temp_a_values = [None] * MATRIX_ROW_COL_CT
        
        for col in range(MATRIX_ROW_COL_CT):
            #First column
            if col == 0:
                intial_entry = row * MATRIX_ROW_COL_CT
                final_point_entry = (row * MATRIX_ROW_COL_CT) + (MATRIX_ROW_COL_CT - 1)
            #Rest of the columns
            else:
                intial_entry = row * MATRIX_ROW_COL_CT + col
                final_point_entry = row * MATRIX_ROW_COL_CT + (col - 1)
                
            arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_A_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_A_VGROUP], arcPath))
            
            temp_a_values[(col - 1) % MATRIX_ROW_COL_CT] = self.entry_a_values[intial_entry]
        
        for col in range(MATRIX_ROW_COL_CT):
            self.entry_a_values[row * MATRIX_ROW_COL_CT + col] = temp_a_values[col]

        return move_animations
            
    def moveBValuesUp(self, matrix, col):
        move_animations = []
        temp_b_values = [None] * MATRIX_ROW_COL_CT
        
        for row in range(MATRIX_ROW_COL_CT):
            #First Row
            if row == 0:
                intial_entry = col
                final_point_entry = col + (MATRIX_ROW_COL_CT * (MATRIX_ROW_COL_CT - 1))
            #Rest of the rows
            else:
                intial_entry = col + (row * MATRIX_ROW_COL_CT)
                final_point_entry = col + ((row - 1) * MATRIX_ROW_COL_CT)
            
            arcPath = ArcBetweenPoints(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), matrix[final_point_entry][MATRIX_C_ENTRY_B_VGROUP].get_center(), angle=PI/2)
            move_animations.append(MoveAlongPath(matrix[intial_entry][MATRIX_C_ENTRY_B_VGROUP], arcPath))
        
            temp_b_values[(row - 1) % MATRIX_ROW_COL_CT] = self.entry_b_values[intial_entry]
        
        for row in range(MATRIX_ROW_COL_CT):
            self.entry_b_values[row * MATRIX_ROW_COL_CT + col] = temp_b_values[row]
            
        return move_animations