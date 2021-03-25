import os
import sys
import re
import glob
import shutil
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
        print(message.ERROR_KEYBOARD_INTERRUPT_MSG)
        sys.exit(1)


def main():
    app_info = info.AppInfo()

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

    # create app dir
    template_root_path: str = os.path.join(os.path.dirname(__file__), 'template')
    app_root_path: str = app_info.app_name.replace(' ', '_')
    if os.path.exists(app_root_path):
        print(message.ERROR_APP_EXISTS_MSG(app_info.app_name))
        sys.exit(1)
    shutil.copytree(template_root_path, app_root_path)

    # specify PATH of the template files
    file_loader = FileSystemLoader(app_root_path)
    env = Environment(loader=file_loader)

    # overwrite template files
    for file_name in glob.glob(app_root_path + '/**/*.jinja', recursive=True):
        template = env.get_template(os.path.basename(file_name))
        save_file_name = file_name.replace('.jinja', '')

        # write
        with open(save_file_name, 'w') as file:
            file.write(template.render(info=app_info))
        # delete template file
        os.remove(file_name)

    # successful
    print(message.CREATED_APP_MSG(app_info.app_name))


def is_correct_app_name(app_name: str) -> bool:
    return re.fullmatch(r'[0-9a-zA-Z][0-9a-zA-Z_\- ]*', app_name)


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
