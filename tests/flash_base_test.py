import unittest
from flash_base import Flash, solve_flash

class TestFlashModule(unittest.TestCase):

    def test_psi_class_set_values(self):
        psi_instance = Flash.psi_class()
        z_test = [0.1, 0.2, 0.3, 0.4]
        k_test = [1, 2, 3, 4]
        psi_instance.set_values(z_test, k_test)
        self.assertEqual(psi_instance.z.tolist(), z_test)
        self.assertEqual(psi_instance.k.tolist(), k_test)

    def test_psi_class_f_psi(self):
        psi_instance = Flash.psi_class()
        z_test = [0.1, 0.2, 0.3, 0.4]
        k_test = [1, 2, 3, 4]
        psi_instance.set_values(z_test, k_test)
        result = psi_instance.f_psi(0.5)
        expected_result = 0.834177777777778
        self.assertAlmostEqual(result, expected_result, places=5)

    def test_flash_initialization(self):
        flash_instance = Flash()
        self.assertIsInstance(flash_instance, Flash)

    def test_flash_get_variables(self):
        flash_instance = Flash()
        variables = flash_instance.get_variables()
        self.assertEqual(len(variables), 1)
        self.assertEqual(variables[0].name, "psi")

    def test_flash_get_initial_point(self):
        flash_instance = Flash()
        initial_point = flash_instance.get_initial_point()
        self.assertEqual(initial_point, [0.5])

    def test_solve_flash(self):
        z_test = [0.1, 0.2, 0.3, 0.4]
        k_test = [4.2, 1.75, 0.74, 0.34]
        result = solve_flash(z_test, k_test)
        expected_status = 0.12187670230987685
        self.assertEqual(result, expected_status)

if __name__ == '__main__':
    unittest.main()