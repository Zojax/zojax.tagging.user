##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface


class IUserTaggable(interface.Interface):
    """Marker interface for taggable object by user."""


class IPersonalTags(interface.Interface):
    """Personal tags"""

    engine = interface.Attribute('Tagging engind')

    def getTags(oid):
        """Return tags for oid."""

    def setTags(oid, tags):
        """Set tags for oid."""


class IPersonalTagsConfiglet(interface.Interface):
    """Personal tags configlet """
