# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase
from zope.i18nmessageid import MessageFactory

mf = MessageFactory('linguatags')


class KeywordsViewlet(ViewletBase):
    """Return messagestrings for keywords"""

    def displayMessageString(self, keyword):
        return mf(keyword)
