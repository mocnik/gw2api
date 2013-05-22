Python Wrapper for Guild Wars 2 official API
============================================

This Python module provides access to the official Guild Wars 2 API.

Guild Wars 2 API
----------------

[Guild Wars 2 API](https://forum-en.guildwars2.com/forum/community/api/API-Documentation/first#post2028044) is officially
supported API. It provides access and tools to monitoring the state of all dynamic events, state of the WvW match-ups
and listing of all items and recipes available in Guild Wars 2.

Installation
------------

Put `gw2api.py` inside your project and use it with `import gw2api`.

Usage
-----

    import gw2api

	# Server names in French
    gw2api.get_world_names(lang="fr")

    # Specific event on Gate of Madness
    gw2api.get_events(event_id="EB8D67FD-8371-4E21-A934-805C025D0AF4", world_id=1007)

    # All events in Queensdale on Gate of Madness
    gw2api.get_events(map_id=15, world_id=1007)


License
-------

    The MIT License (MIT)

    Copyright (c) 2013 Rok Mocnik <rok.mocnik@ntnu.no>

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
