def auto_buffer(obj):
    from SMELT import buffers
    from PIL.ImageFile import ImageFile
    types = [
        {
            'in': ImageFile,
            'out': buffers.PillowBuffer
        }
    ]
    in_type = obj.__class__.__base__
    try:
        out_type = list(filter(lambda x: x['in'] is in_type, types))[0]['out']
        return out_type(obj)
    except IndexError:
        raise TypeError("Could not auto convert obj to buffer")


def timeout(method, limit=None, exception=True):
    try:
        import thread
    except ModuleNotFoundError:
        import _thread as thread
    import threading
    timer = threading.Timer(limit, thread.interrupt_main)
    res = None
    if limit:
        try:
            timer.start()
            res = method()
        except KeyboardInterrupt:
            if exception:
                raise Exception("Timeout occurred. Function<%s> had %d seconds to execute" % (method.__name__, limit))
            else:
                pass
        finally:
            timer.cancel()
    else:
        res = method()
    return res


def dumpstr(obj, internals=False, methods=False):
    string = ''
    for attr in dir(obj):
        value = getattr(obj, attr)
        if callable(value) and not methods:
            continue
        if attr[0] == "_" and not internals:
            continue
        string += "%s = %r\n" % (attr, getattr(obj, attr))
    return string


def dump(obj, internals, methods):
    print(dumpstr(obj, internals=internals, methods=methods))
