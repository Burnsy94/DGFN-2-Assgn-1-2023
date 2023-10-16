'''
TPRG 2131 Fall 2023 Assignment 1
October, 2023
Alex Burns <100885375>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

from A_V_calc import calculate_volume_rect_prism, calculate_area_triangle, calculate_area_circle

def test_calculate_volume_rect_prism():    # code corrected by chatGPT on October 15th, 2023. Done by giving it assertion examples from lecture slides and prompting "complete the following assertions in code."
    """Test calculate_volume_rect_prism function"""
    assert calculate_volume_rect_prism(2, 3, 4) == 24
    assert calculate_volume_rect_prism(3, 2, 1) == 6
    assert calculate_volume_rect_prism(3, 2, 5) == 30
    assert calculate_volume_rect_prism(5, 4, 2) == 40

def test_calculate_area_triangle():      # code corrected by chatGPT on October 15th, 2023. Done by giving it assertion examples from lecture slides and prompting "complete the following assertions in code."
    """Test calculate_area_triangle function"""
    assert calculate_area_triangle(2, 3) == 3.0
    assert calculate_area_triangle(3, 2) == 3.0
    assert calculate_area_triangle(5, 5) == 12.5
    assert calculate_area_triangle(7, 4) == 14.0

def test_calculate_area_circle():       # code corrected by chatGPT on October 15th, 2023. Done by giving it assertion examples from lecture slides and prompting "complete the following assertions in code."
    """Test calculate_area_circle function"""
    assert abs(calculate_area_circle(2) - 12.56637061435) < 1e-10
    assert abs(calculate_area_circle(3) - 28.27433388231) < 1e-10
    assert abs(calculate_area_circle(5) - 78.53981633974) < 1e-10
    assert abs(calculate_area_circle(7) - 153.9380400259) < 1e-10


