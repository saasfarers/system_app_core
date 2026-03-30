# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GovernanceTypeMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.SmallText | None
		election_based: DF.Check
		governance_code: DF.Data
		governance_name: DF.Data
		has_trustees: DF.Check
		is_active: DF.Check
		term_duration: DF.Int
	# end: auto-generated types

	pass
