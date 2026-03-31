# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Organisation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business_type: DF.Literal[None]
		contact_person: DF.Link | None
		is_religious_org: DF.Check
		legal_name: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		registration_no: DF.Data | None
		tax_id: DF.Data | None
	# end: auto-generated types

	pass
