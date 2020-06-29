

def test_start_implementation(res):
    res.session.login(username="sb_doc_analyst", password="Default!1")
    res.backend.get_token()
    res.backend.create_document()
    res.navigation.open_defdocs_service()
    res.navigation.open_created_document()
    res.navigation.open_parameters()
    res.document.add_subsidiary()
    assert res.assert_data.get_dzo1() == "sb_docs_DZO1"
    res.navigation.implement_document()
    res.navigation.reopen_defdocs_service()
    res.navigation.open_first_document()
    assert res.assert_data.get_implementation_status() == "На ознакомлении"
    res.session.logout()
