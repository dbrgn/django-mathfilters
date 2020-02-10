import logging
from decimal import Decimal

from django.template import Library


register = Library()
logger = logging.getLogger(__name__)


def valid_numeric(arg):
    if isinstance(arg, (int, float, Decimal)):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)


def handle_float_decimal_combinations(value, arg, operation):
    if isinstance(value, float) and isinstance(arg, Decimal):
        logger.warning('Unsafe operation: {0!r} {1} {2!r}.'.format(value, operation, arg))
        value = Decimal(str(value))
    if isinstance(value, Decimal) and isinstance(arg, float):
        logger.warning('Unsafe operation: {0!r} {1} {2!r}.'.format(value, operation, arg))
        arg = Decimal(str(arg))
    return value, arg


@register.filter
def sub(value, arg):
    """Subtract the arg from the value."""
    try:
        nvalue, narg = handle_float_decimal_combinations(
            valid_numeric(value), valid_numeric(arg), '-')
        return nvalue - narg
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''


@register.filter
def mul(value, arg):
    """Multiply the arg with the value."""
    try:
        nvalue, narg = handle_float_decimal_combinations(
            valid_numeric(value), valid_numeric(arg), '*')
        return nvalue * narg
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''


@register.filter
def div(value, arg):
    """Divide the arg by the value."""
    try:
        nvalue, narg = handle_float_decimal_combinations(
            valid_numeric(value), valid_numeric(arg), '/')
        return nvalue / narg
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''


@register.filter
def intdiv(value, arg):
    """Divide the arg by the value. Use integer (floor) division."""
    try:
        nvalue, narg = handle_float_decimal_combinations(
            valid_numeric(value), valid_numeric(arg), '//')
        return nvalue // narg
    except (ValueError, TypeError):
        try:
            return value // arg
        except Exception:
            return ''


@register.filter(name='abs')
def absolute(value):
    """Return the absolute value."""
    try:
        return abs(valid_numeric(value))
    except (ValueError, TypeError):
        try:
            return abs(value)
        except Exception:
            return ''


@register.filter
def mod(value, arg):
    """Return the modulo value."""
    try:
        nvalue, narg = handle_float_decimal_combinations(
            valid_numeric(value), valid_numeric(arg), '%')
        return nvalue % narg
    except (ValueError, TypeError):
        try:
            return value % arg
        except Exception:
            return ''


@register.filter(name='addition')
def addition(value, arg):
    """Float-friendly replacement for Django's built-in `add` filter."""
    try:
        nvalue, narg = handle_float_decimal_combinations(
            valid_numeric(value), valid_numeric(arg), '+')
        return nvalue + narg
    except (ValueError, TypeError):
        try:
            return value + arg
        except Exception:
            return ''
