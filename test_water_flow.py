from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import water_flow

def test_water_column_height():
    assert water_column_height(0, 0) == 0
    assert water_column_height(0, 10) == approx(7.5)
    assert water_column_height(25, 0) == 25
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0, 0.018, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0, 1.75) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 0) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1000, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.28687, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)


def test_pressure_loss_from_fittings():
    # Test cases
    assert water_flow.pressure_loss_from_fittings(0, 3) == 0.001
    assert water_flow.pressure_loss_from_fittings(1.65, 0) == 0.001
    assert water_flow.pressure_loss_from_fittings(1.65, 2) == -0.109
    assert water_flow.pressure_loss_from_fittings(1.75, 2) == -0.122
    assert water_flow.pressure_loss_from_fittings(1.75, 5) == -0.306

def test_reynolds_number():
    # Test cases
    assert water_flow.reynolds_number(0.048692, 0) == 0
    assert water_flow.reynolds_number(0.048692, 1.65) == 80069
    assert water_flow.reynolds_number(0.048692, 1.75) == 84922
    assert water_flow.reynolds_number(0.28687, 1.65) == 471729
    assert water_flow.reynolds_number(0.28687, 1.75) == 500318

def test_pressure_loss_from_pipe_reduction():
    # Test cases
    assert water_flow.pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == 0.001
    assert water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == -163.744
    assert water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == -184.182

# Additional test function for psi to kPa conversion (Exceeding Requirements)
def test_psi_to_kpa_conversion():
    assert water_flow.psi_to_kpa(1) == 6.89476
    assert water_flow.psi_to_kpa(10) == 68.9476
    assert water_flow.psi_to_kpa(20) == 137.8952

# Run all the test functions
def run_tests():
    test_pressure_loss_from_fittings()
    test_reynolds_number()
    test_pressure_loss_from_pipe_reduction()
    test_psi_to_kpa_conversion()

# if __name__ == "__main__":
#     run_tests()


# Call the main function that is part of pytest to execute the test functions in this file.
if __name__ == '__main__':
    
    pytest.main(["-v", "--tb=line", "-rN", __file__])
