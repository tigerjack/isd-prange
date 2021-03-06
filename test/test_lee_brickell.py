import numpy as np
import unittest
from parameterized import parameterized
from test.isd_common import ISDTest
from isdclassic.methods import lee_brickell
from isdclassic.utils import rectangular_codes_hardcoded


class ISDLeeBrickellTest(ISDTest):
    @classmethod
    def setUpClass(cls):
        # Just to use prange logger
        super().setUpClass()
        import logging
        lee_logger = logging.getLogger('isdclassic.methods.lee_brickell')
        lee_logger.setLevel(cls.logger.level)
        lee_logger.handlers = cls.logger.handlers
        return
        lee_logger = logging.getLogger('isdclassic.utils.lu')
        lee_logger.setLevel(cls.logger.level)
        lee_logger.handlers = cls.logger.handlers

    @parameterized.expand([
        ("n4_k1_d4_w1_p1", 4, 1, 4, 1, 1, True),
        ("n7_k4_d3_w1_p1", 7, 4, 3, 1, 1, True),
        ("n8_k4_d4_w1_p1", 8, 4, 4, 1, 1, True),
        ("n15_k11_d3_w1_p1", 15, 11, 3, 1, 1, True),
        ("n16_k11_d4_w1_p1", 16, 11, 4, 1, 1, True),
    ])
    def test_simple_h_s_d_w_p(self, name, n, k, d, w, p, scramble):
        self.common(name, n, k, d, w, p, scramble)

    @parameterized.expand([
        ("n23_k12_d7_w3_p1", 23, 12, 7, 3, 1, True),
        ("n23_k12_d7_w3_p2", 23, 12, 7, 3, 2, True),
    ])
    @unittest.skipIf(not ISDTest.SLOW, "Skipped slow test")
    def test_slow_h_s_d_w_p(self, name, n, k, d, w, p, scramble):
        self.common(name, n, k, d, w, p, scramble)

    @parameterized.expand([
        # Quantum reference
        ("n8_k4_d4_w2_p1", 8, 4, 4, 2, 1, True),
        ("n8_k4_d4_w2_p2", 8, 4, 4, 2, 2, True),
        # Slow bcz k low & p high, unlikely to have the condition satisfied
        ("n8_k3_d4_w2_p1", 8, 3, 4, 2, 1, True),
        ("n8_k2_d5_w3_p1", 8, 2, 5, 3, 1, True),
        ("n8_k2_d5_w3_p2", 8, 2, 5, 3, 2, True),
        # Very slow
        ("n8_k1_d7_w3_p1", 8, 1, 7, 3, 1, True),
    ])
    @unittest.skipIf(not ISDTest.FAKE, "Skipped fake test")
    def test_fake_h_s_d_w_p(self, name, n, k, d, w, p, scramble):
        self.common(name, n, k, d, w, p, scramble)

    def common(self, name, n, k, d, w, p, scramble):
        # first _ is the G, we are not interested in it
        # second _ is the isHamming boolean value, not interested
        h, _, syndromes, errors, w, _ = rectangular_codes_hardcoded.get_isd_systematic_parameters(
            n, k, d, w)
        self.logger.info(
            "Launching TEST {} w/ n = {}, k = {}, d = {}, w = {}, p = {}".
            format(name, n, k, d, w, p))
        self.logger.debug("h = \n{0}".format(h))

        syndromes, errors = self.get_max_syndromes_errors(syndromes, errors)
        h_p, errors_p = self.scramble_h_errors(
            h, errors) if scramble else (h, errors)
        for i, s in enumerate(syndromes):
            with self.subTest(h=h_p, s=s, w=w, p=p):
                self.logger.info("**************")
                self.logger.info("Launching SUBTEST w/ s = {0}".format(s))
                lee = lee_brickell.LeeBrickell(h_p, s, w, p)
                e = lee.run()
                self.logger.debug(
                    "For s = {0}, w = {1}, p = {2} h = \n{3}\nerror is {4}".
                    format(s, w, p, h_p, e))
                np.testing.assert_array_almost_equal(e, errors_p[i])


if __name__ == '__main__':
    unittest.main()
