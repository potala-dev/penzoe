import factory


class ThreadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "discourse.Thread"

    user = factory.SubFactory("penzoe.users.tests.factories.UserFactory")
    book = factory.SubFactory("penzoe.books.tests.factories.BookFactory")
    title = factory.Sequence(lambda n: f"Thread {n}")


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "discourse.Comment"

    user = factory.SubFactory("penzoe.users.tests.factories.UserFactory")
    thread = factory.SubFactory(ThreadFactory)
    text = factory.Sequence(lambda n: f"Comment {n} text.")
