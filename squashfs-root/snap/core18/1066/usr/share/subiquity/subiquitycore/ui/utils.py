# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" UI utilities """

from urwid import Padding as _Padding
from urwid import AttrMap, Text
from functools import partialmethod
from subiquitycore.palette import STYLES


def apply_padders(cls):
    """ Decorator for generating useful padding methods

    Loops through and generates methods like:

      Padding.push_1(Widget)

      Sets the left padding attribute by 1

      Padding.pull_24(Widget)

      Sets right padding attribute by 24.

      Padding.center_50(Widget)

      Provides center padding with a relative width of 50
    """
    padding_count = 100

    for i in range(1, padding_count):
        setattr(cls, 'push_{}'.format(i), partialmethod(_Padding, left=i))
        setattr(cls, 'pull_{}'.format(i), partialmethod(_Padding, right=i))
        setattr(cls, 'fixed_{}'.format(i),
                partialmethod(_Padding, align='center',
                              width=i, min_width=i))
        setattr(cls, 'center_{}'.format(i),
                partialmethod(_Padding, align='center',
                              width=('relative', i)))
        setattr(cls, 'left_{}'.format(i),
                partialmethod(_Padding, align='left',
                              width=('relative', i)))
        setattr(cls, 'right_{}'.format(i),
                partialmethod(_Padding, align='right',
                              width=('relative', i)))
    return cls


@apply_padders
class Padding:
    """ Padding methods

    .. py:meth:: push_X(:class:`urwid.Widget`)

       This method supports padding the left side of the widget
       from 1-99, for example:

       .. code::

          Padding.push_20(Text("This will be indented 20 columns")

    .. py:meth:: pull_X(:class:`urwid.Widget`)

       This method supports padding the right side of the widget
       from 1-99, for example:

       .. code::

          Padding.pull_20(Text("This will be right indented 20 columns")

    .. py:meth:: fixed_X(:class:`urwid.Widget`)

       This method supports padding the widget to a fixed size and
       centering it.
       from 1-99, for example:

       .. code::

          Padding.fixed_20(Text("This will be centered and fixed sized
                                 of 20 columns"))

    .. py:meth:: center_X(:class:`urwid.Widget`)

       This method centers a widget with X being the relative width of
       the widget.

       .. code::

          Padding.center_10(Text("This will be centered with a "
                                 "width of 10 columns"))

    .. py:meth:: left_X(:class:`urwid.Widget`)

       This method aligns a widget left with X being the relative width of
       the widget.

       .. code::

          Padding.left_10(Text("This will be left aligned with a "
                               "width of 10 columns"))

    .. py:meth:: right_X(:class:`urwid.Widget`)

       This method right aligns a widget with X being the relative width of
       the widget.

       .. code::

          Padding.right_10(Text("This will be right aligned with a "
                                "width of 10 columns"))

    """
    line_break = partialmethod(Text)


def apply_style_map(cls):
    """ Applies AttrMap attributes to Color class

    Eg:

      Color.frame_header(Text("I'm text in the Orange frame header"))
      Color.body(Text("Im text in wrapped with the body color"))
    """
    style_names = set()
    for k in STYLES:
        style_names.add(k[0])
    for k in STYLES:
        kf = k[0] + ' focus'
        if k[0] + ' focus' in style_names:
            setattr(cls, k[0], partialmethod(AttrMap, attr_map=k[0], focus_map=kf))
        else:
            setattr(cls, k[0], partialmethod(AttrMap, attr_map=k[0]))
    return cls


@apply_style_map
class Color:
    """ Partial methods for :class:`~subiquity.palette.STYLES`

    .. py:meth:: frame_header(:class:`urwid.Widget`)

       This method colors widget based on the style map used.

       .. code::

          Color.frame_header(Text("This will use foreground and background "
                                  "defined from the STYLES attribute"))

    """
    pass
