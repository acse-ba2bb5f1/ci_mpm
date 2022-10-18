import pytest

import numpy as np

from simple_functions.trig_functions import my_sin


class TestTrigFunctions(object):
    '''Class to test our trigonometric functions are working correctly'''

    @pytest.mark.parametrize('number, expected', [
        (0, 0),
        (np.pi/2, 1),
        (-np.pi/2, -1)
    ])
    def test_my_sin(self, number, expected):
        '''Test our sin function'''
        answer = my_sin(number)
        assert answer == expected
