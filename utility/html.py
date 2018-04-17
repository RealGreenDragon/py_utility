# -*- coding: utf-8 -*-

"""
Copyright (C) 2018  Daniele Giudice
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
"""

# Cross version HTML escaping functions
try:
    # Python v2.2.x - v2.7.x
    from HTMLParser import HTMLParser
    _html_parser = HTMLParser()
    def html_escape(html_string):
        return _html_parser.escape(html_string)
    def html_unescape(html_string):
        return _html_parser.unescape(html_string)
except ImportError:
    try:
        # Python v3.4.x or upper
        from html import escape as html_escape
        from html import unescape as html_unescape
    except ImportError:
        # Python v3.0.x - v3.3.x
        from html.parser import HTMLParser
        _html_parser = HTMLParser()
        def html_escape(html_string):
            return _html_parser.escape(html_string)
        def html_unescape(html_string):
            return _html_parser.unescape(html_string)
