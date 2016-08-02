# -*- coding: utf-8 -*-
from plone import api
from zope.annotation.interfaces import IAnnotations


STORAGE_KEY = 'collective.linguatags'


def get_storage():
    portal = api.portal.get()
    return IAnnotations(portal, STORAGE_KEY)
