"""class for testing the register_project method"""
import unittest
import json
import os
from src.main.python.uc3m_consulting import EnterpriseManager, EnterpriseManagementException

class TestRegisterProject(unittest.TestCase):
    def setUp(self):
        """Clean up the JSON file before each test."""
        self.filename = "corporate_operations.json"
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_TC5_invalid_cif_not_string(self):
        """TC5: CIF must be a string."""
        enterprise_manager = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project(123456789, "PRO02", "first test", "LOGISTICS", "02/01/2026", 60000.01)
        self.assertEqual(str(cm.exception), "CIF must be a string")

    def test_TC6_invalid_cif_algorithm(self):
        """TC6: CIF fails validation algorithm pattern."""
        enterprise_manager = EnterpriseManager()
        with self.assertRaises(EnterpriseManagementException) as cm:
            enterprise_manager.register_project("AA123456B", "PRO03", "first test", "LOGISTICS", "03/01/2026", 60000.02)
        self.assertEqual(str(cm.exception), "CIF does not pass validation algorithm")

if __name__ == '__main__':
    unittest.main()