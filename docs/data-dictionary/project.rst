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

Most finance variables will be converted into US dollars. The GO Lab team does the conversion using the yearly exchange rate provided by the World Bank, using the start year of service delivery as a reference.

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

If the project started, or was delivering services in or after March 2020, it may have experienced some changes due to the COVID-19 pandemic.  

.. datadictionary::
   :schema: project.json
   :path: /properties/changes_to_project_due_to_covid19

Outcome Funds
-------------

There is no standard or agreed definition as to what constitutes an 'outcomes fund'. Broadly, an outcomes fund is an approach that enables several outcomes-based contracts to be developed and supported in parallel. A common goal espoused by outcomes fund developers is to improve services that tackle complex social issues by growing the outcomes contracting market particularly by funding impact bonds and other payment-by-results mechanisms. In their broadest sense outcomes funds signal a commitment to pay for social outcomes, rather than inputs or activities.

When viewing data, other variables from the fund data model may be included to provide more information. See :doc:`the Fund data dictionary <fund>` for more information on what these variables mean.

.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_funds/items


Delivery Locations
------------------

This is a list. One project can have multiple items of data, as one project can deliver services in many different places at the same time. One item of data is defined as: 

.. datadictionary::
   :schema: project.json
   :path: /properties/delivery_locations/items


Sources
-------

This is a list. One project can have multiple items of data, as we may use multiple sources of information to populate one project spreadsheet. One item of data is defined as:

.. datadictionary::
   :schema: project.json
   :path: /properties/sources/items


Organisations
-------------

The organisations listed are those referenced in other tabs of the spreadsheet (such as service providers, investors, outcome payers, etc.). Each organisation has a unique INDIGO identifier defined by the GO Lab team.

When viewing data, variables from the organisation data model may be included to provide more information. See :doc:`the Organisation data dictionary <organisation>` for more information on what these variables mean.

Service Provisions
------------------

This section collects data about four different dimensions of service provision: 
 
•	Organisations providing services to impact bond projects 
•	Planned services 
•	Actual services 
•	Alterations to contracted services 
 
This is a list. One project can have multiple items of data, as one impact bond could have several service providers. One item of data is defined as: 

.. datadictionary::
   :schema: project.json
   :path: /properties/service_provisions/items


Outcome Payment Commitments
---------------------------

This section aims to collect data about three different dimensions of outcome payments: 

•	Organisations paying for outcomes 
•	Maximum potential outcome payments (in best case scenario) 
•	Total outcome payments made up to date (this can be updated during the life of the project) 

This is a list of data items. One project can have multiple items of data, as one project may have multiple outcome payers. One item of data is defined as:


.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_payment_commitments/items


Investments
-----------

This section aims to collect data about three different dimensions of investment: 
 
•	Organisations investing in impact bond projects 
•	Initial investment commitments 
•	Return to investment in best case scenario 
•	Investor repayments (this can be updated during the life of the project) 
 
This is a list. One project can have multiple items of data, as one project can receive capital from different investors. One item of data represents a particular investor and is defined as: 

.. datadictionary::
   :schema: project.json
   :path: /properties/investments/items

Intermediary services
---------------------

This section aims to collect data about two different dimensions of intermediary services: 
 
•	Organisations providing intermediary services to impact bond projects 
•	Type of intermediary services 
 
This is a list. One project can have multiple items of data, as one project may receive intermediation from several organisations. One item of data represents one intermediary organisation and is defined as: 

.. datadictionary::
   :schema: project.json
   :path: /properties/intermediary_services/items

Outcome Metrics
---------------

This is a list. One project can have multiple items of data, as one project may have several outcomes to achieve. One item of data represents one outcome metric and is defined as: 

.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_metrics/items

Outcome Pricing
---------------

This is a list. One project can have multiple items of data, as one project may have several outcomes to achieve with different prices. One item of data represents one social outcome price and is defined as: 


.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_pricings/items


Results
-------

This is a list. One project can have multiple items of data, as one project may have several outcomes with different results. One item of data represents the result for one outcome metric and is defined as: 


.. datadictionary::
   :schema: project.json
   :path: /properties/results/items

Outcome Payment Plans
---------------------

This is a list. One project can have multiple items of data, as one project can have different sets of planned payments over its lifetime. One item of data represents one plan and is defined as:

.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_payment_plans/items


Outcome Payments
----------------

This is a list. One project can have multiple items of data, as one project can receive different outcome payments for different outcome metrics, time periods and plans.
One item of data represents one outcome payment (to one outcome metric and within one plan) and is defined as:

.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_payments/items


Actual payments should have rows of data with "Type" set to "Actual" and with "Outcome Payment Plan Id" set left empty.

Outcome payments can belong to multiple plans, as plans may change over the lifetime of the project.
Plans should first be declared in the "Outcome Payment Plans" section.
Then for each plan, add multiple rows in the "Outcome Payments" section.
Each plan should include all past actual payments, and planned future payments (set "Type" column).
This may result in some actual payments being duplicated in different plans, but this is acceptable and necessary.

