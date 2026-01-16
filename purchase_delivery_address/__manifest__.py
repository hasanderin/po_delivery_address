{
    'name': 'Purchase Delivery Address',
    'version': '15.0.1.0.0',
    'category': 'Inventory/Purchase',
    'summary': 'Selectable Delivery Address on Purchase Orders',
    'description': """
        This module adds a 'Delivery Address' field to Purchase Orders.
        It allows users to specify a delivery partner address different from
        the default warehouse address.
    """,
    'author': 'Antigravity',
    'depends': ['purchase', 'stock'],
    'data': [
        'views/purchase_order_view.xml',
        'reports/purchase_order_templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
