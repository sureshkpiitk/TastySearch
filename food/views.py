from django.conf import settings
from django.shortcuts import render

# Create your views here.
MAX_LIMIT = 1000
doc_list = []


def create_doc():
    with open('{}/food/finefoods.txt'.format(settings.BASE_DIR), 'r', encoding="ISO-8859-1") as f:
        line = f.readline()
        temp_doc = dict()
        terms = set()
        while line and len(doc_list) < MAX_LIMIT:
            if line == '\n':
                line = f.readline()
                temp_doc = dict()
                terms = set()
                continue
            if "product/productId: " in line:
                doc_id = line[19:]
                temp_doc['productId'] = doc_id.strip()
            line = f.readline()
            if 'review/userId: ' in line:
                user_id = line[15:]
                temp_doc['userId'] = user_id.strip()
            line = f.readline()
            if 'review/profileName: ' in line:
                profile_name = line[20:]
                temp_doc['profileName'] = profile_name.strip()
            line = f.readline()
            if 'review/helpfulness: ' in line:
                review = line[20:]
                temp_doc['helpfulness'] = review.strip()
            line = f.readline()
            if 'review/score: 'in line:
                score = line[14:]
                temp_doc['score'] = float(score.strip())
            line = f.readline()
            if 'review/time: ' in line:
                time = line[13:]
                temp_doc['time'] = time.strip()
            line = f.readline()
            if 'review/summary: ' in line:
                summary = line[16:]
                terms.update(summary.strip().split(' '))
                temp_doc['keys'] = terms
                temp_doc['summary'] = summary
            line = f.readline()
            if 'review/text: ' in line:
                text = line[13:]
                terms.update(text.strip().split(' '))
                temp_doc['text'] = text
            line = f.readline()
            if line == '\n':
                doc_list.append(temp_doc)


def search(request):
    query = request.POST.get('query').strip()
    tokens = query.split(' ')
    limit = request.POST.get('limit').strip()
    length = len(tokens)
    result_list = list()
    if not doc_list:
        create_doc()
    for item in doc_list:
        count = 0
        for token in tokens:
            if token in item['keys']:
                count += 1
        if count:
            result_list.append((item, count/length, item['score']))

    result_list = sorted(result_list, key=lambda result_list:result_list[1], reverse=True)
    result_list = sorted(result_list, key=lambda result_list:result_list[2], reverse=True)
    result_list = result_list[:int(limit)] if limit else result_list
    return render(request, 'search.html', {'results': result_list})


def home(request):
    return render(request, 'home.html')
