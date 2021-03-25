class FontColors:
    RED: str = '\x1b[31m'
    GREEN: str = '\x1b[32m'
    YELLOW: str = '\x1b[33m'
    RESET: str = '\x1b[0m'


def CREATED_APP_MSG(app_name: str) -> str:
    result: str = 'Created ' + app_name + ' app.'
    return result


ERROR_INVALID_INPUT_MSG: str = '%sInvalid format. Try again.%s' % (
    FontColors.RED,
    FontColors.RESET,
)


ERROR_KEYBOARD_INTERRUPT_MSG: str = '%sKeyboad Interrupt.%s' % (
    FontColors.RED,
    FontColors.RESET,
)


def ERROR_APP_EXISTS_MSG(app_name: str) -> str:
    result: str = '%s%s app is already exists. Try again.%s' % (
        FontColors.RED,
        app_name,
        FontColors.RESET,
    )
    return result


def APP_NAME_INPUT_GUIDE(default_str: str) -> str:
    default_str += '' if default_str == '' else ' '
    result: str = 'app name %s%s%s: ' % (
        FontColors.GREEN,
        default_str,
        FontColors.RESET,
    )
    return result


def AUTHOR_INPUT_GUIDE(default_str: str) -> str:
    default_str += '' if default_str == '' else ' '
    result: str = 'author %s%s%s: ' % (
        FontColors.GREEN,
        default_str,
        FontColors.RESET,
    )
    return result


def DESCRIPTION_INPUT_GUIDE(default_str: str) -> str:
    default_str += '' if default_str == '' else ' '
    result: str = 'description %s%s%s: ' % (
        FontColors.GREEN,
        default_str,
        FontColors.RESET,
    )
    return result


def APP_VERSION_INPUT_GUIDE(default_str: str) -> str:
    default_str += '' if default_str == '' else ' '
    result: str = 'app version %s%s%s: ' % (
        FontColors.GREEN,
        default_str,
        FontColors.RESET,
    )
    return result


def PYTHON_VERSION_INPUT_GUIDE(default_str: str) -> str:
    default_str += '' if default_str == '' else ' '
    result: str = 'python version %s%s%s: ' % (
        FontColors.GREEN,
        default_str,
        FontColors.RESET,
    )
    return result
