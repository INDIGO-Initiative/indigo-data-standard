
Formatting data
---------------

Dates
^^^^^

The specification allows for imprecise dates depending on how much information is known (e.g., 2020 or 2020-06). Dates must use the YYYY-MM-DD format.

Currencies and currency conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A field describing a monetary value in the INDIGO specification should have an accompanying currency field. Monetary values must be described as numbers only with no currency symbols, commas or textual descriptions of large numbers.

Currency codes must come from the `ISO 4217 <https://en.wikipedia.org/wiki/ISO_4217>`_ code list.

.. admonition:: Example

   A social impact bond makes an investment of USD250000. This data should be input as:

    +------------------------------------------+--------------+
    | Field                                    | Entity value |
    +==========================================+==============+
    | investment_commitment/currency/value     | USD          |
    +-------------+----------------------------+--------------+
    | investment_commitment/amount/exact/value | 250000       |
    +-------------+----------------------------+--------------+

    Inputting the value as "250,000", "$250000" or "250k" would be wrong.

Monetary values should be input in the currency of the original transaction. There may be a converted USD value of any transaction, calculated by the INDIGO project, using the methodology described in the data dictionary. Data providers should not convert transactions to USD when supplying data.

