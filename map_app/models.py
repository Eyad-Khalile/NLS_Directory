from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from phone_field import PhoneField


class Orgs(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True,
                            related_name='children', db_index=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=False,
                            verbose_name="Organisation name / Organisationsname")

    org_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Organisations N° / Organisations Nr.")

    website = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Webseite / Webseite")
    primary_phone = PhoneField(
        max_length=255, blank=True, null=True, verbose_name="Primary phone / primäres Telefon")
    add_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Additional name / Org. Namenszusatz")
    fax = PhoneField(
        max_length=255, blank=True, null=True, verbose_name="Fax")
    member_of = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Member of / Mitglied von")
    another_phone = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Another phone / anderes Telefon")
    staff = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Staff / Mitarbeiter")
    primary_email = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Primary email / primäre E-Mail")
    another_email = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Another email / andere E-Mail")
    ownership = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Ownership / Eigentümer")
    sector = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Sector / Branche")
    evaluation = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Evaluation / Wertung")
    org_type = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Type / Typ")
    ust_number = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="UST. N° / Ust. Nr.")
    email_opt_from = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Email OPT from / E-Mail Opt. aus")
    yearly_revenue = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Yearly revenue / jährlicher Umsatz")
    responsible = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Responsible / zuständig")
    inform_owners = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Inform owners / Besitzer informieren")

    changed = models.DateTimeField(
        blank=True, null=True, verbose_name="changed / geändert")
    created = models.DateTimeField(
        blank=True, null=True, verbose_name="created / erstellt")

    most_recently_amended_by = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Most recently amended by / zuletzt geändert durch")
    created_from_lead = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Created from lead / aus Lead erstellt")

    address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="address / Rechnungsadresse")
    shipping_address = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Shipping address / Lieferadresse")
    invoice_po_box = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Invoice PO Box / Rechnung Postfach")
    delivery_mailbox = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Delivery mailbox / Lieferung Postfach")
    invoice_place = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Invoice Place / Rechnung Ort")
    delivery_place = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Delivery Place / Lieferung Ort")
    org_invoice_federal_state = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Invoice Federal State / Rechnung Bundesland")
    org_delivery_state = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Delivery State / Lieferung Bundesland")
    org_Invoice_postal_code = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Invoice postal code / Rechnung PLZ")
    org_delivery_zip_code = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Delivery zip code / Lieferung PLZ")
    org_invoice_country = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Invoice country / Rechnung Land")

    org_country = models.ForeignKey(
        "Countries", related_name="org_country", on_delete=models.SET_NULL, null=True, blank=True)

    org_delivery_country = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Delivery country / Lieferung Land")
    org_description = models.TextField(
        max_length=2000, blank=True, null=True, verbose_name="Description / Beschreibung")
    about_link = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='About Link')

    full_address = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Full Address")

    latitude = models.DecimalField(
        max_digits=30, decimal_places=20, null=True, blank=True, default="0.00", verbose_name="Latitude")
    longitude = models.DecimalField(
        max_digits=30, decimal_places=20, null=True, blank=True, default="0.00", verbose_name="Longitude")

    filter_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Filter name")

    order_by = models.IntegerField(
        null=True, blank=True, unique=True, verbose_name="Order Number")

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(
        auto_now=True, auto_now_add=False, null=True, blank=True)

    ceo = models.CharField(max_length=255, null=True,
                           blank=True, verbose_name="CEO")

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'organisations'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("org_details", kwargs={"id": self.id})


class Countries(models.Model):
    name = models.CharField(max_length=150, verbose_name="country name")
    path = models.TextField(max_length=5000, verbose_name="path")
    filtre_name = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.DecimalField(
        max_digits=30, decimal_places=20, null=True, blank=True, default="0.00", verbose_name="Latitude")
    longitude = models.DecimalField(
        max_digits=30, decimal_places=20, null=True, blank=True, default="0.00", verbose_name="Longitude")
    created_at = models.DateTimeField(
        auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.filtre_name or self.name
