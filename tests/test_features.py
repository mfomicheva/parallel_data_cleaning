from features.length_absolute_difference import LengthAbsoluteDifference
from features.mismatch_numbers_identity import MismatchNumbersIdentity
from features.mismatch_numbers_count import MismatchNumbersCount


def test_length_absolute_difference():
    source = 'This is a test'
    target = 'Es un test'
    feature = LengthAbsoluteDifference(source, target)
    feature.run()
    assert feature.score == 1.


def test_mismatch_number_identity():
    source = 'This is the test 1'
    target = 'Es un test 2'
    feature = MismatchNumbersIdentity(source, target)
    feature.run()
    assert feature.score == 0.2222222222222222


def test_mismatch_number_count():
    source = 'This is the test 1'
    target = 'Es un test 2'
    feature = MismatchNumbersCount(source, target)
    feature.run()
    assert feature.score == 0.
