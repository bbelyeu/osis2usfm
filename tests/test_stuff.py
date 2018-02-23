"""Test the OSIS to USFM conversion module."""
# pylint: disable=no-member
import unittest

from osis2usfm import convert  # isort:skip


class TestConversions(unittest.TestCase):
    """Test convert function."""

    def test_conversion(self):
        """Test the some converstions."""
        osis = ['Gen.1.1', '2Pet.1.1', 'John.1.1']
        usfms = convert(osis)
        self.assertEqual(['GEN.1.1', '2PE.1.1', 'JHN.1.1'], usfms)
