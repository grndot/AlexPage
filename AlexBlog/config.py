from dataclasses import dataclass

from environs import Env


@dataclass
class Django:
    """
    Creates the Django object from environment variables.
    """
    secret_key: str

    @staticmethod
    def from_env(env: Env):
        """
        Creates the Django object from environment variables.
        """
        secret_key = env.str("SECRET_KEY")
        return Django(secret_key=secret_key)


@dataclass
class Config:
    """
    The main configuration class that integrates all the other configuration classes.
    This class holds the other configuration classes, providing a centralized point of access for all settings.
    Attributes
    ----------
    django : Django
    """
    django: Django


def load_config(path: str|None = None) -> Config:
    """
    This function takes an optional file path as input and returns a Config object.
    :param path: The path of env file from where to load the configuration variables.
    It reads environment variables from a .env file if provided, else from the process environment.
    :return: Config object with attributes set as per environment variables.
    """

    # Create an Env object.
    # The Env object will be used to read environment variables.
    env = Env()
    env.read_env(path)

    return Config(
            django=Django.from_env(env))
