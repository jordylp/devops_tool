# test_audit.py
from check_ip import inventario


def test_ip_en_inventario():

    assert "192.168.1.10" in inventario


def test_ip_no_registrada():
    # Verificamos que una IP falsa no este en el inventario
    assert "10.0.0.1" not in inventario
