from __future__ import unicode_literals
import json
import frappe
from uuid import getnode as get_mac


@frappe.whitelist(allow_guest=True)
def create_attendance_record(mac,employee,att_date,time):
	mac1 = get_mac()
	print "MAC1",type(long(mac1))
	print "MAC",type(long(mac))
	if long(mac) == long(mac1):
		emp_name = frappe.db.get_value("Employee",{"name":employee},"employee_name")
		if emp_name :
			try:
				att_record = frappe.db.get_value("Attendance",{"att_date":att_date,"status":"Present","employee":employee},"name")
				print "att_record",att_record
				if not att_record :
					attendance_doc = frappe.new_doc("Attendance")
					attendance_doc.employee = employee
					attendance_doc.att_date = att_date
					attendance_doc.save(ignore_permissions=True)

				attendance_log = frappe.new_doc("Attendance Log")
				attendance_log.employee = employee
				attendance_log.att_date = att_date
				attendance_log.time = time
				attendance_log.save(ignore_permissions=True)
				#attendance_doc.submit()
				#attendance_log.submit()
				return "success"
			except Exception, e:
				print frappe.get_traceback()
				raise e
		else:
			print "Invalid Employee ID"
			return "Invalid Employee ID"
	else:

		return "INVALID user"
