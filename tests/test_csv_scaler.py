"""Test csv_scaler."""

from unittest.mock import mock_open, patch

from click.testing import CliRunner

from csv_scaler import main


def test_main():
    """Test main."""
    with patch("builtins.open", new_callable=mock_open, read_data="dummy_pk\n42"):
        runner = CliRunner()
        result = runner.invoke(main, ["-f", "dummy_path", "-pk", "dummy_pk"])
        assert result.exit_code == 0


@patch("csv_scaler.main")
def test_csv_scaler(mock_main):  # pylint: disable=unused-argument
    """Test csv_scaler."""
    from csv_scaler import __main__  # pylint: disable=import-outside-toplevel, unused-import
