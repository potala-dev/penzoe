from test_plus.test import TestCase as PlustTestCase

from penzoe.book.tests.factories import BookFactory

from .factories import ProfileFactory, UserFactory


class TestCase(PlustTestCase):
    """A base test case class."""

    user_factory = UserFactory


class TestUser(TestCase):
    def test_book(self):
        user = self.make_user()
        book = BookFactory(user=user)

        assert user.book_set.latest("id") == book
