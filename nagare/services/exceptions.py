# Encoding: utf-8

# --
# Copyright (c) 2008-2019 Net-ng.
# All rights reserved.
#
# This software is licensed under the BSD License, as described in
# the file LICENSE.txt, which you should have received as part of
# this distribution.
# --


class BadConfiguration(Exception):
    """Invalid configuration"""


class MissingDependency(Exception):
    """Missing dependency to inject"""


class MissingService(Exception):
    """Missing service to inject"""
