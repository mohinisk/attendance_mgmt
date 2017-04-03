// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt


frappe.ui.form.on("Attendance", "validate", function(frm) {

		
	var total_time_spent = 0;

	var a = convert_hhmmss();
	
	$.each(cur_frm.doc.timesheet,function(i,d){

  		var diff =  moment.utc(moment(d.out_time,"HH:mm:ss").diff(moment(d.in_time,"HH:mm:ss"))).format("HH:mm:ss")
		
		frappe.model.set_value(d.doctype, d.name, "working_hour", diff);
		
		var startTime=moment(d.in_time, "HH:mm:ss");
		var endTime=moment(d.out_time, "HH:mm:ss");
		var duration = moment.duration(endTime.diff(startTime));
				
		var seconds = parseInt(duration.asSeconds());
		console.log("seconds---",seconds);
		
		total_time_spent += seconds;
		
	}),
console.log(" total time ",total_time_spent);

convert_hhmmss: function(total_time_spent) {
		
		var h = Math.floor(seconds / 3600);
		var m = Math.floor((seconds - (hours * 3600)) / 60);
		var s = seconds - (hours * 3600) - (minutes * 60);

		  // round seconds
		seconds = Math.round(seconds * 100) / 100

		  var result = (h < 10 ? "0" + hours : hours);
		      result += "-" + (m < 10 ? "0" + minutes : minutes);
		      result += "-" + (s < 10 ? "0" + seconds : seconds);
  			return result;

  			console.log("hhmmss-----", result);
}

});

