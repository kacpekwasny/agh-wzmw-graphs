

def inherit_docstring(inherit_from, *, concat=False):
    """
    The inner function will by default have its __doc__ overwriten by the inherit_from.__doc__,
    or if concat=True, then the inherit_from.__doc__ will be appended to the inner function.__doc__
        params:
            inherit_from: function
            concat: bool    True            -> append
                            False (default) -> overwrite
        return:
            function (with the changed __doc__)
    """
    def decorator(func):
        if concat:
            func.__doc__ = "\n" + inherit_from.__doc__
            return func
        func.__doc__ = inherit_from.__doc__
        return func
    return decorator



