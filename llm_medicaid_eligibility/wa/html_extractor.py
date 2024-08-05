def html_extractor(soup):
    return soup.body.main if soup.body.find("main") else soup.body
