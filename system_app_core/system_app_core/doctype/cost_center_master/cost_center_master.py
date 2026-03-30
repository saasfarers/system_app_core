# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CostCenterMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		cost_center_code: DF.Data
		cost_center_name: DF.Data
		institution: DF.Data
		is_active: DF.Check
		is_group: DF.Check
		parent_cost_center: DF.Data | None
	# end: auto-generated types

	pass
