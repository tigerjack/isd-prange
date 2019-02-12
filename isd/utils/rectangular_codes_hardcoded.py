import numpy as np
import logging

_logger = logging.getLogger(__name__)


def get_isd_systematic_parameters(n, k, d, w):
    """Given the input parameters, returns the corresponding isd hardcoded
    parameters (if they are present)

    :param n: 
    :param k: 
    :param d: 
    :param w: 
    :returns: 
    :rtype: 

    """
    if (n, k, d, w) == (4, 1, 4, 1):
        return _get_4_1_4_w1()
    elif (n, k, d, w) == (7, 4, 3, 1):
        return _get_7_4_3_w1()
    elif (n, k, d, w) == (15, 11, 4, 1):
        return _get_15_11_4_w1()
    elif (n, k, d, w) == (8, 4, 4, 1):
        return _get_8_4_4_w1()
    else:
        raise AttributeError("Combination not supported yet.")


def _get_4_1_4_w1():
    h = get_systematic_h(4, 1, 4)
    g = get_systematic_g(4, 1, 4)
    isHamming = False
    syndromes = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
    errors = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    w = 1
    return h, g, syndromes, errors, w, isHamming


def _get_8_4_4_w1():
    h = get_systematic_h(8, 4, 4)
    g = get_systematic_g(8, 4, 4)
    # TODO
    syndromes = np.array([[1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1],
                          [0, 1, 1, 1]])
    errors = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
    ])
    w = 1
    isHamming = False
    return h, g, syndromes, errors, w, isHamming


def _get_7_4_3_w1():
    h = get_systematic_h(7, 4, 3)
    g = get_systematic_g(7, 4, 3)
    w = 1
    isHamming = True
    syndromes = np.array([
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ])
    errors = np.array([
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
    ])
    return h, g, syndromes, errors, w, isHamming


def _get_15_11_4_w1():
    h = get_systematic_h(15, 11, 4)
    g = get_systematic_g(15, 11, 4)
    w = 1
    isHamming = True
    syndromes = np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0],
         [0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1],
         [1, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 0, 1]])
    errors = np.array([
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
    ])
    return h, g, syndromes, errors, w, isHamming


def get_systematic_g(n, k, d):
    if (n, k, d) == (4, 1, 4):
        return _get_4_1_4_systematic_g()
    elif (n, k, d) == (9, 4, 4):
        return _get_9_4_4_systematic_g()
    elif (n, k, d) == (15, 11, 4):
        return _get_15_11_4_systematic_g()
    elif (n, k, d) == (7, 4, 3):
        return _get_7_4_3_systematic_g()
    elif (n, k, d) == (8, 4, 4):
        return _get_8_4_4_systematic_g()
    else:
        raise AttributeError(
            "[{0}, {1}, {2}] parity matrix not yet implemented".format(
                n, k, d))


def _get_4_1_4_systematic_g():
    return np.array([[1, 1, 1, 1]])


def _get_8_4_4_systematic_g():
    g = np.array([
        [1., 0., 0., 0., 1., 1., 1., 0.],
        [0., 1., 0., 0., 1., 0., 1., 1.],
        [0., 0., 1., 0., 1., 1., 0., 1.],
        [0., 0., 0., 1., 0., 1., 1., 1.],
    ])
    return g


def _get_9_4_4_systematic_g():
    """
    Get a fixed generator matrix G for the [9, 4, 4] code
    """
    g = np.array([
        [1., 0., 0., 0., 1., 0., 1., 0., 1.],
        [0., 1., 0., 0., 1., 0., 0., 1., 1.],
        [0., 0., 1., 0., 0., 1., 1., 0., 1.],
        [0., 0., 0., 1., 0., 1., 0., 1., 1.],
    ])
    return g


def _get_7_4_3_systematic_g():
    """
    Get a fixed systematic G matrix for a [7, 4, 3] code, i.e. the matrix
    [[1 0 0 0 ], [0 1 0 0], [0 0 1 0], [0 0 0 1], [1 1 0 1], [1 0 1 1], [0 1 1 1]].T
    """
    # g = np.array([[1., 0., 0., 0., 1., 1., 0.], [0., 1., 0., 0., 1., 0., 1.],
    #               [0., 0., 1., 0., 0., 1., 1.], [0., 0., 0., 1., 1., 1., 1.]])
    g = np.array([
        [1., 0., 0., 0., 1., 1., 1.],
        [0., 1., 0., 0., 1., 0., 1.],
        [0., 0., 1., 0., 1., 1., 0.],
        [0., 0., 0., 1., 0., 1., 1.],
    ])
    return g


def _get_15_11_4_systematic_g():
    g = np.array([
        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0.],
        [0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0.],
        [0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1.],
        [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 1.],
        [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0.],
        [0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1., 0., 1.],
        [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 1., 0.],
        [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 1., 1., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1., 1., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 1., 1.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 0., 0., 1.],
    ])
    return g


def get_systematic_h(n, k, d):
    if (n, k, d) == (4, 1, 4):
        return _get_4_1_4_systematic_h()
    elif (n, k, d) == (7, 4, 3):
        return _get_7_4_3_systematic_h()
    elif (n, k, d) == (9, 4, 4):
        return _get_9_4_4_systematic_h()
    elif (n, k, d) == (15, 11, 4):
        return _get_15_11_4_systematic_h()
    elif (n, k, d) == (8, 4, 4):
        return _get_8_4_4_systematic_h()
    else:
        raise AttributeError(
            "[{0}, {1}, {2}] parity matrix not yet implemented".format(
                n, k, d))


def _get_4_1_4_systematic_h():
    h = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]).T
    return h


def _get_15_11_4_systematic_h():
    hz = np.array([
        [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    ])
    return hz


def _get_8_4_4_systematic_h():
    h = np.array([[1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 1],
                  [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]).T
    return h


def _get_7_4_3_systematic_h():
    h = np.array([
        [1, 1, 1, 0, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 0, 0, 1],
    ])
    return h


def _get_9_4_4_systematic_h():
    h = np.array([
        [1., 1., 0., 0., 1., 0., 0., 0., 0.],
        [0., 0., 1., 1., 0., 1., 0., 0., 0.],
        [1., 0., 1., 0., 0., 0., 1., 0., 0.],
        [0., 1., 0., 1., 0., 0., 0., 1., 0.],
        [1., 1., 1., 1., 0., 0., 0., 0., 1.],
    ])
    return h
