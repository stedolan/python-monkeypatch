import types

def combine(old, new):
    if type(new) in [types.MethodType, types.FunctionType]:
        docs = [d for d in [getattr(old, '__doc__'), getattr(new, '__doc__')] if d]
        if len(docs) == 1:
            new.__doc__ = docs[0]
        elif len(docs) == 2:
            new.__doc__ = "%s\n\nMonkeypatched:\n%s" % tuple(docs)

class MonkeyPatchMeta(type):
    def __new__(cls, name, bases, dict):
        if '__patched_class__' in dict:
            return super(MonkeyPatchMeta, cls).__new__(cls, name, bases, dict)
        oldcls = bases[0].__patched_class__
        if not isinstance(oldcls, type):
            raise TypeError("%s is not a class" % name)
        for k,v in dict.items():
            if k not in ['__patched_class__', '__metaclass__']:
                combine(getattr(oldcls, k), v)
                setattr(oldcls, k, v)
        return oldcls

def MonkeyPatch(cls):
    '''Inheriting from MonkeyPatch(Foo) will not create a new class,
    but will instead modify the class Foo'''
    class Patcher(object):
        __patched_class__ = cls
        __metaclass__ = MonkeyPatchMeta
    return Patcher
