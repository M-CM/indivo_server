from indivo.models import Immunization
from indivo.lib.iso8601 import parse_utc_date as date

immunization_fact = Immunization(
    date=date("2009-05-16T12:00:00Z"),
    administration_status_title="Not Administered",
    administration_status_system="http://smartplatforms.org/terms/codes/ImmunizationAdministrationStatus#",
    administration_status_identifier="notAdministered", 
    product_class_title="TYPHOID",
    product_class_system="http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=vg#",
    product_class_identifier="TYPHOID",
    product_name_title="typhoid, oral",
    product_name_system="http://www2a.cdc.gov/nip/IIS/IISStandards/vaccines.asp?rpt=cvx#",
    product_name_identifier="25",
    refusal_reason_title="Allergy to vaccine/vaccine components, or allergy to eggs",
    refusal_reason_system="http://smartplatforms.org/terms/codes/ImmunizationRefusalReason#",
    refusal_reason_identifier="allergy",
  )

