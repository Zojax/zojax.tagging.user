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
from zope.component import getUtility
from zojax.tagging.user.interfaces import IPersonalTags, IPersonalTagsConfiglet


class PersonalTags(object):
    interface.implements(IPersonalTags)

    @property
    def engine(self):
        return getUtility(IPersonalTagsConfiglet).getEngine(self.__principal__.id)

    def getTags(self, oid):
        configlet = getUtility(IPersonalTagsConfiglet)
        return configlet.getTags(self.__principal__.id, oid)

    def setTags(self, oid, tags):
        configlet = getUtility(IPersonalTagsConfiglet)
        configlet.setTags(self.__principal__.id, oid, tags)

    def removeTags(self, oid):
        configlet = getUtility(IPersonalTagsConfiglet)
        configlet.removeTags(self.__principal__.id, oid)
