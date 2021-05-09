# Generated by Django 3.1.6 on 2021-03-27 19:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0014_auto_20210327_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Organisation name / Organisationsname')),
                ('filter_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Filter name')),
                ('org_number', models.CharField(max_length=255, verbose_name='Organisations N° / Organisations Nr.')),
                ('website', models.CharField(max_length=255, verbose_name='Webseite / Webseite')),
                ('primary_phone', phone_field.models.PhoneField(blank=True, max_length=255, null=True, verbose_name='Primary phone / primäres Telefon')),
                ('add_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Additional name / Org. Namenszusatz')),
                ('fax', phone_field.models.PhoneField(blank=True, max_length=255, null=True, verbose_name='Fax')),
                ('member_of', models.CharField(blank=True, max_length=255, null=True, verbose_name='Member of / Mitglied von')),
                ('another_phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Another phone / anderes Telefon')),
                ('staff', models.CharField(blank=True, max_length=255, null=True, verbose_name='Staff / Mitarbeiter')),
                ('primary_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Primary email / primäre E-Mail')),
                ('another_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='Another email / andere E-Mail')),
                ('ownership', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ownership / Eigentümer')),
                ('sector', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sector / Branche')),
                ('evaluation', models.CharField(blank=True, max_length=255, null=True, verbose_name='Evaluation / Wertung')),
                ('org_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Type / Typ')),
                ('ust_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='UST. N° / Ust. Nr.')),
                ('email_opt_from', models.CharField(blank=True, max_length=255, null=True, verbose_name='Email OPT from / E-Mail Opt. aus')),
                ('yearly_revenue', models.CharField(blank=True, max_length=255, null=True, verbose_name='Yearly revenue / jährlicher Umsatz')),
                ('responsible', models.CharField(blank=True, max_length=255, null=True, verbose_name='Responsible / zuständig')),
                ('inform_owners', models.CharField(blank=True, max_length=255, null=True, verbose_name='Inform owners / Besitzer informieren')),
                ('changed', models.DateTimeField(blank=True, null=True, verbose_name='changed / geändert')),
                ('created', models.DateTimeField(blank=True, null=True, verbose_name='created / erstellt')),
                ('most_recently_amended_by', models.CharField(blank=True, max_length=255, null=True, verbose_name='Most recently amended by / zuletzt geändert durch')),
                ('created_from_lead', models.CharField(blank=True, max_length=255, null=True, verbose_name='Created from lead / aus Lead erstellt')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address / Rechnungsadresse')),
                ('invoice_po_box', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice PO Box / Rechnung Postfach')),
                ('invoice_place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice Place / Rechnung Ort')),
                ('delivery_place', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery Place / Lieferung Ort')),
                ('org_invoice_federal_state', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice Federal State / Rechnung Bundesland')),
                ('org_delivery_state', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery State / Lieferung Bundesland')),
                ('org_Invoice_postal_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice postal code / Rechnung PLZ')),
                ('org_delivery_zip_code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery zip code / Lieferung PLZ')),
                ('org_invoice_country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Invoice country / Rechnung Land')),
                ('org_delivery_country', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery country / Lieferung Land')),
                ('full_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='The complete address')),
                ('latitude', models.DecimalField(blank=True, decimal_places=20, default='0.00', max_digits=30, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=20, default='0.00', max_digits=30, null=True, verbose_name='Longitude')),
                ('shipping_address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Shipping address / Lieferadresse')),
                ('delivery_mailbox', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery mailbox / Lieferung Postfach')),
                ('org_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description / Beschreibung')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('ceo', models.CharField(blank=True, max_length=255, null=True, verbose_name='CEO')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='map_app.orgs')),
            ],
            options={
                'verbose_name_plural': 'organisations',
            },
        ),
    ]