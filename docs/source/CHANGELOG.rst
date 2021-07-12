
Changelog
=========

1.2.0 - 2021-07-12
------------------

Changed
^^^^^^^

* Remove default value in the parameters


1.1.1 - 2021-06-24
------------------

Changed
^^^^^^^

* Upgrade the dependency packages


1.1.0 - 2021-06-23
------------------

Added
^^^^^


* A link to the document on ``README.md``
* Enabled the sub menu on document nav bar.
* ``GET /sapi/v1/lending/daily/product/list`` includes new parameters, current and size.
* New endpoints for Sub-Account:

  * ``POST /sapi/v1/managed-subaccount/deposit`` to deposit assets into the managed sub-account (only for investor master account)
  * ``GET /sapi/v1/managed-subaccount/asset`` to query managed sub-account asset details (only for investor master account)
  * ``POST /sapi/v1/managed-subaccount/withdraw`` to withdrawal assets from the managed sub-account (only for investor master account)

1.0.0 - 2021-06-15
------------------

Added
^^^^^


* First release, please find details from ``README.md``
