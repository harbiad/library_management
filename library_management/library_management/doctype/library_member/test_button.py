# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):
     def test_bt(self):
        if self.first_name == 'Saad':
           # frappe.throw(
           # title='Error',
           # msg='You can not use this name "Saad!"',
           # exc=FileNotFoundError )
           frappe.msgprint(
                   msg='test button سعد',
                   title='Error',
                   raise_exception=FileNotFoundError)

