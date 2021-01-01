# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


# will override the implementation of writing file to disk
# can be used to upload files to a CDN instead of writing
# the file to disk
def write_file():
    frappe.throw(
           title='Error',
           msg='You can not use this name "Saad!"',
           exc=FileNotFoundError )


#    frappe.msgprint(
#                    msg='This file does not exist سعد',
#                    title='Error',
#                    raise_exception=FileNotFoundError)
#    pass

# will run before file is written to disk
def before_write():
    frappe.msgprint(
                    msg='before write سعد',
                    title='Error',
                    raise_exception=FileNotFoundError)
