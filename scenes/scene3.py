from manim import ArcBetweenPoints, MoveAlongPath, Text, MathTex, FadeIn, FadeOut, Transform, PI, RIGHT, LEFT, UP
import numpy as np
from constants import *
from intial import Intial

class Scene3:
    def __init__(self):
        self.intial = Intial()
        self.computed_c_values = self.intial.returnComputedCAsArray()
        self.temp_computed_c_values = []
        self.text_c_value_list = []
        self.entry_a_values = np.array(MATRIX_A_NUMBERS.copy())
        self.entry_b_values = np.array(MATRIX_B_NUMBERS.copy())
        
    def moveAValuesAcross(self, matrix, row):
        """Move Aij values across the matrix

        Args:
            matrix (VGroup): matrix used in the scene
            row (int): index of the row to move the values across

        Returns:
            list: list of animations that move each Aij value across the matrix
        """
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
        
        #Store the values in a temporary array
            temp_a_values[(col - 1) % MATRIX_ROW_COL_CT] = self.entry_a_values[intial_entry]
        
        for col in range(MATRIX_ROW_COL_CT):
            self.entry_a_values[row * MATRIX_ROW_COL_CT + col] = temp_a_values[col]

        return move_animations
            
    def moveBValuesUp(self, matrix, col):
        """Move Bij values up the matrix

        Args:
            matrix (VGroup): matrix used in the scene
            col (int): index of the column to move the values up

        Returns:
            list: list of animations that move each Bij value up the matrix
        """
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
        
        #Store the values in a temporary array
            temp_b_values[(row - 1) % MATRIX_ROW_COL_CT] = self.entry_b_values[intial_entry]
        
        for row in range(MATRIX_ROW_COL_CT):
            self.entry_b_values[row * MATRIX_ROW_COL_CT + col] = temp_b_values[row]
            
        return move_animations
    
    def computeCValues(self, matrix):
        """Compute the temporary Cij values (Aij * Bij) and add them to the computed Cij (new temp Cij + prev. Cij) values

        Args:
            matrix (VGroup): matrix used in the scene

        Returns:
            list: intial fade in animations for multi sign
            list: final fade in animations for computed temp C values
            list: intial move animations for Aij and Bij values to multi sign
            list: final move animations for computed temp C values to final position
            list: intial fade out animations for multi sign, Aij and Bij values
            list: final fade out animations for computed temp Cij values
            list: transform animations for computed temp Cij values to final temp Cij value
        """
        intial_move_animations = []
        final_move_animations = []
        intial_fade_in_animations = []
        final_fade_in_animations = []
        intial_fade_out_animations = []
        final_fade_out_animations = []
        transform_animations = []
        
        self.temp_computed_c_values = self.entry_a_values * self.entry_b_values
        self.computed_c_values += self.temp_computed_c_values
        for row in range(MATRIX_ROW_COL_CT):
            for col in range(MATRIX_ROW_COL_CT):
                entry = col + (row * MATRIX_ROW_COL_CT)
                text_c_value = Text(str(self.computed_c_values[entry]), color=C_VALUES_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center())
                text_temp_c_value = Text(str(self.temp_computed_c_values[entry]), color=C_VALUES_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center())
                self.text_c_value_list.append(text_temp_c_value)
                
                aij_value = Text(str(self.entry_a_values[entry]), color=MATRIX_A_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center()).shift(LEFT * 0.3 + UP * 0.3)
                bij_value = Text(str(self.entry_b_values[entry]), color=MATRIX_B_COLOR, font_size=MATRIX_FONT_SIZE).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center()).shift(RIGHT * 0.3 + UP * 0.3)
                multi_sign = MathTex('\\times', color=MATRIX_A_COLOR).scale(0.65).move_to(matrix[entry][MATRIX_C_BOX_VGROUP].get_center())
                
                intial_fade_in_animations.append(FadeIn(multi_sign))
                
                intial_move_animations.append(aij_value.animate.move_to(multi_sign.get_center()))
                intial_move_animations.append(bij_value.animate.move_to(multi_sign.get_center()))
                
                final_fade_in_animations.append(FadeIn(text_temp_c_value))
                
                final_move_animations.append(text_temp_c_value.animate.move_to(matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP].get_center()))
                
                transform_animations.append(Transform(matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP], text_c_value.move_to(matrix[entry][MATRIX_C_ENTRY_COMPUTED_C_VGROUP].get_center())))
                
                intial_fade_out_animations.append(FadeOut(multi_sign))
                intial_fade_out_animations.append(FadeOut(aij_value))
                intial_fade_out_animations.append(FadeOut(bij_value))
                
                final_fade_out_animations.append(FadeOut(text_temp_c_value))
                
        return intial_fade_in_animations, final_fade_in_animations, intial_move_animations, final_move_animations, intial_fade_out_animations, final_fade_out_animations, transform_animations
                