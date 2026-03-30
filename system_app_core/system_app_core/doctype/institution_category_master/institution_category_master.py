# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InstitutionCategoryMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allows_financial: DF.Check
		allows_rental: DF.Check
		applies_to_faith: DF.Data | None
		category_code: DF.Data
		category_name: DF.Data
		description: DF.SmallText | None
		is_active_: DF.Check
		is_administrative_entity_: DF.Check
		is_property_entity_: DF.Check
		is_religious_entity_: DF.Check
	# end: auto-generated types

	pass
