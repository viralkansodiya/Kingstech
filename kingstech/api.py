import os
import frappe
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

def get_extention(self,method):
    split_tup = os.path.splitext(self.file_url)
    file_extantion = split_tup[1]
    if file_extantion not in [".PDF",".pdf"] and self.attached_to_doctype in ["Lead",'Draft BAS','Cases Facilitated','Primary BAS','Opportunity']:
        frappe.throw("Only <b>.pdf</b> files are allowed as attachments. Please remove or replace the files")


@frappe.whitelist()
def get_date_validation(lead_date):
    currentDate = nowdate()
    date_before_6_days = getdate(currentDate) - timedelta(days= 6)

    date_before_6_days = datetime.strptime(str(date_before_6_days), "%Y-%m-%d")
    currentDate = datetime.strptime(str(currentDate), "%Y-%m-%d")
    lead_date = datetime.strptime(str(lead_date), "%Y-%m-%d")
    

    if not (date_before_6_days <= lead_date <= currentDate):
        return "Date of visit should be between {0} and {1}".format(frappe.format(getdate(date_before_6_days)), frappe.format(getdate(currentDate)))


