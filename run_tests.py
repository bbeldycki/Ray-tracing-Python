from unittest import TestLoader, TextTestRunner, TestSuite
from unit_tests.functions_tests import TestFunctionMuRoots, TestFunctionPolynomialRoots, TestFunctionNodesAndWeightsGaussLegendre


if __name__ == '__main__':

    loader = TestLoader()
    tests = [loader.loadTestsFromTestCase(test) for test in (TestFunctionMuRoots, TestFunctionPolynomialRoots,
                                                             TestFunctionNodesAndWeightsGaussLegendre)]
    suite = TestSuite(tests)

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
