# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Person(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.SmallText | None
		date_of_birth: DF.Date | None
		family: DF.Data | None
		first_name: DF.Data | None
		last_name: DF.Data | None
		marital_status: DF.Literal["Married", "Unmarried"]
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		select_gjnt: DF.Literal["Male", "Female"]
	# end: auto-generated types

	pass
