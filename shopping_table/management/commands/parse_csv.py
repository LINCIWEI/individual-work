import csv
from pathlib import Path
from django.db import models
from django.core.management.base import BaseCommand, CommandError
import os
from shopping_table.models import maintable,detailtable



class Command(BaseCommand):
    help = 'Load data from csv'


    def handle(self, *args, **options):
        # drop the data from the table so that if we rerun the file, we don't repeat values
        maintable.objects.all().delete()
        print("table dropped successfully")
        # create table again

        # open the file to read it into the database
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(
                str(base_dir) + '/shopping_table/data/main_table.csv',newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                # print(row)

                summary_object = maintable.objects.create(
                    product_id=int(row[0]),
                    price=float(row[1]),
                    promotion_name=(row[2]),
                    sales_country=(row[3]),
                )
                summary_object.save()


        detailtable.objects.all().delete()
        print("table dropped successfully")
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        with open(
                str(base_dir) + '/shopping_table/data/product_detail.csv', newline='') as f:
            reader = csv.reader(f, delimiter=",")
            next(reader)  # skip the header line
            for row in reader:
                print(row)
                if row[2] is not '':
                    detail_product =int(row[0])
                    print(detail_product)
                    detail = maintable.objects.filter(product_id=detail_product).first()
                    print(detail.product_id)


                    Detailtable = detailtable.objects.create(
                        product_id=detail.product_id,
                        promotion_name=(row[1]),
                        sales_country=(row[2]),
                        sales_volume=(row[3]),
                        negative_comment=int(row[4]),
                        price=float(row[5]),
                        invoice_date=(row[6]),
                        supplier=(row[7]),
                        brand_name=(row[8]),
                    )
                    Detailtable.save()
                else:
                    next(reader)

        print("data parsed successfully")