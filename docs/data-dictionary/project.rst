Project
=======

General Overview
----------------

Names
^^^^^


.. datadictionary::
   :schema: project.json
   :path: /properties/name

.. datadictionary::
   :schema: project.json
   :path: /properties/alternative_names


Stage of Development
^^^^^^^^^^^^^^^^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/stage_development


Jurisdiction
^^^^^^^^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/jurisdiction

Dates
^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/dates

Overall project finance
^^^^^^^^^^^^^^^^^^^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/overall_project_finance

Purpose and classifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/purpose_and_classifications

Service and beneficiaries
^^^^^^^^^^^^^^^^^^^^^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/service_and_beneficiaries

Changes to project due to COVID-19
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. datadictionary::
   :schema: project.json
   :path: /properties/changes_to_project_due_to_covid19

Outcome Funds
-------------




Delivery Locations
------------------


.. datadictionary::
   :schema: project.json
   :path: /properties/delivery_locations/items


Sources
-------


.. datadictionary::
   :schema: project.json
   :path: /properties/sources/items


Organisations
-------------





Service Provisions
------------------



.. datadictionary::
   :schema: project.json
   :path: /properties/service_provisions/items


Outcome Payment Commitments
---------------------------

.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_payment_commitments/items


Investments
-----------



.. datadictionary::
   :schema: project.json
   :path: /properties/investments/items

Intermediary services
---------------------


.. datadictionary::
   :schema: project.json
   :path: /properties/intermediary_services/items

Outcome Metrics
---------------


.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_metrics/items

Outcome Pricing
---------------


.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_pricings/items


Grants
------


.. datadictionary::
   :schema: project.json
   :path: /properties/grants/items



Results
-------


.. datadictionary::
   :schema: project.json
   :path: /properties/results/items

Outcome Payments
----------------


.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_payments/items


Open Contracting
----------------


.. datadictionary::
   :schema: project.json
   :path: /properties/open_contracting_datas/items

360Giving
---------


.. datadictionary::
   :schema: project.json
   :path: /properties/360giving_datas/items

Documents
---------


.. datadictionary::
   :schema: project.json
   :path: /properties/documents/items


Social Investment Prototype
---------------------------


The Social Investment Prototype offers additional tabs to describe technical assistance and the financial aspects of projects in greater detail, including individual transactions.


On the `General Overview` tab:

.. datadictionary::
   :schema: project.json
   :path: /properties/social_investment_prototype


Investment Details
^^^^^^^^^^^^^^^^^^

Expected and latest internal rates of return can be recorded on the investment details tab (This may be in the general overview tab).


.. datadictionary::
   :schema: project.json
   :path: /properties/investment_details


Transactions
^^^^^^^^^^^^

The transactions tab is designed as a ledger of money in and money out of a project.

A transaction is modelled with a sending organisation and a receiving organisation, a date and an amount. These fields are required.

The value of a transaction (`Amount`) must be positive.

A transaction can be linked to the project as a whole (the default) or to a:

* Outcome payment (using the Outcome Metric ID column to link to the relevant row on the Outcome Metrics tab);
* Investment (using the Investment ID column to link to the relevant row on the Investment tab); or,
* Grant (using the Grant ID column to link to the relevant row on the Grants tab).

Only **one** of these IDs should appear per row, i.e. transactions should be disaggregated where possible. This is particularly important if the data is to be used in further analysis or visualisations.

The transaction type field is used to identify the purpose of the transaction.

The formatting rules on dates and currency values should be followed.

.. datadictionary::
   :schema: project.json
   :path: /properties/transactions/items


Technical Assistance
^^^^^^^^^^^^^^^^^^^^

Technical Assistance is modelled as a period of engagement between a funding organisation and a recipient organisation with a defined start and end date.

This period of engagement can be broken down on the Technical Assistance Details tab into a series of component activities (as well as high-level information that covers the whole engagement where appropriate).

An activity is linked to an engagement by using the relevant `id` from the `Technical Assistance` tab. Multiple activities can be linked to a single engagement.

Data should not be provided if no technical assistance from a given category has been given, i.e., zero values are not necessary but assumed in the absence of data.

Each activity can be assigned a cost and a cost type and a time cost in days.

Where no cost is available, or where a cost is inappropriate, a row can be added with the relevant category selected and the value and cost type fields left blank. This will allow activities to be analysed as simple counts.

Activities can be further classified by the delivery approach.

On the `Technical Assistance` tab:

.. datadictionary::
   :schema: project.json
   :path: /properties/technical_assistances/items

On the `Technical Assistance Details` tab:

.. datadictionary::
   :schema: project.json
   :path: /properties/technical_assistance_details/items

