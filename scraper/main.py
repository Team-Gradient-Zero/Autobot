from requests_html import HTMLSession

class Reviews:
    def __init__(self, asin) -> None:
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}
        self.url = f'https://www.amazon.co.uk/product-reviews/{self.asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber='
    def paganation(self, page):
        r = self.session.get(self.url+str(page))
        # r.html.render(sleep=1)
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')
    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]', first = True).text
            rating = review.find('i[data-hook=review-star-rating] span', first = True).text
            body = review.find('span[data-hook=review-body] span', first = True).text.replace('\n', '').strip()

            data = {
                'title': title,
                'rating': rating,
                'body': body[:100]
            }
            total.append(data)
        return total

if __name__ == '__main__':
    amz = Reviews('B0797QCXS6')
    reviews = amz.paganation(1)
    print(amz.parse(reviews))