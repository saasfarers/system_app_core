# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FundCategoryMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		default__expense_account: DF.Data | None
		default_cost_center: DF.Data | None
		default_income_account: DF.Data | None
		default_liabliity_account: DF.Data | None
		description: DF.SmallText | None
		faith_applicability: DF.Data | None
		faith_applicability_copy: DF.Data | None
		fund_category_id: DF.Data | None
		fund_category_name: DF.Data | None
		fund_nature: DF.Literal[None]
		fund_nature_copy: DF.Literal[None]
		income_type: DF.Literal[None]
		income_type_copy: DF.Literal[None]
		is_active: DF.Check
		linked_to_event_types: DF.Data | None
		recurrence_type: DF.Literal[None]
		recurrence_type_copy: DF.Literal[None]
		requires_donor_declaration: DF.Check
		requires_event_referance: DF.Check
		restriction_type: DF.Literal[None]
		restriction_type_copy: DF.Literal[None]
		short_code: DF.Data | None
		supports_anonymous_donation: DF.Check
	# end: auto-generated types

	pass
