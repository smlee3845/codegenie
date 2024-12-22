def test_plugin_loader():
    os.makedirs("tests/test_plugins", exist_ok=True)  
    plugins = load_plugins("tests/test_plugins")
    assert len(plugins) == 0  
