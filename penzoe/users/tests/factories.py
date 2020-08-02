import factory
from django.conf import settings


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: f"user_{n}")
    email = "testuser@test.com"


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "users.Profile"
