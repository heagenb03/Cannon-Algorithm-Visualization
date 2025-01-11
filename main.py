from manim import Scene, VGroup, MathTex, FadeIn, FadeOut, LEFT, RIGHT, ORIGIN
import sys
sys.path.insert(0, 'scenes')

from constants import *
from scenes.scene1 import Scene1
from scenes.scene2 import Scene2
from scenes.scene3 import Scene3

class Cannon(Scene):
    def construct(self):
        scene1 = Scene1()
        scene2 = Scene2()
        scene3 = Scene3()
        
        """
        Scene 1 
            #1. Create Matrix A, B, C
            #2. Move Aij & Bij values to corresponding Cij values / Fadeout Matrix A & B
        """
        
        #1        
        multi_sign = MathTex("\\times")
        equal_sign = MathTex("=")
        
        matrixA_scene1 = scene1.createMatrixA()
        matrixB_scene1 = scene1.createMatrixB()
        matrixC_scene1 = scene1.createMatrixC()
        algorithm_title = scene1.createTitle()
        
        matrices = VGroup(
            matrixC_scene1,
            equal_sign,
            matrixB_scene1,
            multi_sign,
            matrixA_scene1
        ).arrange(LEFT, buff=MATRIX_BUFFER*2)
        
        matrices.move_to(ORIGIN)
        
        self.add(algorithm_title)
        self.play(FadeIn(matrices))
        self.wait(5)
        
        #2
        move_animations = scene1.moveEnteriesToMatrixC(matrixA_scene1, matrixB_scene1, matrixC_scene1)
        self.play(*move_animations)
        self.wait(0.5)
        
        partial_matrixC_scene = scene1.createPartialMatrixC()
        
        self.play(FadeOut(matrices),
                FadeIn(partial_matrixC_scene.shift(RIGHT * scene1.RIGHT_ALINGMENT))
        )
        self.wait(0.5)
        
        """
        Scene 2 
            1. Move Matrix C to center
            2. Realign Matrix C for future animation purposes
        """
        
        #1
        matrixC_scene2 = scene2.createMatrixC()


        move_animations = scene2.moveMatrixCtoCenter(matrixB_scene1, partial_matrixC_scene)
        self.play(*move_animations)
        self.play(FadeOut(partial_matrixC_scene),
                FadeIn(matrixC_scene2.shift(RIGHT * scene2.RIGHT_ALINGMENT))
        )
        
        #2
        adjust_animations = scene2.realignMatrixC(matrixC_scene2)
        self.play(*adjust_animations)
        
        self.wait(1)
        
        """
        Scene 3
            1. Move correspodning Aij values across the matrix
            2. Move correspodning Bij values across the matrix
            3. Compute Cij values
            4. Move all Aij values accross the matrix
            5. Move all Bij values up the matrix
        """
        #1
        for row in range(1, MATRIX_ROW_COL_CT):
            for count in range(row):
                move_animations = scene3.moveAValuesAcross(matrixC_scene2, row)
                self.play(*move_animations)
                self.wait(0.25)
        
        #2
        for col in range(1, MATRIX_ROW_COL_CT):
            for count in range(col):
                move_animations = scene3.moveBValuesUp(matrixC_scene2, col)
                self.play(*move_animations)
                self.wait(0.25)
        self.wait(1)
        
        shift_count = 0
        while shift_count < MATRIX_ROW_COL_CT:
            #3
            scene3.text_c_value_list = []
            scene3.temp_computed_c_values = []
            
            intial_fade_in_animations, final_fade_in_animations, intial_move_animations, final_move_animations, intial_fade_out_animations, final_fade_out_animations, transform_animations = scene3.computeCValues(matrixC_scene2)
            
            self.play(*intial_fade_in_animations)
            self.wait(1)
            self.play(*intial_move_animations)
            self.wait(0.15)
            self.play(*final_fade_in_animations,
                    *intial_fade_out_animations)
            self.wait(1)
            self.play(*final_move_animations)
            self.wait(0.5)
            self.play(*transform_animations,
                    *final_fade_out_animations)
            self.wait(2)
            
            
            if shift_count != MATRIX_ROW_COL_CT - 1:
                #4
                total_move_animations = []
                for row in range(MATRIX_ROW_COL_CT):
                    move_animations = scene3.moveAValuesAcross(matrixC_scene2, row)
                    total_move_animations.extend(move_animations)
                    
                self.play(*total_move_animations)
                self.wait(1)
                
                #5
                total_move_animations = []
                for col in range(MATRIX_ROW_COL_CT):
                    move_animations = scene3.moveBValuesUp(matrixC_scene2, col)
                    total_move_animations.extend(move_animations)
                
                self.play(*total_move_animations)
                self.wait(1)
            
            shift_count += 1
            
        """
        Scene 4
        """