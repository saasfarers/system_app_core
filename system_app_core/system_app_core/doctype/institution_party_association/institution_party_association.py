# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InstitutionPartyAssociation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		erp_customer: DF.Data | None
		erp_supplier: DF.Data | None
		financially_active: DF.Check
		from_date: DF.Date
		has_portal_access: DF.Check
		institution: DF.Link
		linked_employee: DF.Data | None
		name: DF.Int | None
		party: DF.Link
		relationship_type: DF.Literal["Devotee", "Donor", "Volunteer", "Employee", "Religious Leader", "Trustee", "Tenant", "Supplier", "Service Provider", "Beneficiary", "Student"]
		status: DF.Literal["Active", "Inactive"]
		to_date: DF.Date | None
	# end: auto-generated types

	pass
