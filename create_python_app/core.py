import sys
import re
import datetime
from jinja2 import Environment, FileSystemLoader

from . import message
from . import info


def input_info(default_str: str, input_guide, validation):
    try:
        while True:
            input_str: str = input(input_guide(default_str)) or default_str

            # validation
            if validation(input_str):
                return input_str
            else:
                print(message.ERROR_INVALID_INPUT_MSG)

    except KeyboardInterrupt:
        print(message.ERROR_KEYBOARD_INTERRUPT)
        sys.exit(1)


def main():
    app_info: info.AppInfo = info.AppInfo()

    # input info
    app_info.app_name = input_info(
        get_default_app_name(),
        message.APP_NAME_INPUT_GUIDE,
        is_correct_app_name,
    )
    app_info.author = input_info(
        get_default_author(),
        message.AUTHOR_INPUT_GUIDE,
        is_correct_author,
    )
    app_info.description = input_info(
        get_default_description(),
        message.DESCRIPTION_INPUT_GUIDE,
        is_correct_description,
    )
    app_info.app_version = input_info(
        get_default_app_version(),
        message.APP_VERSION_INPUT_GUIDE,
        is_correct_app_version,
    )
    app_info.python_version = input_info(
        get_default_python_version(),
        message.PYTHON_VERSION_INPUT_GUIDE,
        is_correct_python_version,
    )
    app_info.year = get_default_year()


def is_correct_app_name(app_name: str) -> bool:
    return app_name != ''


def is_correct_author(author: str) -> bool:
    return author != ''


def is_correct_description(description: str) -> bool:
    return description != ''


def is_correct_app_version(app_version: str) -> bool:
    return re.fullmatch(r'([1-9]\d{0,4}|0)(\.(([1-9]\d{0,4})|0)){0,3}$', app_version)


def is_correct_python_version(python_version: str) -> bool:
    return re.fullmatch(r'([1-9]\d{0,4}|0)(\.(([1-9]\d{0,4})|0)){0,3}$', python_version)


def get_default_app_name() -> str:
    return ''


def get_default_author() -> str:
    return ''


def get_default_description() -> str:
    return ''


def get_default_app_version() -> str:
    return '0.1.0'


def get_default_python_version() -> str:
    return '%s.%s' % (sys.version_info.major, sys.version_info.minor)


def get_default_year() -> str:
    return datetime.date.today().year


main()
