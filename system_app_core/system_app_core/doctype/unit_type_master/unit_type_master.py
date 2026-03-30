# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class UnitTypeMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allows_booking: DF.Check
		category: DF.Literal["Religious", "Commercial", "Residential", "Educational", "Land"]
		description: DF.SmallText | None
		is_active: DF.Check
		is_financial_unit: DF.Check
		is_rentable: DF.Check
		unit_code: DF.Data
		unit_type_name: DF.Data
	# end: auto-generated types

	pass
