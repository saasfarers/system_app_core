# Copyright (c) 2026, saasfarers and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InstitutionMaster(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.Data | None
		allow_independent_bank_accounts: DF.Check
		allow_independent_budgeting: DF.Check
		can_own_assets: DF.Check
		can_run_educational_programs: DF.Check
		contact: DF.Data | None
		cost_center: DF.Data | None
		country: DF.Data | None
		default_currency: DF.Data | None
		default_donation_fund: DF.Data | None
		default_expense_fund: DF.Data | None
		election_cycle: DF.Data | None
		faith: DF.Data | None
		governance_type: DF.Data | None
		governing_body_name: DF.Data | None
		has_paid_staff: DF.Check
		has_volunteer_network: DF.Check
		head_of_institution: DF.Data | None
		hierarchy_level: DF.Int
		institution_category: DF.Data
		institution_code: DF.Data
		institution_id: DF.Autocomplete
		institution_logo: DF.AttachImage | None
		institution_name: DF.Data
		is_donation_accepting_unit: DF.Check
		is_expense_booking_unit: DF.Check
		is_financially_autonomous: DF.Check
		is_operational_unit: DF.Check
		is_record_only_unit: DF.Check
		is_registered_legal_entity: DF.Check
		is_rentable_asset_holder: DF.Check
		legal_name: DF.Data | None
		legal_structure_type: DF.Data | None
		number_of_trustees: DF.Int
		parent_institution: DF.Data | None
		registration_number: DF.Data | None
		status: DF.Literal[None]
		supports_multi_fund_accounting: DF.Check
		tax_id: DF.Data | None
		time_zone: DF.Data
		year_established: DF.Int
	# end: auto-generated types

	pass
