
Helper Classes
==============

This part of the documentation covers all classes and public methods.

Site
----

Controls the details of the program execution.

.. autoclass:: wallymart.site.pages.Pages
   :members:
   :inherited-members:

.. autoclass:: wallymart.site.portal.customer_portal.CustomerPortal
   :members:

.. autoclass:: wallymart.site.portal.employee_portal.EmployeePortal
   :members:

Startup
-------

Startup module that configures required items used throughout the lifecycle of the program.

.. autoclass:: wallymart.startup.database_configurator.DatabaseConfigurator
   :members:

.. autoclass:: wallymart.startup.logger_configurator.LoggerConfigurator
   :members:

Utils
-----

Utilities used by Pages or the collection objects in ORM.

.. autoclass:: wallymart.utils.database_connection.DatabaseConnection
   :members:

.. autoclass:: wallymart.utils.shopping_cart.ShoppingCart
   :members:

.. autoclass:: wallymart.utils.credential_encoder.CredentialEncoder
   :members:

ORM
---

Container classes to store information prior to being written to the database.

.. autoclass:: wallymart.orm.credentials.Credentials
   :members:

.. autoclass:: wallymart.orm.customer.Customer
   :members:

.. autoclass:: wallymart.orm.employee.Employee
   :members:

.. autoclass:: wallymart.orm.order_item.OrderItem
   :members:

.. autoclass:: wallymart.orm.product.Product
   :members:

.. autoclass:: wallymart.orm.review.Review
   :members: