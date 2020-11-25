import click.testing
import pytest
import requests

from modern_python import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()



def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
   

# mock being inspected to see if they were called
def test_main_invokes_requests_get(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert mock_requests_get.called

# deterministic return value
def test_main_prints_title(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert "Lorem Ipsum" in result.output

# inspect the arguments the were called with
def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    result = runner.invoke(console.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]

def test_main_fails_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output
   
@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("modern_python.wikipedia.random_page")

def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")

@pytest.mark.e2e
def test_main_succeeds_in_produciton_env(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0