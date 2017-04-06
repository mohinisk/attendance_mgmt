from __future__ import unicode_literals
import json
import frappe

@frappe.whitelist(allow_guest=True)
def get_user_details():
	try:
		response = frappe._dict({})
		data = [{ 'name': u'mohini.k@indictranstech.com'}]
		response.data = data
		response.message = "user"
		print data
		return response
	except Exception, e:
		print frappe.get_traceback()
		raise e

@frappe.whitelist(allow_guest=True)
def get_users_details(email,first_name):
	print "&&&&$$$$$$"
	print "email",email
	print "first name",first_name
	user = frappe.new_doc("User")
	user.email = email
	user.first_name = first_name
	#print user
	user.insert()
	return user
	#user.submit()

@frappe.whitelist(allow_guest=True)
def create_attendance_record(employee,att_date,time):
	emp_name = frappe.db.get_value("Employee",{"name":employee},"employee_name")
	if emp_name :
		try:
			attendance_doc = frappe.new_doc("Attendance")
			attendance_doc.employee = employee
			attendance_doc.att_date = att_date

			attendance_log = frappe.new_doc("Attendance Log")
			attendance_log.employee = employee
			attendance_log.att_date = att_date
			attendance_log.time = time

			attendance_doc.save(ignore_permissions=True)
			attendance_log.save(ignore_permissions=True)

			

			return "success"
		except Exception, e:
			print frappe.get_traceback()
			raise e

	else:
		print "Invalid Employee ID"
		return "Invalid Employee ID"