# Copyright (c) 2025, NightWalkAX and contributors
# For license information, please see license.txt

import frappe

from doctyped_cheatsheets.doctyped_cheatsheets.src.process_cheatsheets import (
    save_to_frappe,
)


def after_install():
    """
    This function is executed automatically after installing the app.
    Loads all cheatsheets from JSON files.
    """
    print("\n" + "="*60)
    print("Installing Doctyped Cheatsheets...")
    print("="*60 + "\n")

    try:
        save_to_frappe()
        print("\n✓ Cheatsheets installed successfully!")
    except Exception as e:
        print(f"\n✗ Error installing cheatsheets: {e!s}")
        frappe.log_error(
            message=frappe.get_traceback(),
            title="Cheatsheets Installation Error"
        )
        # No hacemos raise para no bloquear la instalación completa de la app
        print(
            "Installation completed with errors. "
            "Check Error Log for details."
        )

    print("="*60 + "\n")