.. list-table:: Example Outcome Payments
   :header-rows: 1

   * - Plan
     - Period, Start to end
     - Type
     - Amount USD
   * - plan1
     - 2020-01-01 to 2020-12-31
     - Planned
     - 100,000
   * - plan1
     - 2021-01-01 to 2021-12-31
     - Planned
     - 100,000
   * - plan1
     - 2022-01-01 to 2022-12-31
     - Planned
     - 100,000
   * -
     -
     -
     -
   * -
     - 2020-01-01 to 2020-12-31
     - Actual
     - 50,000
   * -
     -
     -
     -
   * - plan2
     - 2020-01-01 to 2020-12-31
     - Actual
     - 50,000
   * - plan2
     - 2021-01-01 to 2021-12-31
     - Planned
     - 75,000
   * - plan2
     - 2022-01-01 to 2022-12-31
     - Planned
     - 75,000

In this example, the project started with a plan and "plan1" was recorded.
The actual results for the first year were then recorded.
Given the difference between the plan and the performance, a second plan was made and "plan2" was recorded.
The second plan includes the actual payment that was considered when making the plan, and thus the actual payment is duplicated.

Open Contracting
----------------

The OCDS (Open Contracting Data Standard) is a standard that enables disclosure of data and documents at all stages of the contracting process by defining a common data model and unique identifiers for documents. An explanation of how the Open Contracting Data Standard work can be found here: https://standard.open-contracting.org/latest/en/ 
 
This is a list. One project can have multiple items of data as one impact bond project can be associated with various procurement processes. One item of data is defined as: 


.. datadictionary::
   :schema: project.json
   :path: /properties/open_contracting_datas/items

360Giving
---------

The 360Giving Data Standard enables the disclosure of data on grants and grant making. An explanation of how the 360Giving Standard works can be found here: https://standard.threesixtygiving.org/en/latest/ 
 
This is a list. One project can have multiple items of data as one impact bond may have received more than one grant. One item of data is defined as: 


.. datadictionary::
   :schema: project.json
   :path: /properties/360giving_datas/items

Documents
---------

This is a list of supporting documentation for this project. Documents include press releases, interim reports, final reports, case studies, etc. One project can have multiple items of data. One item of data is defined as: 


.. datadictionary::
   :schema: project.json
   :path: /properties/documents/items


Provider Side Cost
------------------


.. datadictionary::
   :schema: project.json
   :path: /properties/provider_side_cost/items

Phase options
^^^^^^^^^^^^^

.. csv-table::
   :file: ../../schema/codelists/project_provider_side_cost_phase.csv



Classification options
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ../../schema/codelists/project_provider_side_cost_classification.csv



Type options
^^^^^^^^^^^^

.. csv-table::
   :file: ../../schema/codelists/project_provider_side_cost_type.csv


Outcome Payer Cost
------------------


.. datadictionary::
   :schema: project.json
   :path: /properties/outcome_payer_cost/items

Phase options
^^^^^^^^^^^^^

.. csv-table::
   :file: ../../schema/codelists/project_outcome_payer_cost_phase.csv



Classification options
^^^^^^^^^^^^^^^^^^^^^^

.. csv-table::
   :file: ../../schema/codelists/project_outcome_payer_cost_classification.csv



Type options
^^^^^^^^^^^^

.. csv-table::
   :file: ../../schema/codelists/project_outcome_payer_cost_type.csv




Social Investment Prototype
---------------------------


The Social Investment Prototype offers additional tabs to describe technical assistance and some financial aspects of projects in greater detail, including individual transactions. 
 
This first set of variables is in the General Overview tab: 


.. datadictionary::
   :schema: project.json
   :path: /properties/social_investment_prototype


Investment Details
^^^^^^^^^^^^^^^^^^

Expected and latest internal rates of return can be recorded on the investment details table (in the general overview tab).


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

This is a list. One project can have multiple items of data. One item of data is defined as:

.. datadictionary::
   :schema: project.json
   :path: /properties/transactions/items


Technical Assistance
^^^^^^^^^^^^^^^^^^^^

Technical Assistance (TA) is modelled as a period of engagement between a funding organisation and a recipient organisation with a defined start and end date.

This period of engagement can be broken down on the Technical Assistance Details tab into a series of component activities (as well as high-level information that covers the whole engagement where appropriate).

An activity is linked to an engagement by using the relevant `id` from the `Technical Assistance` tab. Multiple activities can be linked to a single engagement.

Data should not be provided if no technical assistance from a given category has been given, i.e., zero values are not necessary but assumed in the absence of data.

Each activity can be assigned a cost and a cost type and a time cost in days.

Where no cost is available, or where a cost is inappropriate, a row can be added with the relevant category selected and the value and cost type fields left blank. This will allow activities to be analysed as simple counts.

Activities can be further classified by the delivery approach.

On the `Technical Assistance` tab, there is a list. One project can have multiple items of data. One item of data is defined as:


.. datadictionary::
   :schema: project.json
   :path: /properties/technical_assistances/items

On the `Technical Assistance Details` tab, there is a list. One project can have multiple items of data. One item of data is defined as:

.. datadictionary::
   :schema: project.json
   :path: /properties/technical_assistance_details/items

