Versions & Changelog
====================

Versions
--------

This data standard is versioned.

The scheme used is 3 numbers, `MAJOR.MINOR.PATCH` and follows `SemVer <https://semver.org/spec/v2.0.0.html>`_. In brief:

Increments to Patch numbers:

* should not change the intention of how the data standard actually works.
* may include modified and additional content to make clear things that were previously unclear.
* may include changes to correct previous mistakes.

Increments to Minor numbers:

* may include changes to the workings of the data standard, limited to additions of new models or fields in a backwards compatible manner.

Increments to Major numbers:

* may include changes to the workings of the data standard in a manner that is not backwards compatible. This will probably be modifications of existing models or fields.

Changelog
---------

4.0.0 - 2023-06-27
~~~~~~~~~~~~~~~~~~

Unreleased
~~~~~~~~~~

Project - Removed Scenario Sheet as this is not used.

Project - added new "Outcome Payment Plans" and added reference from "Outcome Payments" to this.

Project - changed descriptions for fields that reference other ID's to make it clear that ID's here should reference the original ID elsewhere and not be created here. This was changed in:

  *  "Outcome Pricings" section, "Outcome Metric Id" field
  *  "Transactions" section, "Investment Id" and "Outcome Metric Id" fields
  *  "Technical Assistance Details" section, "Technical Assistance Id" field
  *  "Results" section, "Outcome Metric Id" field
  *  "Outcome Payments" section, "Outcome Metric Id" field

Project - remove "Grant ID" from "Transactions".

3.1.1 - 2023-02-03
~~~~~~~~~~~~~~~~~~

Corrected spelling of "modelling" option in project, Intermediary services, Organisation Role Category.

3.1.0 - 2023-01-24
~~~~~~~~~~~~~~~~~~

Add Provider Side Cost and Outcome Payer Cost to project.

Add duration of service provision (anticipated and actual) to project.

Add job title, Twitter, LinkedIn and profile to organisation contact section. 

Add status fields to organisation contact section. 

3.0.1 - 2022-10-21
~~~~~~~~~~~~~~~~~~

Add sandboxes field to Results in Project model. (As this is is a internal field, releasing as a patch release.)

3.0.0 - 2022-05-06
~~~~~~~~~~~~~~~~~~

New Pipeline model

Changes to Project descriptions after `a review and consultation process <https://golab.bsg.ox.ac.uk/community/news/have-your-say-with-the-impact-bond-dataset-data-definitions/>`_. This does not change the meaning of any variables, only adds examples, clarifies some definitions and includes descriptions for the 'Sources' and "Notes' variables.

Specify options for sources type (Project, Organisation and Pipeline).

Project "Stage of Development" - remove two options. Data for these lives in Pipeline now.

Add non standard "references-model" and "references-models-seperator" keys to JSON Schema for links between models.

Add non standard "references-data-key", "references-data-list" and "references-datas-seperator" keys to JSON Schema for links between part of the same model. Done for "sources" only - project.json and pipeline.json is missing other references.

2.3.0 - 2022-03-18
~~~~~~~~~~~~~~~~~~

Documents moved to new home at https://indigo-data-standard.readthedocs.io

Versioning of these documents restarted properly.

Between this release and the last one, many additions were made to the data models and definitions clarified.

2.02 - 2020-11-11
~~~~~~~~~~~~~~~~~

Updated variable definitions, footnotes and hyperlinks.

2.01 - 2020-09-03
~~~~~~~~~~~~~~~~~

Updated based on changes to the prototype tabs. Add priority levels.

2.0 - 2020-08-27
~~~~~~~~~~~~~~~~

Moved from version 1 drafts to Version 2.

