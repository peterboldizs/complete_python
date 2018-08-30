from unittest import TestCase
from unittest.mock import patch, call
from nose.tools import assert_equal, assert_list_equal
from ch7a_filter.filter_func import filter_ints, is_positive


class FilterIntsTestCase(TestCase):

    @patch('filter_func.is_positive')
    def test_filter_ints(self, is_positive_mock):
        v = [3, -4, 0, 5, 8]
        filter_ints(v)
        assert_equal(
            [call(3), call(-4), call(0), call(5), call(8)],
            is_positive_mock.call_args_list
        )

    def test_filter_ints_return(self):
        v1 = [3, -4, 0, -2, 5, 0, 8, -1]
        v2 = [7, -4, 0, -2, 3, 1]

        assert_list_equal([3, 5, 8], filter_ints(v1), "these list are not identical")
        assert_list_equal([7, 3, 1], filter_ints(v2), "these list are not identical")

    def test_is_positive(self):
        assert_equal(True, is_positive(2))
        assert_equal(False, is_positive(0))
        assert_equal(False, is_positive(-2))