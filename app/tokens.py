from django.contrib.auth.tokens import PasswordResetTokenGenerator


def create_token(user):
    return PasswordResetTokenGenerator().make_token(user)


def validate_token(user, token):
    return PasswordResetTokenGenerator().check_token(user, token)
