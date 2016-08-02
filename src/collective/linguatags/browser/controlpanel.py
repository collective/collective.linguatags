# -*- coding: utf-8 -*-s
from collective.linguatags import _
from collective.linguatags.storage import get_storage
from persistent.dict import PersistentDict
from plone import api
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LinguaTagsControlPanel(BrowserView):
    """Control panel for the portal actions."""

    template = ViewPageTemplateFile('controlpanel.pt')

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.storage = get_storage()

    def available_languages(self):
        return sorted(
            api.portal.get_registry_record('plone.available_languages')
        )

    def tags(self):
        catalog = api.portal.get_tool('portal_catalog')
        index = catalog._catalog.getIndex('Subject')
        for tag in index._index:
            yield tag

    def translation(self, tag, language):
        return self.storage.get(tag, {}).get(language, '')

    def __call__(self):
        if self.request.form.get('submitted', False):
            for tag in self.tags():
                value = self.request.form.get(tag, None)
                if value is None:
                    continue
                translations = self.storage.get(tag, None)
                if translations is None:
                    self.storage[tag] = PersistentDict()
                for lang in value:
                    if lang not in self.available_languages():
                        continue
                    self.storage[tag][lang] = value[lang]
                api.portal.show_message(
                    _('Translations saved'),
                    request=self.request
                )
        return self.template()
