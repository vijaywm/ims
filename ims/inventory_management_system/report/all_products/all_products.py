# Copyright (c) 2013, businessintel.in and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    from erpnext.stock.report.stock_balance.stock_balance import execute

    columns, data = execute(filters)
    return get_columns(columns), get_data(data)


def get_columns(columns):
    return [
        {
            "label": "SKU",
            "fieldname": "item_code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 300,
        },
        {"label": "Item Name", "fieldname": "item_name", "width": 250},
        {
            "label": "Item Group",
            "fieldname": "item_group",
            "fieldtype": "Link",
            "options": "Item Group",
            "width": 180,
        },
        {
            "label": "Warehouse",
            "fieldname": "warehouse",
            "fieldtype": "Link",
            "options": "Warehouse",
            "width": 140,
        },
        {
            "label": "Balance Qty",
            "fieldname": "bal_qty",
            "fieldtype": "Float",
            "width": 100,
            "convertible": "qty",
        },
        {
            "label": "Cost",
            "fieldname": "val_rate",
            "fieldtype": "Currency",
            "width": 150,
            "convertible": "rate",
            "options": "currency",
        },
    ]


def get_data(data):
    return data