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

    GW2api - Python wrapper for Guild Wars 2 official API.
    Copyright (C) 2013  Rok Mocnik <rok dot mocnik at ntnu dot no>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
