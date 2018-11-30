from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By
# Top Search Scenario
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
# Search User Scenario

@step('Top search results for "{search_term}" are shown')
def step_impl(context, search_term):
    context.search_page.navigate("https://twitter.com/search?src=typd&q=Robit%20Alhazmi")
    assert_equal(context.search_page.get_page_title(), "Robit Alhazmi - Twitter Search")

@step('I click on the "{search_term}" link')
def step_impl(context, search_term):
    context.search_page.click_element(By.LINK_TEXT, search_term)

@step('User related to "{search_result}" are shown on the results page')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))