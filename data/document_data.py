import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])


document_name = random_string("test_", 6)
document_name_be = random_string("test_", 6)
document_name_new = random_string("test_", 6)




# def document_name(res):
#     res.backend.get_last_document_name()[0:11] + 1


