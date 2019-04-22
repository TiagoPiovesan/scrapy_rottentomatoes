from movie.models import Movie

def clean_title(param):
    return param

def clean_critics_consensus(param):
    return ' '.join(param)

def clean_average_grade(param):
    param = param.strip().replace('/5', '')
    return param

def clean_poster(param):
    if param:
        param = param[0]['path']
    return param

def clean_amount_reviews(param):
    return param.strip()

def clean_approval_percentage(param):
    return param.strip().replace('%', '')


class CrawlingPipeline(object):
    def process_item(self, item, spider):
        title = clean_title(item['title'])
        critics_consensus = clean_critics_consensus(item['critics_consensus'])
        average_grade = clean_average_grade(item['average_grade'])
        poster = clean_poster(item['images'])
        amount_reviews = clean_amount_reviews(item['amount_reviews'])
        approval_percentage = clean_approval_percentage(item['approval_percentage'])

        Movie.objects.create(
            title=title,
            critics_consensus=critics_consensus,
            average_grade=average_grade,
            poster=poster,
            amount_reviews=amount_reviews,
            approval_percentage=approval_percentage,
        )

        return item
