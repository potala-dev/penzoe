from test_plus.test import TestCase as PlustTestCase

from penzoe.users.tests.factories import UserFactory


class TestCase(PlustTestCase):
    """A base test case class."""

    user_factory = UserFactory
