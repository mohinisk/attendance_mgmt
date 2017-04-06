from __future__ import unicode_literals
import json
import frappe
from uuid import getnode as get_mac


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
def create_attendance_record(mac,employee,att_date,time_log):
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
				attendance_log.append("time" , {
					"time_log" : time_log
				})
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

# @frappe.whitelist()
# def submit_attendance_for_day():
# submit_att = frappe.get_all("Conference booking",filters={'workflow_state':"Booked"})
# for i in range(0,len(Book_conf)):
# 	conf_date = frappe.get_value("Conference booking", Book_conf[i]['name'], "date")
# 	conf_to_time = frappe.get_value("Conference booking", Book_conf[i]['name'], "to_time")
# 	conf_datetime = str(conf_date)+" "+str(conf_to_time)
# 	conf_datetime1 = frappe.utils.data.get_datetime(conf_datetime)
# 	current_datetime = frappe.utils.data.now_datetime()
# 	diff=frappe.utils.data.time_diff_in_hours(conf_datetime1,current_datetime)

# 	if diff<0:
# 		close_conf=frappe.db.sql("""update `tabConference booking` set workflow_state='Closed' where name=%s""",(Book_conf[i]['name']))