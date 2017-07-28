"""Contains a bunch of data for the tests"""

testdata = {'creator': {'bio': "Don't let your dreams be dreams", 'title': 'Chief Strategist', 'owner': True, 'admin': True, 'company': {'name': 'Honcho Design', 'id': 1033447817}, 'created_at': '2016-09-22T16:21:03.625-05:00', 'name': 'Test User', 'personable_type': 'User', 'email_address': 'victor@honchodesign.com', 'attachable_sgid': 'BAh7CEkiCGdpZAY6BkVUSSIrZ2lkOi8vYmMzL1BlcnNvbQQcMDA3Mjk5MTQzP2V4cGlyZXNfaW4GOwBUSSIMcHVycG9zZQY7AFRJIg9hdHRhY2hhYmxlBjsAVEkiD2V4cGlyZXNfYXQGOwBUMA==--919d2c8b11ff403eefcab9db42dd26846d0c3102', 'updated_at': '2016-09-22T16:21:06.184-05:00', 'id': 1007299143, 'time_zone': 'America/Chicago', 'avatar_url': 'https://3.basecamp-static.com/195539477/people/BAhpBEcqCjw=--c632b967cec296b87363a697a67a87f9cc1e5b45/avatar-64-x4'}, 'command': 'testcommand testargument', 'callback_url': 'https://localhost/callback'}

testdata_notfound = {'creator': {'bio': "Don't let your dreams be dreams", 'title': 'Chief Strategist', 'owner': True, 'admin': True, 'company': {'name': 'Honcho Design', 'id': 1033447817}, 'created_at': '2016-09-22T16:21:03.625-05:00', 'name': 'Test User', 'personable_type': 'User', 'email_address': 'victor@honchodesign.com', 'attachable_sgid': 'BAh7CEkiCGdpZAY6BkVUSSIrZ2lkOi8vYmMzL1BlcnNvbQQcMDA3Mjk5MTQzP2V4cGlyZXNfaW4GOwBUSSIMcHVycG9zZQY7AFRJIg9hdHRhY2hhYmxlBjsAVEkiD2V4cGlyZXNfYXQGOwBUMA==--919d2c8b11ff403eefcab9db42dd26846d0c3102', 'updated_at': '2016-09-22T16:21:06.184-05:00', 'id': 1007299143, 'time_zone': 'America/Chicago', 'avatar_url': 'https://3.basecamp-static.com/195539477/people/BAhpBEcqCjw=--c632b967cec296b87363a697a67a87f9cc1e5b45/avatar-64-x4'}, 'command': 'asdfjklasdfwerqa that will never have a function', 'callback_url': 'https://localhost/callback'}

testjson = """{
  "command": "testcommand testargument",
  "creator": {
    "id": 1007299143,
    "attachable_sgid": "BAh7CEkiCGdpZAY6BkVUSSIrZ2lkOi8vYmMzL1BlcnNvbQQcMDA3Mjk5MTQzP2V4cGlyZXNfaW4GOwBUSSIMcHVycG9zZQY7AFRJIg9hdHRhY2hhYmxlBjsAVEkiD2V4cGlyZXNfYXQGOwBUMA==--919d2c8b11ff403eefcab9db42dd26846d0c3102",
    "name": "Test User",
    "email_address": "victor@honchodesign.com",
    "personable_type": "User",
    "title": "Chief Strategist",
    "bio": "Don't let your dreams be dreams",
    "created_at": "2016-09-22T16:21:03.625-05:00",
    "updated_at": "2016-09-22T16:21:06.184-05:00",
    "admin": true,
    "owner": true,
    "time_zone": "America/Chicago",
    "avatar_url": "https://3.basecamp-static.com/195539477/people/BAhpBEcqCjw=--c632b967cec296b87363a697a67a87f9cc1e5b45/avatar-64-x4",
    "company": {
      "id": 1033447817,
      "name": "Honcho Design"
    }
  },
  "callback_url": "https://localhost/callback"
}"""
