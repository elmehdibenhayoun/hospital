{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Manage hospital patients, doctors, appointments, departements, rooms, equipments, operations, and invoices',
    'sequence': -100,
    'description': """Hospital management system""",
    'category': 'Healthcare',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
        'views/hospital_appointment_views.xml',
        'views/hospital_departement_views.xml',
        'views/hospital_room_views.xml',
        'views/hospital_equipement_views.xml',
        'views/hospital_operation_views.xml',
        'views/hospital_facture_views.xml',
        'views/menus.xml',
       # 'views/hospital_report_views.xml',
        'views/hospital_report_views.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
