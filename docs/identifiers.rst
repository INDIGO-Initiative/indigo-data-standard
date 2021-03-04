
Identifiers
===========

The INDIGO specification uses three kinds of identifier to link data internally and offers space to enhance the data with the identifiers of related disclosures.

INDIGO identifiers
------------------

INDIGO identifiers are assigned to projects, organisations and funds to ensure uniqueness for these important entities across all published datasets. An INDIGO identifier must not be changed once assigned.

The entity an INDIGO identifier refers to can be inferred from the prefix, as follows.

+-------------+------------------------------------------+
| Prefix      | Entity type                              |
+=============+==========================================+
| INDIGO-POJ  | A project.                               |
+-------------+------------------------------------------+
| INDIGO-ORG  | An organisation.                         |
+-------------+------------------------------------------+
| INDIGO-FUND | An outcome payment or investment fund.   |
+-------------+------------------------------------------+

Real-world identifiers
----------------------

Most organisations will have an official registration number suitable for use as a unique identifier. The INDIGO specification requires identifiers to use the format and prefixes specified by org-id, an open register of organization lists.

An organisation identifier consists of:

1. A list code: a prefix that describes the list the identifier is taken from.
2. An identifier taken from that list.

.. admonition:: Example

   Open Data Services Co-operative Limited is a private company limited by shares, registered in the UK. From the `org-id page <http://org-id.guide/list/GB-COH>`_ the prefix for Companies House is GB-COH. From the `linked register <https://beta.companieshouse.gov.uk/company/09506232>`_ the company number is 09506232. The full identifier in org-id format is then GB-COH-09506232.

Internal identifiers
--------------------

Internal identifiers are unique within a project and used to join components of a project together, for example a result can be linked to a specific outcome metric. Once an internal identifier is set it must not be changed.

Related contract identifiers
----------------------------

To link one or more contracting processes published to the Open Contracting Data Standard (OCDS), use the `ocid`, or contract processing identifier, field. The value in the INDIGO dataset must match that in the relevant published OCDS field. The use of this field is described in the `OCDS documentation <https://standard.open-contracting.org/latest/en/schema/identifiers/#contracting-process-identifier-ocid>`_. The data dictionary describes in what circumstances a contracting process is considered to be linked to a project.

Related grant identifiers
-------------------------

To link one or more grants published to the 360Giving Data Standard, use the `grant_id`, or grant ID, field. The value  of the `grant_id` field in the INDIGO dataset must match that in the relevant 360Giving field. The use of this field in is described in the `360Giving documentation <http://standard.threesixtygiving.org/en/latest/identifiers/#grant-identifier>`_. The data dictionary describes in what circumstances a grant is considered to be linked to a project.
