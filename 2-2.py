from random import randint


def build_web(line, name):
    f = open(name, 'w')
    msg = """
    <html>
        <head>
            <meta http-equiv='Content-Type' content='text/html; charset=utf-8' />
            <title>CGI script output </title>
        </head>

        <body>
            <H1>{}</H1>
        </body>
    </html>

    """.format(line)
    f.write(msg)
    f.close()


def main():
    content = ['Beautiful is better than ugly.',
               'Explicit is better than implicit.',
               'Simple is better than complex.',
               'Complex is better than complicated.',
               'Flat is better than nested.',
               'Sparse is better than dense.',
               'Readability counts.',
               "Special cases aren't special enough to break the rules.",
               "Although practicality beats purity.",
               "Errors should never pass silently.",
               "Unless explicitly silenced.",
               "In the face of ambiguity, refuse the temptation to guess.",
               "There should be one-- and preferably only one --obvious way to do it.",
               "Although that way may not be obvious at first unless you're Dutch.",
               "Now is better than never.",
               "Although never is often better than *right* now.",
               "If the implementation is hard to explain, it's a bad idea.",
               "If the implementation is easy to explain, it may be a good idea.",
               "Namespaces are one honking great idea -- let's do more of those!"]

    html_name = 'The_Zen_of_Python.html'
    build_web(content[randint(0, len(content))], html_name)


if __name__ == "__main__":
    main()
