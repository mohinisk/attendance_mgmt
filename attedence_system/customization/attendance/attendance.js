// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.ui.form.on("Attendance", "validate", function(frm, dt, dn) {


	var total_time_spent = 0;

	$.each(cur_frm.doc.timesheet,function(i,d){

		if(d.in_time && d.out_time){	
			if(d.in_time > d.out_time){
				msgprint(__("Start Time should not be greater than End Time"));
				validated = false;
			}
		}	

  		var diff =  moment.utc(moment(d.out_time,"HH:mm:ss").diff(moment(d.in_time,"HH:mm:ss"))).format("HH:mm:ss")
		
		frappe.model.set_value(d.doctype, d.name, "working_hour", diff);
		
		var startTime=moment(d.in_time, "HH:mm:ss");
		var endTime=moment(d.out_time, "HH:mm:ss");
		var duration = moment.duration(endTime.diff(startTime));
				
		var seconds = parseInt(duration.asSeconds());
		
		total_time_spent += seconds;
		
	})
	var hh_mm_ss = convert_hhmmss(total_time_spent);

	frappe.model.set_value(dt, dn, "total_working_", hh_mm_ss );

	var hours = get_hours(hh_mm_ss);


	
});

convert_hhmmss = function(total_time_spent) {
		
		var h = Math.floor(total_time_spent / 3600);
		var m = Math.floor((total_time_spent - (h * 3600)) / 60);
		var s = total_time_spent - (h * 3600) - (m * 60);

		  // round seconds
		s = Math.round(s * 100) / 100

		var result = (h < 10 ? "0" + h : h);
		    result += ":" + (m < 10 ? "0" + m : m);
		    result += ":" + (s < 10 ? "0" + s : s);

  		return result;  			
},

get_hours = function(hh_mm_ss){
	
	if (hh_mm_ss.value !== ""){
		var hours = hh_mm_ss.split(":")[0];
		return hours;
	}
},

leave_status = function(frm){
		frappe.call({
				method: "attedence_system.customization.attendance.attendance.leave_status"
		})
				
	}
