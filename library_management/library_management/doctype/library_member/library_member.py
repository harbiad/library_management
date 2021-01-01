# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LibraryMember(Document):

      def testbt(self):
           if self.first_name == 'Saad':
           # frappe.throw(
           # title='Error',
           # msg='You can not use this name "Saad!"',
           # exc=FileNotFoundError )
               frappe.msgprint(
                   msg='test button سعد',
                   title='Error',
                   raise_exception=FileNotFoundError)




      def validate(self):
         if self.first_name == 'Saad':
           # frappe.throw(
           # title='Error',
           # msg='You can not use this name "Saad!"',
           # exc=FileNotFoundError )
           frappe.msgprint(
                   msg='This name does not exist سعد',
                   title='Error',
                   raise_exception=FileNotFoundError)
           self.first_name = "SSSS"
#           frappe.msgprint("hey done!")
#            frappe.msgprint("test")
           # frappe.throw('Name can not be Saad')
#      pass
     # this method will run every time a document is saved
      def before_save(self):
         self.full_name = f'{self.first_name} {self.last_name or ""}'
#	pass

