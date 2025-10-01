// Copyright (c) 2025, NightWalkAX and contributors
// For license information, please see license.txt

frappe.ui.form.on("Cheatsheet", {
	refresh(frm) {

	},

	language(frm) {
		// Swap title and alternative title
		if (frm.doc.title && frm.doc.title_alt) {
			let temp_title = frm.doc.title;
			frm.set_value('title', frm.doc.title_alt);
			frm.set_value('title_alt', temp_title);
		}

		// Swap fields in all items on the child table
		if (frm.doc.items && frm.doc.items.length > 0) {
			frm.doc.items.forEach(function(item) {
				// Swap description and description_alt
				if (item.description && item.description_alt) {
					let temp_desc = item.description;
					frappe.model.set_value(item.doctype, item.name, 'description', item.description_alt);
					frappe.model.set_value(item.doctype, item.name, 'description_alt', temp_desc);
				}

				// Swap example and example_alt
				if (item.example && item.example_alt) {
					let temp_example = item.example;
					frappe.model.set_value(item.doctype, item.name, 'example', item.example_alt);
					frappe.model.set_value(item.doctype, item.name, 'example_alt', temp_example);
				}
			});

			// Refresh the table to show changes
			frm.refresh_field('items');
		}
	}
});
