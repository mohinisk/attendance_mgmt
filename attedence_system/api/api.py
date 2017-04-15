from __future__ import unicode_literals
import json
import frappe

@frappe.whitelist(allow_guest=True)
def create_attendance_record(employee,att_date,time):
	print "\n\n\n\n\n\n employee",employee
	print "att_date",att_date
	print "time",time
	emp_name = frappe.db.get_value("Employee",{"name":employee},"employee_name")
	if emp_name :
		try:
			att_record = frappe.db.get_value("Attendance",{"att_date":att_date,"status":"Present","employee":employee},"name")
			if not att_record :
				attendance_doc = frappe.new_doc("Attendance")
				attendance_doc.employee = employee
				attendance_doc.att_date = att_date
				attendance_doc.save(ignore_permissions=True)
				#attendance_doc.submit()

			attendance_log = frappe.new_doc("Attendance Log")
			attendance_log.employee = employee
			attendance_log.att_date = att_date
			attendance_log.time = time
			attendance_log.save(ignore_permissions=True)
			print "attendance_log.name",attendance_log.name
			frappe.db.commit()
			return "Welcome",frappe.db.get_value("Employee",{"name":employee},"employee_name")
		except Exception, e:
			raise e
	else:
			return "Invalid Employee ID"
	

@frappe.whitelist(allow_guest=True)
def status_absent():
	emp_name = frappe.db.sql("""select employee, employee_name, company from `tabEmployee` where employee  NOT IN ( select employee from `tabAttendance` where att_date = "2017-04-06")""", as_dict=1)
	
	print "\n\n\n", emp_name 
	if emp_name:
		try:
			for emp_details in emp_name:
				print "----------\n\n\n", emp_details
				attendance_doc = frappe.new_doc("Attendance")
				attendance_doc.att_date = "2017-04-06"
				attendance_doc.employee = emp_details["employee"]          
				attendance_doc.employee_name = emp_details["employee_name"]        
				attendance_doc.company = emp_details["company"]	         
				attendance_doc.status = "Absent"
				attendance_doc.save(ignore_permissions=True)
				attendance_doc.submit()

		except Exception, e:
			print frappe.get_traceback()
			raise e

