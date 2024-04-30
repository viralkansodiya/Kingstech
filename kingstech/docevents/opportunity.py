import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_in_shop_training(source_name):
    doc = get_mapped_doc(
		"Opportunity",
		source_name,
		{
			"Opportunity": {
				"doctype": "Training Event",
				"field_map": {
                    },
			}
		},
		ignore_permissions=True,
	)
    return doc