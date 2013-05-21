# GW2api - Python wrapper for Guild Wars 2 official API.
# Copyright (C) 2013  Rok Mocnik <rok dot mocnik at ntnu dot no>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Import proper urllib and JSON library
import urllib2
try:
    import json
except ImportError:
    import simplejson as json

def get_items():
    """ Get a list of all item ids. """
    return _request("items.json")

def get_item_details(id, lang="en"):
    """ Get details of specific item. """
    return _request("item_details.json", item_id=id, lang=lang)

def get_recipes():
    """ Get a list of all recipes. """
    return _request("recipes.json")

def get_recipe_details(id, lang="en"):
    """ Get details of specific item. """
    return _request("recipe_details.json", recipe_id=id, lang=lang)

def get_wvw_matches():
    """ Get the current running WvW matches. """
    return _request("wvw/matches.json")

def get_wvw_match_details(id):
    """ Get the current match details. """
    return _request("wvw/match_details.json", match_id=id)

def get_wvw_objective_names(lang="en"):
    """ Get the names of all objectives in WvW maps. """
    return _request("wvw/objective_names.json", lang=lang)

def get_event_names(lang="en"):
    """ Get names of all existing events. """
    return _request("event_names.json", lang=lang)

def get_map_names(lang="en"):
    """ Get names of all maps. """
    return _request("map_names.json", lang=lang)

def get_world_names(lang="en"):
    """ Get names of all world servers. """
    return _request("world_names.json", lang=lang)

def get_events(**args):
    """ Get list events based on filtering by world, map and event. """
    return _request("events.json", **args)


def _request(json_location, **args):
    """ Makes a request on the Guild Wars 2 API."""
    url = 'https://api.guildwars2.com/v1/' + json_location + '?' + '&'.join(str(argument) + '=' + str(value) for argument, value in args.items())
    return json.loads(urllib2.urlopen(url).read())
