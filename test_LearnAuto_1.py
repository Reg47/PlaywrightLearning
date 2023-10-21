
from playwright.sync_api import Playwright, sync_playwright, expect

def testrun(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="How to run the example test").click()
    page.get_by_role("img", name="tests running in command line").click()
    page.get_by_role("heading", name="Running the Example Test in UI ModeDirect link to Running the Example Test in UI Mode").click()
    page.get_by_role("heading", name="Running the Example Test in UI ModeDirect link to Running the Example Test in UI Mode").click()
    page.get_by_role("heading", name="Updating PlaywrightDirect link to Updating Playwright").click()
    page.get_by_role("heading", name="System requirementsDirect link to System requirements").click()
    page.get_by_text("Node.js 16+").click()
    page.get_by_text("Windows 10+, Windows Server 2016+ or Windows Subsystem for Linux (WSL).").click()
    page.get_by_text("MacOS 12 Monterey or MacOS 13 Ventura.").click()
    page.get_by_text("Debian 11, Debian 12, Ubuntu 20.04 or Ubuntu 22.04.").click()
    page.get_by_role("link", name="Next Writing tests »").click()
    page.get_by_role("heading", name="Writing tests").click()

    # ---------------------
    context.close()
    browser.close()

    print("complete")
