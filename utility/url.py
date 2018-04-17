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

# Cross version URL quoting functions
try:
    # Python v2.x
    from urllib import quote_plus as url_quote_plus
    from urllib import unquote_plus as url_unquote_plus
    from urllib import quote as url_quote
    from urllib import unquote as url_unquote
    from urllib import urlencode
except ImportError:
    # Python v3.x
    from urllib.parse import quote_plus as url_quote_plus
    from urllib.parse import unquote_plus as url_unquote_plus
    from urllib.parse import quote as url_quote
    from urllib.parse import unquote as url_unquote
    from urllib.parse import urlencode
