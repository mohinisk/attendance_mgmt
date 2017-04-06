# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "attedence_system"
app_title = "Attedence System"
app_publisher = "Frappe"
app_description = "App for employee attedence, keep track of employee in-time and out-time."
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@frappe.com	"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/attedence_system/css/attedence_system.css"
# app_include_js = "/assets/attedence_system/js/attedence_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/attedence_system/css/attedence_system.css"
# web_include_js = "/assets/attedence_system/js/attedence_system.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "attedence_system.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "attedence_system.install.before_install"
# after_install = "attedence_system.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "attedence_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events



doctype_js={
	"Attendance":["customization/attendance/attendance.js"]
}



doc_events = {
	"Attendance" :{
		"before_insert": "attedence_system.customization.attendance.attendance.check_leave_records"
		}
}




# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"conference_management.conference_management.doctype.conference_booking.conference_booking.conference_close",
		
# 	]
# }
# 	"daily": [
# 		"attedence_system.tasks.daily"
# 	],
# 	"hourly": [
# 		"attedence_system.tasks.hourly"
# 	],
# 	"weekly": [
# 		"attedence_system.tasks.weekly"
# 	]
# 	"monthly": [
# 		"attedence_system.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "attedence_system.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "attedence_system.event.get_events"
# }

fixtures = ["Custom Field", "Property Setter"]

