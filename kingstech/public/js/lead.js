
frappe.ui.form.on('Lead', {
    refresh:function(frm){
        
    },
    lead_date(frm) {
        if(frm.doc.lead_date){
            frappe.call({
                method:"kingstech.api.get_date_validation",
                args:{
                    lead_date : frm.doc.lead_date
                },
                callback:function(r){
                    if(r.message){
                        frappe.throw(r.message)
                    }
                }
            })
        }
	}
})