"""Module """
import re
from .enterprise_management_exception import EnterpriseManagementException

class EnterpriseManager:
    """Class for providing the methods for managing the orders"""
    def __init__(self):
        pass

    def register_project(self, company_cif: str, project_achronym: str, project_description: str, department: str, date: str, budget: float):
        """Method for registering the project"""
        # TC5: Validate Type
        if not isinstance(company_cif, str):
            raise EnterpriseManagementException("CIF must be a string")

        # TC6: Validation Algorithm (Basic pattern check for Letter + 8 chars)
        cif_pattern = r'^[A-Z][0-9]{7}[A-Z0-9]$'
        if not re.match(cif_pattern, company_cif):
            raise EnterpriseManagementException("CIF does not pass validation algorithm")

        pass

    @staticmethod
    def validate_cif(cif: str):
        """RETURNs TRUE IF THE IBAN RECEIVED IS VALID SPANISH IBAN,
        OR FALSE IN OTHER CASE"""
        return True
