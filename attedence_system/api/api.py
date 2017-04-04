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
def create_attendance_record(employee,att_date,in_time,out_time):
	attendance = frappe.new_doc("Attendance")
	attendance.employee = employee
	attendance.att_date = att_date
	print "in_time",in_time
	print "out_time",out_time

	attendance.append("timesheet", {
		"in_time": in_time,
		"out_time": out_time
	})
	attendance.save(ignore_permissions=True)
	
	#return attendance
