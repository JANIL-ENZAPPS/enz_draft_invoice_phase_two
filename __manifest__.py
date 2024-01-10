# -*- coding: utf-8 -*-
{
    'name': "KSA Zatca Phase-2",
    'summary': """
        Phase-2 of ZATCA e-Invoicing(Fatoorah): Integration Phase, its include solution for KSA business""",
    'description': """
        Phase-2 of ZATCA e-Invoicing(Fatoorah): Integration Phase, its include solution for KSA business
    """,
    'live_test_url': 'https://youtu.be/_M3PtOBzeC4',
    "author": "Enzapps Private Limited",
    "website": "www.enzapps.com",
    'license': 'AGPL-3',
    'images': ['static/description/icon.png'],
    'category': 'Invoicing',
    'version': '14.0',
    'price': 399, 'currency': 'USD',
    'depends': ['account', 'sale', 'l10n_sa_invoice', 'purchase', 'account_debit_note','enz_ksa_phase_two_zatca'],
    'external_dependencies': {
        'python': ['cryptography', 'lxml', 'qrcode']
    },
    'data': [
    ],
}