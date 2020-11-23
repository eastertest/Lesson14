from pytest_bdd import scenario, given, when, then
import pytest

from fullRetirementAge import *


@scenario('retirementAge.feature', 'Find retirement age')
def testRetirementAge():
    pass


@given("fullRetirementAge has been started in the terminal")
def run_program(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == 'test\n'


@when('my year of birth is entered')
def enter_birth_year(monkeypatch, capsys):

    monkeypatch.setattr('builtins.input', lambda _: '1993')
    monkeypatch.setattr('builtins.input', lambda _: '6')
    out, err = capsys.readouterr()
    assert out == 'test\n'


# @when('my birth month is entered')
#def enter_birth_month(monkeypatch,capsys):

#    out, err = capsys.readouterr()


@then('my retirement age is displayed')
def age_displayed():
    #out, err = capsys.readouterr()
    out = 4
    assert out == 'test\n'
