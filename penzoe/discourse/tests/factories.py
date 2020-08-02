import factory


class ThreadFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "discourse.Thread"

    user = factory.SubFactory("penzoe.users.tests.factories.UserFactory")
    book = factory.SubFactory("penzoe.users.tests.factories.UserFactory")
