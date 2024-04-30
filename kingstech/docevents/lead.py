import frappe
from frappe.model.mapper import get_mapped_doc
from kingstech.api import get_date_validation
from frappe.utils import (
	add_days,
	add_months,
	add_years,
	cint,
	cstr,
	date_diff,
	flt,
	formatdate,
	get_last_day,
	get_timestamp,
	getdate,
	nowdate,
)
from datetime import datetime , timedelta
@frappe.whitelist()
def make_in_shop_training(source_name):
    doc = get_mapped_doc(
        "Lead",
        source_name,
        {
            "Lead": {
                "doctype": "Training Event",
                "field_map": {
                    },
            }
        },
        ignore_permissions=True,
    )
    return doc

def validate(self, method):
    lead_date = self.lead_date
    currentDate = nowdate()
    date_before_6_days = getdate(currentDate) - timedelta(days= 6)

    date_before_6_days = datetime.strptime(str(date_before_6_days), "%Y-%m-%d")
    currentDate = datetime.strptime(str(currentDate), "%Y-%m-%d")
    lead_date = datetime.strptime(str(lead_date), "%Y-%m-%d")
    

    if not (date_before_6_days <= lead_date <= currentDate):
        frappe.throw("Date of visit should be between {0} and {1}".format(frappe.format(getdate(date_before_6_days)), frappe.format(getdate(currentDate))))