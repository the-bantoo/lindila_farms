import frappe
from frappe import _

@frappe.whitelist()
def leave_application(name):
    doc = frappe.get_doc("Attendance", name)
    employee = frappe.get_doc('Employee', doc.employee)
    
    new_application = frappe.get_doc({
        "doctype": "Leave Application",
        "leave_type": "Leave Without Pay",
        "employee": doc.employee,
        "from_date":doc.attendance_date,
        "to_date":doc.attendance_date,
        "leave_approver":employee.leave_approver
    })
    new_application.insert()