# -*- coding: utf-8 -*-
from zope.i18nmessageid import MessageFactory
from plone.app.layout.viewlets import ViewletBase

mf = MessageFactory('linguatags')


class KeywordsViewlet(ViewletBase):
    """Return messagestrings for keywords"""

    def displayMessageString(self, keyword):
        return mf(keyword)
