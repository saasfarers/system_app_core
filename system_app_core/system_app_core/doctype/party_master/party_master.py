# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PartyMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from system_app_core.system_app_core.doctype.organisation.organisation import Organisation
		from system_app_core.system_app_core.doctype.person.person import Person

		can_be_customer: DF.Check
		can_be_donor: DF.Check
		can_be_employee: DF.Check
		can_be_supplier: DF.Check
		can_be_tenant: DF.Check
		can_be_volunteer: DF.Check
		email: DF.Data | None
		has_system_access: DF.Check
		mobile_number: DF.Data | None
		name: DF.Int | None
		organisation: DF.Table[Organisation]
		party_id: DF.Autocomplete
		party_name: DF.Data
		party_type: DF.Literal["Individual", "Organisation"]
		person: DF.Table[Person]
		status: DF.Literal["Active", "Inactive", "Blacklisted"]
	# end: auto-generated types

	pass
