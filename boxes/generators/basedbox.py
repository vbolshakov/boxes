#!/usr/bin/env python3
# Copyright (C) 2013-2014 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *


class BasedBox(Boxes):
    """Fully closed box on a base"""

    ui_group = "Box"

    def __init__(self):
        Boxes.__init__(self)
        self.addSettingsArgs(edges.FingerJointSettings)
        self.buildArgParser("x", "y", "h", "outside")

    def render(self):

        x, y, h = self.x, self.y, self.h

        if self.outside:
            x = self.adjustSize(x)
            y = self.adjustSize(y)
            h = self.adjustSize(h)

        t = self.thickness

        self.rectangularWall(x, h, "fFFF", move="right")
        self.rectangularWall(y, h, "ffFf", move="up")
        self.rectangularWall(y, h, "ffFf")
        self.rectangularWall(x, h, "fFFF", move="left up")

        self.rectangularWall(x, y, "ffff", move="right")
        self.rectangularWall(x, y, "hhhh")



