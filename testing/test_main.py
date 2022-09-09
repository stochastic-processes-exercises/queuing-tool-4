try:
    from AutoFeedback.funcchecks import check_func
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class UnitTests( unittest.TestCase ): 
   def test_rate_func(self):
      xv, yv = np.linspace( 1, 1200, 1200 ), np.zeros(1200)
      for i in range(1200) : 
          vv = xv[i] - np.floor( xv / 180 )*180
          if vv<60 : yv[i] = 0.5 
          else : yv[i] =1/6 
      assert( check_func( "rate", , ) )
