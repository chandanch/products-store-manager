import pytest
from app.schemas.category_schema import CategoryCreate
from pydantic import ValidationError

from factories.models_factory import generate_random_category_as_dict


def mock_output(return_value):
    return lambda *args, **kwargs: return_value


def test_unit_schema_category_validation():
    valid_data = {
        "name": "test category",
        "slug": "test-slug",
    }
    category = CategoryCreate(**valid_data)
    assert category.name == "test category"
    assert category.is_active is False
    assert category.level == 100
    assert category.parent_id is None

    invalid_data = {
        "name": "test category",
    }
    with pytest.raises(ValidationError):
        CategoryCreate(**invalid_data)


def test_unit_create_category_success(client, monkeypatch):

    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output)
    monkeypatch.setattr("sqlalchemy.orm.Session.commit", mock_output)
    monkeypatch.setattr("sqlalchemy.orm.Session.refresh", mock_output)

    mock_category_data = generate_random_category_as_dict()
    clone_mock_category_data = mock_category_data.copy()

    clone_mock_category_data.pop("id")
    response = client.post("api/category", clone_mock_category_data)
    assert response.status_code == 201
    assert response.json() == mock_category_data


def test_unit_create_category_error(client, monkeypatch):

    monkeypatch.setattr("sqlalchemy.orm.Query.first", mock_output)
    monkeypatch.setattr("sqlalchemy.orm.Session.commit", mock_output)
    monkeypatch.setattr("sqlalchemy.orm.Session.refresh", mock_output)

    mock_category_data = generate_random_category_as_dict()
    clone_mock_category_data = mock_category_data.copy()

    clone_mock_category_data.pop("id")
    response = client.post("api/category", clone_mock_category_data)
    assert response.status_code == 201
    assert response.json() == mock_category_data
