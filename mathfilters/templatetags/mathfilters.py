from django.template import Library

register = Library()


def int_or_float(arg):
    if isinstance(arg, int) or isinstance(arg, float):
        return arg
    try:
        return int(arg)
    except ValueError:
        return float(arg)
    

@register.filter
def sub(value, arg):
    """Subtracts the arg from the value."""
    try:
        return int_or_float(value) - int_or_float(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''
sub.is_safe = False


@register.filter
def mul(value, arg):
    """Multiplies the arg with the value."""
    try:
        return int_or_float(value) * int_or_float(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''
mul.is_safe = False


@register.filter()
def div(value, arg):
    """Divides the arg by the value."""
    try:
        return int_or_float(value) / int_or_float(arg)
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''
div.is_safe = False


@register.filter(name='abs')
def absolute(value):
    """Returns the absolute value."""
    try:
        return abs(int_or_float(value))
    except (ValueError, TypeError):
        try:
            return abs(value)
        except Exception:
            return ''
absolute.is_safe = False
