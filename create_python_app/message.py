class FontColors:
    RED: str = '\x1b[31m'
    GREEN: str = '\x1b[32m'
    YELLOW: str = '\x1b[33m'
    RESET: str = '\x1b[0m'


def NAME_INPUT_GUIDE(default_str: str) -> str:
    result: str = 'name %s%s%s: ' % (
        FontColors.GREEN,
        default_str + '' if default_str == '' else ' ',
        FontColors.RESET,
    )
    return result


def DESCRIPTION_INPUT_GUIDE(default_str: str) -> str:
    result: str = 'description %s%s%s: ' % (
        FontColors.GREEN,
        default_str + '' if default_str == '' else ' ',
        FontColors.RESET,
    )
    return result


def PYTHON_VERSION_INPUT_GUIDE(default_str: str) -> str:
    result: str = 'python version %s%s%s: ' % (
        FontColors.GREEN,
        default_str + '' if default_str == '' else ' ',
        FontColors.RESET,
    )
    return result


def AUTHOR_INPUT_GUIDE(default_str: str) -> str:
    result: str = 'author %s%s%s: ' % (
        FontColors.GREEN,
        default_str + '' if default_str == '' else ' ',
        FontColors.RESET,
    )
    return result
