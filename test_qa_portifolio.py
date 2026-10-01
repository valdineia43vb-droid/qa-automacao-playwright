from playwright.sync_api import sync_playwright

def test_login_com_sucesso():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_timeout(2000)
        
        # Verifica se entrou
        assert "inventory" in page.url
        print("✅ TESTE 1 PASSOU - Login com sucesso!")
        browser.close()

def test_login_com_erro():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "usuario_errado")
        page.fill("#password", "senha_errada")
        page.click("#login-button")
        page.wait_for_timeout(2000)
        
        # Verifica se apareceu erro
        erro = page.locator("[data-test='error']").is_visible()
        assert erro == True
        print("✅ TESTE 2 PASSOU - Validou mensagem de erro!")
        browser.close()

def test_adicionar_no_carrinho():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_timeout(2000)
        page.click("#add-to-cart-sauce-labs-backpack")
        page.wait_for_timeout(1000)
        
        # Verifica se tem 1 no carrinho
        assert page.locator(".shopping_cart_badge").inner_text() == "1"
        print("✅ TESTE 3 PASSOU - Produto no carrinho!")
        browser.close()

if __name__ == "__main__":
    test_login_com_sucesso()
    test_login_com_erro()
    test_adicionar_no_carrinho()
    print("\n🎉 TODOS OS 3 TESTES PASSARAM! PORTFÓLIO PRONTO!")