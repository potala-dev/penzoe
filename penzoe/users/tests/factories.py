import factory
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: f"user_{n}")
    email = factory.Sequence(lambda n: f"user_{n}@test.com")


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.Profile"

    user = factory.SubFactory("penzoe.users.tests.factories.UserFactory")
