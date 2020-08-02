from penzoe.book.tests.factories import BookFactory
from penzoe.discourse.tests.factories import ThreadFactory
from penzoe.test import TestCase


class TestUser(TestCase):
    def test_str(self):
        user = self.make_user()
        assert str(user) == "testuser@test.com"

    def test_book(self):
        user = self.make_user()
        book = BookFactory(user=user)
        assert user.book_set.latest("id") == book

    def test_get_total_points(self):
        user = self.make_user()
        book = BookFactory(user=user)
        ThreadFactory(user=user, book=book, points=1)
        ThreadFactory(user=user, book=book, points=2)
        threads = user.thread_set.all()

        assert user._get_total_points(threads) == 3
