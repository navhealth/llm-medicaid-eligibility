def html_extractor(soup):
    return (
        soup.body.find("div", class_="body")
        if soup.body.find("div", class_="body")
        else soup.body
    )
