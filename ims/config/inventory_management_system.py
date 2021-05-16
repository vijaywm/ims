from __future__ import unicode_literals
import frappe
from frappe import _


def get_data():
    return [
        {
            "label": _("Documents"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Item",
                    "description": _("Item"),
                    "label": _("Item"),
                },
            ],
        },
        {
            "label": _("Setup"),
            "items": [],
        },
        {
            "label": _("Reports"),
            "items": [
                {
                    "type": "report",
                    "name": "All Products",
                    "module_name": "Inventory Management System",
                    "label": _("All Products"),
                    "route": "#query-report/All Products",
                },
            ],
        },
    ]
