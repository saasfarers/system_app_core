# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FaithMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		default_governance_model: DF.Data | None
		description: DF.SmallText | None
		faith_code: DF.Data
		faith_name: DF.Data
		has_denominations_: DF.Check
		is_active_: DF.Check
	# end: auto-generated types

	pass
