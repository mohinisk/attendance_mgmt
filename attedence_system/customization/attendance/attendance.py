# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

from frappe.utils import getdate, nowdate
from frappe import _
from frappe.model.document import Document
# from erpnext.hr.utils import set_employee_name

def check_leave_records(self, method):
		#this is done to check if employee applied has applied for half-day leave or leave
		#while creating Attendance Log
	if self.status == 'Present':
		leave = frappe.db.sql("""select name,  half_day  from `tabLeave Application`
			where employee = %s and %s between from_date and to_date and status = 'Approved'
			and docstatus = 1""", (self.employee, self.att_date), as_dict=1)
		
		if leave:
			if leave[0]["half_day"] == 1:
				frappe.db.set(self, 'status', "Half Day")
			else:
				frappe.throw(_("Employee {0} was on leave on {1}. Cannot mark attendance.").format(self.employee,
					self.att_date))