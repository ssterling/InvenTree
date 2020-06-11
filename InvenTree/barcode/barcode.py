# -*- coding: utf-8 -*-

import hashlib
import json

from InvenTree import plugins as InvenTreePlugins
from barcode import plugins as BarcodePlugins

from stock.serializers import StockItemSerializer, LocationSerializer
from part.serializers import PartSerializer


def hash_barcode(barcode_data):
    """
    Calculate an MD5 hash of barcode data
    """

    hash = hashlib.md5(str(barcode_data).encode())
    return str(hash.hexdigest())


class BarcodePlugin:
    """
    Base class for barcode handling.
    Custom barcode plugins should extend this class as necessary.
    """

    # Override the barcode plugin name for each sub-class
    PLUGIN_NAME = ""

    @property
    def name(self):
        return self.PLUGIN_NAME

    def __init__(self, barcode_data):

        self.data = barcode_data

    def getStockItem(self):
        """
        Attempt to retrieve a StockItem associated with this barcode.
        Default implementation returns None
        """

        return None

    def renderStockItem(self, item):
        """
        Render a stock item to JSON response
        """

        serializer = StockItemSerializer(item, part_detail=True, location_detail=True, supplier_part_detail=True)
        return serializer.data


    def getStockLocation(self):
        """
        Attempt to retrieve a StockLocation associated with this barcode.
        Default implementation returns None
        """

        return None

    def renderStockLocation(self, loc):
        """
        Render a stock location to a JSON response
        """

        serializer = LocationSerializer(loc)
        return serializer.data

    def getPart(self):
        """
        Attempt to retrieve a Part associated with this barcode.
        Default implementation returns None
        """

        return None 

    def renderPart(self, part):
        """
        Render a part to JSON response
        """

        serializer = PartSerializer(part)
        return serializer.data

    def hash(self):
        """
        Calculate a hash for the barcode data.
        This is supposed to uniquely identify the barcode contents,
        at least within the bardcode sub-type.

        The default implementation simply returns an MD5 hash of the barcode data,
        encoded to a string.

        This may be sufficient for most applications, but can obviously be overridden
        by a subclass.

        """

        return hash_barcode(self.data)

    def validate(self):
        """
        Default implementation returns False
        """
        return False


def load_barcode_plugins(debug=False):
    """
    Function to load all barcode plugins
    """

    if debug:
        print("Loading barcode plugins")

    plugins = InvenTreePlugins.get_plugins(BarcodePlugins, BarcodePlugin)

    if debug:
        if len(plugins) > 0:
            print("Discovered {n} plugins:".format(n=len(plugins)))

            for p in plugins:
                print(" - {p}".format(p=p.PLUGIN_NAME))
        else:
            print("No barcode plugins found")

    return plugins