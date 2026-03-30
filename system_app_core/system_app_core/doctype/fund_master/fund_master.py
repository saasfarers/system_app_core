# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class FundMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		default_expense_account: DF.Data | None
		default_income_account: DF.Data | None
		default_liabliity_account: DF.Data | None
		effective_from: DF.Date
		fund_category: DF.Data
		fund_code: DF.Data
		fund_name: DF.Data
		institution: DF.Data
		is_active: DF.Check
		is_restricted: DF.Check
		opening_balance: DF.Currency
	# end: auto-generated types

	pass
