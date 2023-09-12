import frappe

@frappe.whitelist(allow_guest=True)
def login(**kwargs):
    try:
        usr, pwd, cmd = frappe.form_dict.values()
        auth = frappe.auth.LoginManager()
        auth.authenticate(user=usr, pwd=pwd)
        auth.post_login()
        msg={
        'status_code':200,
        'text':frappe.local.response.message,
        'csrf_token':frappe.sessions.get_csrf_token(),
         'sid': frappe.session.sid
        }
        users = frappe.get_doc('User', frappe.session.user)
        msg['info'] = users
        return msg
    except frappe.exceptions.AuthenticationError:
        return {'status_code':401, 'text':frappe.local.response.message}
    except Exception as e:
        return {'status_code':500, 'text':str(e)}