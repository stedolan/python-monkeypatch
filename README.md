
Python programmers!
===================

Are you **tired** of seeing those Ruby types having all the fun? Do you want to reopen a **perfectly good class** and **randomly remodel** its internals? Do you think Aspect-Oriented Programming is a **good idea**?


*Then python-monkeypatch is for you!*
------------------------------------

With just one simple import, you can inject a **burst of excitement** into the maintenance programmers' dreary life! Bring the **element of surprise** back to simple code upgrades! **Free** your code from the **shackles** of modularity!

With **python-monkeypatch**, you can change the code **you want to change**, in the place **you want to change it**. No more trying to find such-and-such a file **just to edit a method**! Mash out the code in **whatever file's lying around**, just like you've seen those Ruby kids doing!

*Disclaminer: the author of this code disclaims responsibility for all consequences of using this module or even reading this documentation, and distances himself from any code written using it.*

Just watch! Here's a perfectly normal, simple class.

    class Wibbler(object):
        '''A totally reasonable class'''
        def __init__(self, x):
            '''Construct a wibbler'''
            self.foo = x
    
        def wibble(self):
            '''Engage the wibbler'''
            print "wibble", self.foo 

It works, just as "designed"!

    >>> the_wibbler = Wibbler(42)
    >>> the_wibbler.wibble()
    wibble 42

But we'd like to change the `wibble` method to do something much better.

 - But the rest of my team disagree!
 - But I'm scared of the code in that file!
 - But I've already closed that file and it's four directories away!

Never fear! **python-monkeypatch** to the rescue!

    from monkeypatch import MonkeyPatch
    class improvements(MonkeyPatch(Wibbler)):
        def wibble(self):
            '''We don't really want the wibbler here...'''
            print "hah! patched!"

**BANG!** And the code is fixed!

    >>> the_wibbler.wibble()
    hah! patched!

And it even supports docstrings! What more could you want?

    >>> help(f.wibble)
    wibble(self) method of Wibbler instance
    Engage the wibbler
    
    Monkeypatched:
    We don't really want the wibbler here...

**python-monkeypatch**: *because your code should be as deranged as its author.*