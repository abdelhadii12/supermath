import math
import pytest
from supermath1.trigonometrie import calcul_sinus, calcul_cosinus, calcul_tangente

def test_calcul_sinus():
    assert calcul_sinus(0) == pytest.approx(0, rel=1e-9)
    assert calcul_sinus(30) == pytest.approx(0.5, rel=1e-9)
    assert calcul_sinus(45) == pytest.approx(math.sqrt(2)/2, rel=1e-9)
    assert calcul_sinus(90) == pytest.approx(1, rel=1e-9)
    assert calcul_sinus(180) == pytest.approx(0, rel=1e-9)

def test_calcul_cosinus():
    assert calcul_cosinus(0) == pytest.approx(1, rel=1e-9)
    assert calcul_cosinus(30) == pytest.approx(math.sqrt(3)/2, rel=1e-9)
    assert calcul_cosinus(45) == pytest.approx(math.sqrt(2)/2, rel=1e-9)
    assert calcul_cosinus(90) == pytest.approx(0, rel=1e-9)
    assert calcul_cosinus(180) == pytest.approx(-1, rel=1e-9)

def test_calcul_tangente():
    assert calcul_tangente(0) == pytest.approx(0, rel=1e-9)
    assert calcul_tangente(30) == pytest.approx(1/math.sqrt(3), rel=1e-9)
    assert calcul_tangente(45) == pytest.approx(1, rel=1e-9)
    assert calcul_tangente(90) == pytest.approx(float('inf'), rel=1e-9)  # Tangente de 90 degrés est infinie
    assert calcul_tangente(180) == pytest.approx(0, rel=1e-9)
