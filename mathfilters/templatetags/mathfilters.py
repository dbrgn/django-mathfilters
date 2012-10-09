from django.template import Library

register = Library()


@register.filter(is_safe=False)
def sub(value, arg):
    """Subtracts the arg from the value."""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        try:
            return value - arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def mul(value, arg):
    """Multiplies the arg with the value."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        try:
            return value * arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def div(value, arg):
    """Divides the arg by the value."""
    try:
        return int(value) / int(arg)
    except (ValueError, TypeError):
        try:
            return value / arg
        except Exception:
            return ''


@register.filter(is_safe=False)
def abs(value):
    """Returns the absolute value."""
    try:
        return abs(int(value))
    except (ValueError, TypeError):
        try:
            return abs(value)
        except Exception:
            return ''
