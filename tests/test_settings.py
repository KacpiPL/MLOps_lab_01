import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from settings import Settings


def test_settings_values():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyApp"
    assert settings.FAKE_API_KEY == "fake-key-123"
