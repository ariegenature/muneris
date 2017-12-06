# This file is part of Muneris.
#
# Muneris is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Muneris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Muneris. If not, see <http://www.gnu.org/licenses/>.

"""Muneris blueprint to view managed areas."""

from flask import Blueprint, render_template


area = Blueprint('area', __name__, static_folder='templates/static', template_folder='templates')


@area.route('/area')
def index():
    template_data = {}
    return render_template('index.html', **template_data)
