import pytest
from fixture.resources import Resources


@pytest.fixture
def res(request):
    fixture = Resources()
    request.addfinalizer(fixture.destroy)
    return fixture
