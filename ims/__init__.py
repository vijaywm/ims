# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = "0.0.1"


@frappe.whitelist(allow_guest=True)
def items(format=None):
    return frappe.db.sql("select name from tabUser", as_dict=True)