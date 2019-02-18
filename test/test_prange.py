import numpy as np
import unittest
from parameterized import parameterized
from test.isd_common import ISDTest
from isdclassic.methods import prange
from isdclassic.utils import rectangular_codes_hardcoded


class ISDPrangeTest(ISDTest):
    @classmethod
    def setUpClass(cls):
        # Just to use prange logger
        ISDTest.setUpClass()
        import logging
        prange_isd_logger = logging.getLogger('isd.methods.prange')
        prange_isd_logger.setLevel(cls.logger.level)
        prange_isd_logger.handlers = cls.logger.handlers

    @parameterized.expand([
        ("n4_k1_d4_w1", 4, 1, 4, 1, False),
        ("n7_k4_d3_w1", 7, 4, 3, 1, True),
        ("n7_k4_d3_w1", 7, 4, 3, 1, False),
        ("n8_k4_d4_w1", 8, 4, 4, 1, False),
        ("n15_k11_d4_w1", 15, 11, 4, 1, True),
        ("n16_k12_d4_w1", 16, 12, 4, 1, False),
        ("n8_k2_d4_w2", 8, 3, 4, 2, False),
        ("n8_k4_d4_w2", 8, 4, 4, 2, False),
        # SLOW
        # ("n16_k11_d7_w3", 16, 11, 7, 3, False),
        # SLOW, but correct
        # ("n23_k12_d7_w3", 23, 12, 7, 3, False),
    ])
    def test_h_s_d_w(self, name, n, k, d, w, scramble):
        # first _ is the G, we are not interested in it
        # second _ is the isHamming boolean value, not interested
        h, _, syndromes, errors, w, _ = rectangular_codes_hardcoded.get_isd_systematic_parameters(
            n, k, d, w)
        self.logger.info("n = {0}, k = {1}, d = {2}, w = {3}".format(
            n, k, d, w))
        self.logger.debug("h = \n{0}".format(h))

        if (scramble):
            p = np.random.permutation(np.eye(h.shape[1]))
            h_p = np.dot(h, p)
            errors_p = np.dot(errors, p)
        else:
            h_p = h
            errors_p = errors
        for i, s in enumerate(syndromes):
            with self.subTest(h=h_p, s=s, w=w):
                self.logger.debug("Launching prange with s = {0}".format(s))
                e = prange.run(h_p, s, w)
                self.logger.debug(
                    "For s = {0}, w = 1, h = \n{1}\nerror is {2}".format(
                        s, h_p, e))
                np.testing.assert_array_almost_equal(e, errors_p[i])


if __name__ == '__main__':
    unittest.main()
