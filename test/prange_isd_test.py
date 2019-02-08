import numpy as np
from isd import prange_isd
import unittest
import test.utils
from test.ISDTest import ISDTest
from parameterized import parameterized


class PrangeISDTest(ISDTest):
    @parameterized.expand([
        ("n7_k4_d3_w1", 7, 4, 3, 1),
        ("n15_k11_d4_w1", 15, 11, 4, 1),
    ])
    def test_h_s_d_w(self, name, n, k, d, w):
        h, syndromes, errors, w = test.utils.get_parameters(n, k, d, w)
        p = np.random.permutation(np.eye(h.shape[1]))
        h_p = np.dot(h, p)
        errors_p = np.dot(errors, p)
        for i, s in enumerate(syndromes):
            with self.subTest(h=h_p, s=s, w=w):
                self.logger.debug("Launching prange with s = {0}".format(s))
                e = prange_isd.isd(h_p, s, w)
                self.logger.debug(
                    "For s = {0}, w = 1, h = \n{1}\nerror is {2}".format(
                        s, h_p, e))
                np.testing.assert_array_almost_equal(e, errors_p[i])


if __name__ == '__main__':
    unittest.main()
