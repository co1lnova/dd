from model.document import Document
from data.document_data import document_name


def test_create_implementation(res):
    res.session.login(username="sb_doc_analyst", password="Default!1")
    res.navigation.open_defdocs_service()
    res.document.create(Document(name=document_name, number="123", date="12122020",
                                 file="/Users/a.marchenko/PycharmProjects/defzone1/env/upload_file.txt"))
    res.navigation.reopen_defdocs_service()
    assert document_name == res.assert_data.get_first_document_name()
    res.session.logout()
