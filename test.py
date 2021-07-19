"""Unit Tests for Student Submission"""
import matplotlib.pyplot as plt
import matplotlib.testing.compare as test
import numpy as np
from PIL import Image
import unittest
# import student_solution


class Test(unittest.TestCase):
    def test_JandJ(self):
        correct = Image.open('./solutions/JandJ_solution.png')
        student = Image.open('./images/jj_earnings.png')
        correct_arr = np.asarray(correct)
        student_arr = np.asarray(student)
        rms_value = test.calculate_rms(correct_arr, student_arr)
        self.assertTrue(rms_value <= 10)

    def test_BNV(self):
        correct = Image.open('./solutions/BVN_solution.png')
        student = Image.open('./images/bivariate_normal_plot.png')
        correct_arr = np.asarray(correct)
        student_arr = np.asarray(student)
        rms_value = test.calculate_rms(correct_arr, student_arr)
        self.assertTrue(rms_value <= 10)

    def test_ABV(self):
        correct = Image.open('./solutions/faceting_solution.png')
        student = Image.open('./images/ABV_histograms.png')
        correct_arr = np.asarray(correct)
        student_arr = np.asarray(student)
        rms_value = test.calculate_rms(correct_arr, student_arr)
        self.assertTrue(rms_value <= 10)

    def test_ABV(self):
        correct = Image.open('./solutions/subplots_solution.png')
        student = Image.open('./images/normally_distributed_wave.png')
        correct_arr = np.asarray(correct)
        student_arr = np.asarray(student)
        rms_value = test.calculate_rms(correct_arr, student_arr)
        self.assertTrue(rms_value <= 10)

    

if __name__ == "__main__":
    unittest.main()