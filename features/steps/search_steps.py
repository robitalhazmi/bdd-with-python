from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to the Twitter Search page')
def step_impl(context):
    context.search_page.navigate("https://twitter.com/search-home")
    assert_equal(context.search_page.get_page_title(), "Twitter Search")

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.search_page.search(search_term)

@step('I am taken to Twitter Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Twitter Search")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))