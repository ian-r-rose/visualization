"""
Regression tests for 2D advection on an annulus.
"""

import sys
import unittest

import clawpack.classic.test as test


class Advection2DAnnulusTest(test.ClassicRegressionTest):
    r"""Basic test for a 2D advection test case"""


    def runTest(self, save=False):

        # Write out data files
        self.load_rundata()
        self.write_rundata_objects()

        # Run code
        self.run_code()

        # Perform tests
        self.check_frame(save=save, frame_num=1,
                         regression_data_path='regression_data_test2.txt')
        self.check_frame(save=save, frame_num=2,
                         regression_data_path='regression_data_test3.txt')

        self.success = True



if __name__=="__main__":
    if len(sys.argv) > 1:
        if bool(sys.argv[1]):
            # Fake the setup and save out output
            test = Advection2DAnnulusTest()
            try:
                test.setUp()
                test.runTest(save=True)
            finally:
                test.tearDown()
            sys.exit(0)
    unittest.main()