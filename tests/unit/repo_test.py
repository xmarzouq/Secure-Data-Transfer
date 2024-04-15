import pytest
from unittest.mock import patch, MagicMock
import uuid
from repo import insert_file, delete_file, read_all_files, encrypt_key, get_mac_address


@pytest.fixture
def mock_supabase():
    with patch("repo.supabase") as mock:
        yield mock


@pytest.fixture
def mock_uuid():
    with patch("uuid.uuid4") as mock:
        mock.return_value = uuid.UUID(int=0)
        yield mock


@pytest.fixture
def mock_rsa_encrypt():
    with patch("repo.layered_rsa_encrypt") as mock:
        mock.return_value = "encrypted_key"
        yield mock


def test_get_mac_address():
    mac = get_mac_address()
    assert len(mac.split(":")) == 6  # MAC address should have 6 octets


def test_insert_file(mock_supabase, mock_rsa_encrypt):
    insert_file(
        "original_name.txt.enc",
        "original_name.txt",
        "aes",
        "/test/text/",
        "aes_key",
        1024,
    )
    mock_supabase.table.assert_called_once_with("files")
    mock_supabase.table().insert.assert_called_once()
    args, _ = mock_supabase.table().insert.call_args

    data = args[0]
    assert data["file_name"] == "original_name.txt.enc"
    assert data["key"] == "encrypted_key"


def test_encrypt_key(mock_rsa_encrypt):
    key = encrypt_key("aes_key")
    assert key == "encrypted_key"


def test_read_all_files(mock_supabase):
    mock_supabase.table().select().execute.return_value = MagicMock(
        data=[{"file_name": "file1.txt"}]
    )
    df = read_all_files()
    assert not df.empty
    assert "file_name" in df.columns
    assert df.at[0, "file_name"] == "file1.txt"


def test_delete_file(mock_supabase):
    response = delete_file("file_to_delete.txt", 1024)
    mock_supabase.table().delete().match.assert_called_once_with(
        {"file_name": "file_to_delete.txt", "file_size": 1024}
    )
    assert response["data"] is not None