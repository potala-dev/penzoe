from penzoe.book.tests.factories import BookFactory
from penzoe.discourse.tests.factories import CommentFactory, ThreadFactory
from penzoe.test import TestCase
from penzoe.users.tests.factories import ProfileFactory


class TestUser(TestCase):
    def test_str(self):
        user = self.make_user()
        assert str(user) == user.email

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

    def test_update_points(self):
        user = self.make_user()
        BookFactory(user=user)
        ThreadFactory(user=user, points=1)
        ThreadFactory(user=user, points=2)
        CommentFactory(user=user, points=1)
        CommentFactory(user=user, points=2)
        user.update_points()

        assert user.points == (1 + (1 + 2) * 2 + (1 + 2) * 5)


class TestProfile(TestCase):
    def test_str(self):
        user = self.make_user()
        profile = ProfileFactory(user=user)

        assert str(profile) == f"{profile.user.email} Profile"
