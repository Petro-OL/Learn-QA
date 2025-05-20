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
    # print(type(users))
    # print(type(users[0]))

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
    # print(product_qnt[0][0])

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

# --------------------------

@pytest.mark.database
# запис в базу при типі основного ключа int значення = Boolean:
# створюється порожній рядок з ключем = 1 (True) чи ключем = 0 (False)
def test_work_db_with_autoconvert_id_type():
    db = Database()
    rec_saved = db.select_product_by_id(1)
    #print(rec_saved)
    db.insert_bad_type_of_data('id', True)
    # ------------------------------------
    rec_bad = db.select_product_by_id(1)
    #print(rec_bad)
    assert rec_bad[0][0] == 1
    assert rec_bad[0][1] == None
    assert rec_bad[0][2] == None
    assert rec_bad[0][3] == None
    # restore
    db.insert_product(rec_saved[0][0], rec_saved[0][1], rec_saved[0][2], rec_saved[0][3])

@pytest.mark.database
# запис в базу при типі основного ключа int значення = Float:
# перевірка на помилку (код = 1)
def test_work_db_with_mismatch_id_type_float():
    db = Database()
    code = db.insert_bad_type_of_data('id', 1.1)
    #print(code)
    assert code == 1

@pytest.mark.database
# запис в базу при типі основного ключа int значення = String:
# перевірка на помилку (код = 1)
def test_work_db_with_mismatch_id_type_str():
    db = Database()
    code = db.insert_bad_type_of_data('id', 'text')
    #print(code)
    assert code == 1

@pytest.mark.database
# запис в базу при типі основного ключа int значення = спец. String:
# перевірка автоперетворення '1' в 1
def test_work_db_with_autoconvert_id_type_from_str():
    db = Database()
    rec_saved = db.select_product_by_id(1)
    #print(rec_saved)
    db.insert_bad_type_of_data('id', "1")
    # ------------------------------------
    rec_bad = db.select_product_by_id(1)
    #print(rec_bad)
    assert rec_bad[0][0] == 1
    assert rec_bad[0][1] == None
    assert rec_bad[0][2] == None
    assert rec_bad[0][3] == None
    # restore
    db.insert_product(rec_saved[0][0], rec_saved[0][1], rec_saved[0][2], rec_saved[0][3])

@pytest.mark.database
# запис в базу при типі даних Поля int значення = String
# ВІДСУТНЯ помилка, перевірка на успіх запису (код = 0)
# -----------------
def test_work_db_with_mismatch_column_type_str_to_int():
    db = Database()
    code = db.insert_bad_type_of_data('quantity', 'text')
    #print(code)
    assert code == 0
    # restore
    query = "SELECT max(id) FROM products"
    db.cursor.execute(query)
    rec_num = db.cursor.fetchall()
    db.delete_product_by_id(rec_num[0][0])
