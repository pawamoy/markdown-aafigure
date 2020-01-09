# This file is part of the markdown_aafigure project
# https://gitlab.com/mbarkhau/markdown_aafigure
#
# Copyright (c) 2019 Manuel Barkhau (mbarkhau@gmail.com) - MIT License
# SPDX-License-Identifier: MIT

__version__ = "v202001.0007"


from markdown_aafigure.extension import AafigureExtension


def makeExtension(**kwargs):
    return AafigureExtension(**kwargs)
