import pytest
from mymath import *

@pytest.mark.parametrize("x,y,val",[(1,1,0.7080734182735712),(5,0.25,-0.18979332974154567)])
def test_sinc2d_regression(x,y,val):
    assert abs(sinc2d(x,y)-val) < 1e-10