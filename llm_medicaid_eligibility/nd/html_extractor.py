def html_extractor(soup):
    return (
        soup.body.find("div", role="main")
        if soup.body.find("div", role="main")
        else soup.body
    )
