import pytest

from string_utils import StringUtils

string_util = StringUtils()

@pytest.mark.parametrize('string, result', [
    ("olesya", "Olesya"), #позитив
    ("olesya Efremova", "Olesya efremova"),#позитив
    ("olesya123", "Olesya123"),#позитив
    ("москва-", "Москва-"),#позитив 
    ("", ""),#негатив
    ("Olesya", "Olesya"),#негатив
    ("MOS", "Mos"), #негатив
    ("123", "123"), #негатив
    ("  mos", "  mos")]) #негатив

def test_capitalize(string, result):
    string_util = StringUtils()
    res = string_util.capitilize(string)
    assert res == result

@pytest.mark.parametrize('string, result', [
    (" mos", "mos"),#Позитив
    (" MOS", "MOS"),#Позитив
    ("  123  ", "123  "),#Позитив
    (" ---", "---"),#Позитив
    ("   A1", "A1"),#Позитив
    ("", ""),#Негатив
    ("mos ", "mos "),#Негатив
    ("123", "123"),#Негатив
    ("F f ", "F f ")])#Негатив

def test_trim(string, result):
    string_util = StringUtils()
    res = string_util.trim(string)
    assert res == result
    
@pytest.mark.parametrize('string, divider, result', [
    ("one,two,three", ",", ["one", "two", "three"]),#Позитив
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),#Позитив
    ("One;TWO;three; for", ";", ["One", "TWO", "three", " for"]),#Позитив
    ("!^-^&^*", "^", ["!", "-", "&", "*"]),#Позитив
    #Негативные проверки:
    ("", None, []),#Негатив
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"])])#Негатив   

def test_to_list(string, divider, result):
        
    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)
    
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("olesya", "s", True),#Позитив
    (" Error", "E", True),#Позитив
    ("oLesya ", "y", True),#Позитив
    ("!-8", "-", True),#Позитив
    ("1 2 3", "1 2", True),#Позитив
    ("", "", True),#Позитив
    (" ", " ", True),#Позитив
    ("olesya", "L", False),#Негатив
    ("error", "E", False),#Негатив
    ("Olesya", "o", False),#Негатив  
    ("mos", "!", False),#Негатив  
    ("", "x", False),#Негатив  
    ("One", "er", False)])#Негатив

def test_contains(string, symbol, result):
    string_util = StringUtils()
    res = string_util.contains(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("Olesya", "y", "Olesa"),#Позитив
    ("Sila", "ila", "S"),#Позитив
    ("1 2345", " ", "12345"),#Позитив
    ("Olesya-Efremova", "-", "OlesyaEfremova"),#Позитив
    ("olesya", "1", "olesya"),#Негатив
    ("", "", ""),#Негатив
    ("", "!", ""),#Негатив
    ("olesya", "", "olesya")])#Негатив

def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("Olesya", "O", True),#Позитив
    ("olesya", "o", True),#Позитив
    (" Olesya ", " ", True),#Позитив
    ("Olesya Efremova", "O", True),#Позитив
    ("123", "1", True),#Позитив
    ("Olesya", "o", False),#Негатив
    ("olesya", "O", False),#Негатив
    ("", "1", False),#Негатив
    ("-2", "2", False),#Негатив
    ("123", "3", False),#Негатив
    ("123", "2", False)])#Негатив

def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, symbol, result', [
    ("olesya", "a", True),#Позитив
    ("olesyA", "A", True),#Позитив
    ("", "", True),#Позитив
    ("123 ", " ", True),#Позитив
    ("123", "3", True),#Позитив
    ("Olesya Efrem", "m", True),#Позитив
    ("one", "O", False),#Негатив
    ("123", "1", False),#Негатив
    ("Olesya", "A", False),#Негатив
    ("", "0", False)])#Негатив

def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

@pytest.mark.parametrize('string, result', [
    ("", True),#Позитив
    (" ", True),#Позитив
    ("           ", True),#Позитив
    ("olesya", False),#Негатив
    (" k", False),#Негатив
    ("      123     ", False),#Негатив
    ("-!", False),#Негатив
    ("0", False)])#Негатив

def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [
    (["a", "b", "c"], ",", "a,b,c"),#Позитив
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),#Позитив
    (["a", "b", "c"], "", "abc"),#Позитив
    (["Olesya", "Efremova"], "-", "Olesya-Efremova"),#Позитив
    (["Olesya", "Efremova"], " ", "Olesya Efremova"),#Позитив
    ([], None, ""),#Негатив
    ([1], "-", "1"),#Негатив
    ([], ",", "")])#Негатив

def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    assert res == result

