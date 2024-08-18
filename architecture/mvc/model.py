#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2024-08-17 11:54:56
# @Author  : Your Name (you@example.org)
# @Link    : link
# @Version : 1.0.0


"""
Model
"""

from .Controllable import Controllable


from abc import abstractmethod
from typing import Any, Callable, Hashable


class i_Model:
    pass


class Model(i_Model, Controllable):
    pass

