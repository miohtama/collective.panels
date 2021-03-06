from .i18n import MessageFactory as _
from plone.app.layout.viewlets import interfaces
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


class ManagerVocabulary(object):
    implements(IVocabularyFactory)

    # Order is important here; the default location will be the first
    # available (non-hidden) manager.
    all_viewlet_managers = (
        (interfaces.IBelowContentBody, _(u"Below body content")),
        (interfaces.IAboveContentBody, _(u"Above body content")),

        (interfaces.IBelowContent, _(u"Below all content")),
        (interfaces.IAboveContent, _(u"Above all content")),

        (interfaces.IPortalFooter, _(u"Portal footer")),
        (interfaces.IPortalTop, _(u"Portal top")),
    )

    def __call__(self, context):
        return SimpleVocabulary([
            SimpleTerm(interface, interface.__name__, title)
            for (interface, title) in self.all_viewlet_managers
        ])


managers = ManagerVocabulary()
