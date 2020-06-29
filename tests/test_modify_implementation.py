from model.document import Document
from data.document_data import document_name_new


def test_modify_first_implementation_name(res):
    res.session.login(username="sb_doc_analyst", password="Default!1")
    res.navigation.open_defdocs_service()
    res.navigation.open_first_document()
    res.navigation.open_parameters()
    res.document.modify_first_implementation_name(name=document_name_new)
    res.navigation.reopen_defdocs_service()
    assert document_name_new == res.assert_data.get_first_document_name()
    res.session.logout()

