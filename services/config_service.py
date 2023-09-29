from typing import Any
from constants import app_config_constants
from utilities.file_utils import FileUtils


class ConfigService:
    def __init__(self, settings_filepath: str) -> None:
        self.config_filepath = settings_filepath
        self.config_object = FileUtils.read_json_file(self.config_filepath)

        self.app_settings_key = app_config_constants.APP_SETTINGS_KEY
        self.blogger_settings_key = app_config_constants.BLOGGER_SETTINGS
        self.api_keys_key = app_config_constants.API_KEYS_KEY
        self.is_config_updated = False

    def get_full_configuration(self):
        return self.config_object

    def get_configuration(self, setting_key: str):
        return self.config_object[setting_key]

    def set_configuration(self, setting_key: str, value: Any):
        self.config_object[setting_key] = value
        self.is_config_updated = True

    def get_preference(self, setting_key: str):
        return self.config_object[self.app_settings_key][setting_key]

    def get_blogger_setting(self, setting_key: str):
        return self.config_object[self.blogger_settings_key][setting_key]

    def get_api_key(self, api_provider: str):
        return self.config_object[self.api_keys_key][api_provider]

    def get_blogger_auth_setting(self, setting_key: str):
        return self.get_blogger_setting("auth_settings")[setting_key]

    def set_blogger_auth_setting(self, setting_key: str, value: Any):
        self.get_blogger_setting("auth_settings")[setting_key] = value
        self.is_config_updated = True

    def __del__(self):
        if self.is_config_updated:
            FileUtils.write_json_file(self.config_filepath, self.config_object)
