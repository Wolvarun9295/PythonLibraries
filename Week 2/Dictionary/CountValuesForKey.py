employee = [{'id': 1, 'success': True, 'name': 'Lary'},
            {'id': 2, 'success': False, 'name': 'Rabi'},
            {'id': 3, 'success': True, 'name': 'Alex'}]
print(f"The count of success as True: {sum(dictionary['success'] for dictionary in employee)}")
