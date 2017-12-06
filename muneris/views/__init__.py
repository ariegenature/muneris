"""Muneris package for views and blueprints."""

from flask import redirect, url_for

from muneris.views.area import area


blueprints = [area]


def home():
    """Muneris homepage."""
    return redirect(url_for('area.index'))
