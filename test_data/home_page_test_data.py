class HomePageTestData:
    VALID_FORM_TEST_DATA = [

        {
            'name': 'Akhilesh Patel',
            'email': 'akhileshpatel597@gmail.com',
            'password': 'Akhil@123'
        }
    ]

    INVALID_FORM_TEST_DATA = [
        {
            'name': '',
            'email': 'akhileshpatel597@gmail.com',
            'password': 'Akhil@123'
        },
        {
            'name': 'Akhilesh Patel',
            'email': 'invalid_email',
            'password': 'Akhil@123'
        },
        {
            'name': 'Akhilesh Patel',
            'email': 'akhileshpatel597@gmail.com',
            'password': 'wrong_password'
        }
    ]
