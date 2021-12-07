{
    'name': "Library App",
    'version': '12.0',
    'author': "Mohammed Bouqs",
    'license': 'AGPL-3',
    'summary': """This App provides library app.""",
    'depends': ['base',
                ],
    'data': [
        'views/library_menu.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/book_list_template.xml'
    ],
    'installable': True,
    'application': True,
}
