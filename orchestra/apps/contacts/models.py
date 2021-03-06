from datetime import datetime

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

from orchestra.models.utils import get_model

from . import settings


class Contact(models.Model):
    """ 
    Represents a customer or member, depending on the context,
    with contact information and related contracted services
    """
    short_name = models.CharField(_("short name"), max_length=128, blank=True)
    full_name = models.CharField(_("full name"), max_length=256, unique=True)
    national_id = models.CharField(_("national ID"), max_length=64)
    address = models.CharField(_("address"), max_length=256, blank=True)
    city = models.CharField(_("city"), max_length=128, blank=True,
            default=settings.CONTACTS_DEFAULT_CITY)
    zipcode = models.PositiveIntegerField(_("zip code"), blank=True, null=True)
    province = models.CharField(_("province"), max_length=20, blank=True,
            default=settings.CONTACTS_DEFAULT_PROVINCE)
    country = models.CharField(_("country"), max_length=20,
            default=settings.CONTACTS_DEFAULT_COUNTRY)
    type = models.CharField(_("type"), max_length=32,
            choices=settings.CONTACTS_TYPE_CHOICES,
            default=settings.CONTACTS_DEFAULT_TYPE)
    comments = models.TextField(_("comments"), max_length=256, blank=True)
    language = models.CharField(_("language"), max_length=2,
            choices=settings.CONTACTS_LANGUAGE_CHOICES,
            default=settings.CONTACTS_DEFAULT_LANGUAGE)
    register_date = models.DateTimeField(_("register date"), auto_now_add=True)
    
    def __unicode__(self):
        return self.full_name


class Contract(models.Model):
    """ Represents contracted services by a particular contact """
    contact = models.ForeignKey(Contact, verbose_name=_("contact"))
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(null=True)
    service = generic.GenericForeignKey()
    description = models.CharField(_("description"), max_length=256, blank=True)
    register_date = models.DateTimeField(_("eegister date"), auto_now_add=True)
    cancel_date = models.DateTimeField(_("cancel date"), null=True, blank=True)
    
    content_object = generic.GenericForeignKey()
    
    class Meta:
        unique_together = ('content_type', 'object_id')
    
    def __unicode__(self):
        return "<%s: %s>" % (self.contact, str(self.service))
    
    def cancel(self):
        self.cancel_date=datetime.now()
        self.save()
    
    @property
    def is_canceled(self):
        if self.cancel_date and self.cancel_date < datetime.now():
            return True
        return False


for model_label in settings.CONTACTS_CONTRACT_MODELS:
    # Hook contact and contract properties to CONTACTS_CONTRACT_MODELS
    @property
    def contract(self):
        return self.related_contract.get()
    
    @property
    def contact(self):
        return self.contract.contact
    
    model = get_model(model_label)
    model.add_to_class('related_contract', generic.GenericRelation('contacts.Contract'))
    model.add_to_class('contract', contract)
    model.add_to_class('contact', contact)
