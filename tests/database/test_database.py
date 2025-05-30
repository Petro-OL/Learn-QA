import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    prod_qnt = db.select_product_qnt_by_id(1)

    assert prod_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    product_qnt = db.select_product_qnt_by_id(4)

    assert product_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

# --------------------------

@pytest.mark.database
# write to base: Boolean-value to primary key field with type int
# an empty string is created with key = 1 (True) or key = 0 (False)
def test_work_db_with_autoconvert_id_type():
    db = Database()
    rec_saved = db.select_product_by_id(1)
    db.insert_bad_type_of_data('id', True)
    # ------------------------------------
    rec_bad = db.select_product_by_id(1)
    assert rec_bad[0][0] == 1
    assert rec_bad[0][1] == None
    assert rec_bad[0][2] == None
    assert rec_bad[0][3] == None
    # restore item
    db.insert_product(rec_saved[0][0], rec_saved[0][1], rec_saved[0][2], rec_saved[0][3])

@pytest.mark.database
# write to base: float-value to primary key type with type int
# error check (code = 1)
def test_work_db_with_mismatch_id_type_float():
    db = Database()
    code = db.insert_bad_type_of_data('id', 1.1)
    assert code == 1

@pytest.mark.database
# write to base: string value:
# error check (code = 1)
def test_work_db_with_mismatch_id_type_str():
    db = Database()
    code = db.insert_bad_type_of_data('id', 'text')
    assert code == 1

@pytest.mark.database
# write to base: spesial-string value:
# checking auto-conversion '1' to 1
def test_work_db_with_autoconvert_id_type_from_str():
    db = Database()
    rec_saved = db.select_product_by_id(1)
    db.insert_bad_type_of_data('id', "1")
    # ------------------------------------
    rec_bad = db.select_product_by_id(1)
    assert rec_bad[0][0] == 1
    assert rec_bad[0][1] == None
    assert rec_bad[0][2] == None
    assert rec_bad[0][3] == None
    # restore
    db.insert_product(rec_saved[0][0], rec_saved[0][1], rec_saved[0][2], rec_saved[0][3])

@pytest.mark.database
# write to base: string-value to field with type int
# MISSING error ( code = 0)
# -----------------
def test_work_db_with_mismatch_column_type_str_to_int():
    db = Database()
    code = db.insert_bad_type_of_data('quantity', 'text')
    assert code > 0
    # restore item
    query = "SELECT max(id) FROM products"
    db.cursor.execute(query)
    rec_num = db.cursor.fetchall()
    db.delete_product_by_id(rec_num[0][0])
