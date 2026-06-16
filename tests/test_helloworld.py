from helloworld import main


def test_main_prints_hello_world(capsys):
    main()

    assert capsys.readouterr().out == "Hello World\n"
