import os
import argparse
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    # Select the correct .env file based on the environment
    env_file = None
    if environment == "dev":
        env_file = ".env.dev"
    elif environment == "test":
        env_file = ".env.test"
    elif environment == "prod":
        env_file = ".env.prod"
    else:
        raise ValueError(f"Unknown environment: {environment}")

    # Load the .env file
    load_dotenv(dotenv_path=env_file)

    # Validate that the loaded ENVIRONMENT matches the requested one
    loaded_environment = os.getenv("ENVIRONMENT")
    if loaded_environment != environment:
        raise ValueError(
            f"Mismatch: expected ENVIRONMENT={environment}, but got ENVIRONMENT={loaded_environment} from {env_file}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
