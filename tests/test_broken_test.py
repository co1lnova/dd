

def test_invalid_credential(res):
    res.session.login(username="invalid", password="invalid")
    res.navigation.open_defdocs_service()

