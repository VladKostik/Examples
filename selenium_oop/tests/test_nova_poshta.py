def test_nova_poshta_presense_of_wh_42(dashboard, browser):
    dashboard.select_top_menu_element('Відділення')
    dashboard.select_sub_menu_element('Пошук відділення за номером ')
    dashboard.find_in_city_list('Оберіть насел. пункт', 'одеса')
    dashboard.select_from_city_list('м. Одеса, Одеська обл.')
    dashboard.select_warehouse_list('Всі відділення')
    dashboard.find_warehouse_by_number('42')
    dashboard.select_warehouse('42')
    dashboard.select_office_link()
    dashboard.is_office_exist()